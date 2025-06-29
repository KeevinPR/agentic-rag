import json

# Load JSON from file (adjust the file path as needed)
with open(
    "/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2/all_papers_data_simple_metadata_cleaned.json",
    "r",
    encoding="utf-8",
) as f:
    data = json.load(f)

# Global counter for all chunks
global_idx = 1
# Iterate over each paper entry and update its chunks
for paper_entry in data.get("papers", []):
    chunks = paper_entry.get("chunks", [])
    for chunk in chunks:
        chunk["chunk_id"] = global_idx
        global_idx += 1

# Save updated JSON to a new file (adjust the file path as needed)
with open(
    "/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2/all_papers_data_simple_metadata_cleaned_ids.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(
    "Chunk IDs updated and saved to all_papers_data_simple_metadata_cleaned_cut_ids.json"
)
