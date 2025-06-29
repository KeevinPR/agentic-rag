import os
import json
from pathlib import Path
from fuzzywuzzy import fuzz
import string

# Define paths
BASE_DIR = Path("/Users/id05309/Documents/tfm/data")
CHUNKS_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2/all_papers_data_simple.json"
OUTPUT_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2/all_papers_data_simple_metadata.json"
UNMATCHED_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2/unmatched_papers.json"
# Add new constant for title mapping file
TITLE_MAPPING_FILE = "/Users/id05309/Documents/tfm/mistral/title_mappings.json"


def normalize_title(title):
    """Normalize a title by converting to lowercase and removing punctuation."""
    return "".join(c for c in title.lower() if c not in string.punctuation)


def extract_title_from_filename(filename):
    """Extract potential title from filename."""
    base_name = filename.replace(".md", "")
    dot_index = base_name.find(". ")
    dash_index = base_name.find(" - ")
    if dot_index != -1 and (dash_index == -1 or dot_index < dash_index):
        title = base_name[:dot_index]
    elif dash_index != -1:
        title = base_name[:dash_index]
    else:
        title = base_name
    return title.rstrip(".,- ").strip()


def load_metadata():
    """Load metadata organized by year."""
    metadata_by_year = {}

    for year_dir in BASE_DIR.iterdir():
        if year_dir.is_dir():
            year = year_dir.name
            json_file = year_dir / f"metadata_{year}.json"

            if json_file.exists():
                print(f"Processing metadata for year: {year}")
                with open(json_file, "r", encoding="utf-8") as f:
                    papers = json.load(f)
                    metadata_by_year[year] = {
                        paper["title"]: {
                            "title": paper["title"],
                            "authors": paper["authors"],
                            "description": paper["description"],
                            "paper_link": paper["paper_link"],
                            "year": paper["year"],
                        }
                        for paper in papers
                    }
                print(f"Loaded {len(metadata_by_year[year])} papers for year {year}")

    return metadata_by_year


def get_pdf_path_for_md(md_filename):
    """Find the corresponding PDF file in the data directory."""
    md_name = md_filename.replace(".md", "")

    # Search through all year directories
    for year_dir in BASE_DIR.iterdir():
        if year_dir.is_dir():
            # Look for PDF files in this year directory
            for pdf_file in year_dir.glob("*.pdf"):
                pdf_name = pdf_file.stem
                if pdf_name == md_name:
                    return pdf_file, year_dir.name

    return None, None


def augment_papers(metadata_by_year):
    """Augment papers with metadata using prefix and fuzzy matching within the correct year."""
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    no_match = 0
    unmatched_papers = []
    # Dictionary to track title mappings
    title_mappings = {}

    # Process each paper in the papers array
    for paper_data in data["papers"]:
        md_filename = paper_data["paper"]["source_file"]

        # Find the corresponding PDF file and its year
        pdf_path, year = get_pdf_path_for_md(md_filename)

        if not pdf_path or not year:
            print(f"Warning: Could not find PDF file for {md_filename}")
            unmatched_papers.append(
                {"file": md_filename, "reason": "PDF file not found"}
            )
            continue

        if year not in metadata_by_year:
            print(f"Warning: No metadata found for year {year}")
            unmatched_papers.append(
                {"file": md_filename, "year": year, "reason": "No metadata for year"}
            )
            continue

        file_title = extract_title_from_filename(md_filename)
        norm_file_title = normalize_title(file_title)

        # Get metadata for this year
        year_metadata = metadata_by_year[year]
        metadata_titles = list(year_metadata.keys())
        norm_metadata_titles = {normalize_title(t): t for t in metadata_titles}

        # Step 1: Try prefix match
        matched_title = None
        for norm_meta_title, original_meta_title in norm_metadata_titles.items():
            if norm_meta_title.startswith(norm_file_title):
                matched_title = original_meta_title
                # Add to title mapping
                title_mappings[file_title] = matched_title
                print(
                    f"Matched (prefix): '{file_title}' to '{matched_title}' for year {year}"
                )
                break

        # Step 2: If no prefix match, try exact match
        if not matched_title and file_title in year_metadata:
            matched_title = file_title
            # Add to title mapping
            title_mappings[file_title] = matched_title
            print(f"Matched (exact): '{file_title}' for year {year}")

        # Step 3: If no exact match, use fuzzy matching
        if not matched_title:
            print(
                f"Warning: No exact/prefix match for file {md_filename} (year: {year}), trying fuzzy matching..."
            )
            for meta_title in metadata_titles:
                similarity = fuzz.ratio(norm_file_title, normalize_title(meta_title))
                if similarity >= 85:  # Adjust threshold as needed
                    matched_title = meta_title
                    # Add to title mapping
                    title_mappings[file_title] = matched_title
                    print(
                        f"Matched (fuzzy, score {similarity}): '{file_title}' to '{matched_title}' for year {year}"
                    )
                    break

        # Step 4: Augment paper if matched, otherwise log failure
        if matched_title:
            paper_metadata = year_metadata[matched_title]
            # Add metadata to paper level only, not to chunks
            paper_data["paper"].update(
                {
                    "title": paper_metadata["title"],
                    "authors": paper_metadata["authors"],
                    "abstract": paper_metadata["description"],
                    "paper_link": paper_metadata["paper_link"],
                    "year": paper_metadata["year"],
                }
            )
        else:
            no_match += 1
            print(f"Warning: No metadata match for file {md_filename} (year: {year})")
            unmatched_papers.append(
                {
                    "file": md_filename,
                    "year": year,
                    "reason": "No matching metadata found",
                }
            )

    print(f"Total unmatched files: {no_match}")

    # Save unmatched papers to a separate JSON file
    with open(UNMATCHED_FILE, "w", encoding="utf-8") as f:
        json.dump(unmatched_papers, f, indent=4, ensure_ascii=False)
    print(f"Unmatched papers saved to {UNMATCHED_FILE}")

    # Save title mappings to a JSON file
    with open(TITLE_MAPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(title_mappings, f, indent=4, ensure_ascii=False)
    print(f"Title mappings saved to {TITLE_MAPPING_FILE}")

    return data


def main():
    print("Loading metadata...")
    metadata_by_year = load_metadata()

    print("Augmenting papers with metadata...")
    augmented_data = augment_papers(metadata_by_year)

    print("Saving augmented data...")
    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(augmented_data, f, indent=4, ensure_ascii=False)

    print(f"Augmented data saved to {OUTPUT_FILE}")
    print(f"Total papers: {len(augmented_data['papers'])}")


if __name__ == "__main__":
    main()
