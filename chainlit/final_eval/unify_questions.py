import os
import json
import re  # For extracting numbers from filenames


def create_unified_full_content_json(
    folder_path, output_filename="unified_full_content_ordered.json"
):
    """
    Traverses numerically named JSON files (e.g., question_1.json, question_2.json)
    in a folder, collects their full JSON content in order, and saves them
    into a new unified JSON file under a 'questions' key.

    Args:
        folder_path (str): The path to the folder containing the JSON files.
        output_filename (str): The name for the output JSON file.
    """
    ordered_file_data_list = []

    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    print(f"Processing files in folder: {folder_path}")

    file_list_to_process = []
    for filename in os.listdir(folder_path):
        # Regex to match 'question_' followed by one or more digits, then '.json'
        match = re.fullmatch(r"question_(\d+)\.json", filename, re.IGNORECASE)
        if match:
            # Extract the number and convert to integer for sorting
            file_number = int(match.group(1))
            file_list_to_process.append(
                (file_number, filename, os.path.join(folder_path, filename))
            )
        elif filename.lower().endswith(".json"):  # Inform about other JSONs
            print(
                f"  Info: Skipping file '{filename}' as it does not match 'question_NUMBER.json' pattern."
            )

    # Sort files based on the extracted number
    file_list_to_process.sort()

    if not file_list_to_process:
        print("No files matching the pattern 'question_NUMBER.json' found.")
        return

    for file_number, filename, file_path in file_list_to_process:
        print(f"  Processing file: {filename} (Order: {file_number})...")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Add the entire content of the JSON file to our list
                ordered_file_data_list.append(data)
        except json.JSONDecodeError:
            print(
                f"    Error: Could not decode JSON from {filename}. It will be skipped."
            )
            # Optionally, you could append a placeholder or error object:
            # ordered_file_data_list.append({"error": "JSONDecodeError", "filename": filename})
        except Exception as e:
            print(
                f"    Error: An unexpected error occurred with {filename}: {e}. It will be skipped."
            )
            # Optionally, append placeholder:
            # ordered_file_data_list.append({"error": str(e), "filename": filename})

    if not ordered_file_data_list:
        print("No JSON data was successfully extracted and ordered.")
        return

    # The final structure: a dictionary with a single key "questions",
    # whose value is the list of JSON objects (the content of each file).
    unified_output = {"questions": ordered_file_data_list}

    try:
        with open(output_filename, "w", encoding="utf-8") as outfile:
            json.dump(unified_output, outfile, indent=2)  # indent=2 for pretty printing
        print(
            f"\nSuccessfully created '{output_filename}' with content from {len(ordered_file_data_list)} files, processed in order."
        )
    except Exception as e:
        print(f"\nError: Could not write to output file '{output_filename}': {e}")


if __name__ == "__main__":
    input_folder = "/Users/id05309/Documents/tfm/chainlit/final_eval/final-v1-100/logs"
    # It's good practice to save the output in the current working directory
    # or a specified output directory, rather than potentially inside the input folder.
    output_file = "ragas_dataset_final-v1-100/all_question_files_content_ordered.json"
    create_unified_full_content_json(input_folder.strip(), output_file)

    # Example usage (if you have a folder named 'my_json_files' in the same directory as the script):
    # create_unified_full_content_json("./my_json_files", "all_question_files_content_ordered.json")
