import json

# Load the JSON file
file_path = (
    "/Users/id05309/Documents/tfm/mistral/evaluate-dataset/final_ragas_dataset_30.json"
)

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"File {file_path} not found.")
    exit()

# Extract and print questions
questions = []
for item in data.get("questions", []):
    question = item.get("question")
    if question:
        questions.append(question)

# Print all questions
print("\nExtracted Questions:")
for idx, question in enumerate(questions, start=1):
    print(f"{idx}. {question}")
