import os
import csv
from pathlib import Path

# Base directory
base_dir = "/Users/id05309/Documents/tfm/data"

# Years to process
years = range(2000, 2025)

# List to store all papers with their year
all_papers = []

for year in years:
    year_dir = os.path.join(base_dir, str(year))

    # Skip if the year directory doesn't exist
    if not os.path.exists(year_dir):
        print(f"Directory for year {year} not found, skipping...")
        continue

    # Iterate through files in the year directory
    for file in os.listdir(year_dir):
        if file.lower().endswith(".pdf"):
            # Store as (year, paper_name)
            paper_name = file.replace(".pdf", "")
            all_papers.append((year, paper_name))

    print(
        f"Processed {year}: found {len([p for p in all_papers if p[0] == year])} papers"
    )

# Write all papers to a single CSV
output_file = "all_papers.csv"
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["year", "paper_name"])  # Header
    for year, paper in all_papers:
        writer.writerow([year, paper])

print(f"\nCreated {output_file} with {len(all_papers)} papers across all years")
print(f"Total number of files processed: {len(all_papers)}")
print("Processing complete!")
