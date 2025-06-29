import os
import re
import json
import logging
import argparse
from datetime import datetime


def setup_logging():
    """Configure logging to write to stdout and file."""
    logger = logging.getLogger("reference_extractor")
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handlers
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    info_handler = logging.FileHandler(
        os.path.join(log_dir, "reference_extraction.log"), mode="w"
    )
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)
    logger.addHandler(info_handler)

    error_handler = logging.FileHandler(
        os.path.join(log_dir, "reference_extraction_errors.log"), mode="w"
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)

    return logger


def get_markdown_files(root_dir, logger):
    """Walk through root_dir and return all Markdown file paths."""
    markdown_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                full_path = os.path.join(dirpath, filename)
                try:
                    if os.path.getsize(full_path) > 0:
                        markdown_files.append(full_path)
                except Exception as e:
                    logger.warning(f"Error checking file {full_path}: {e}")

    logger.info(f"Found {len(markdown_files)} Markdown files in {root_dir}")
    return markdown_files


def extract_references_section(md_content, logger):
    """Extract the references section from markdown content."""
    # Patterns to match reference section headers
    ref_header_patterns = [
        # Basic patterns
        r"(?:^|\n)#+\s*References?\s*\n",  # Matches # References
        r"(?:^|\n)####\s*References?\s*\n",  # Matches #### References
        r"(?:^|\n)##\s*References?\s*\n",  # Matches ## References
        r"(?:^|\n)###\s*References?\s*\n",  # Matches ### References
        # Patterns with formatting
        r"(?:^|\n)#+\s*\*\*References?\*\*\s*\n",  # Matches # **References**
        r"(?:^|\n)####\s*\*\*References?\*\*\s*\n",  # Matches #### **References**
        r"(?:^|\n)####\s*\*References?\*\s*\n",  # Matches #### *References*
        r"(?:^|\n)\*\*References?\*\*\s*\n",  # Matches **References**
        # Patterns with span elements
        r"(?:^|\n)#+\s*(?:<span[^>]*>.*?</span>)*\s*References?\s*\n",  # Matches # <span...></span>References
        r"(?:^|\n)#+\s*(?:<span[^>]*>.*?</span>)*\s*\*\*References?\*\*\s*\n",  # Matches # <span...></span>**References**
        r"(?:^|\n)####\s*(?:<span[^>]*>.*?</span>)*\s*References?\s*\n",  # Matches #### <span...></span>References
        r"(?:^|\n)###\s*(?:<span[^>]*>.*?</span>)*\s*References?\s*\n",  # Matches ### <span...></span>References
        r"(?:^|\n)##\s*(?:<span[^>]*>.*?</span>)*\s*References?\s*\n",  # Matches ## <span...></span>References
        r"(?:^|\n)####\s*(?:<span[^>]*>.*?</span>)*\s*\*\*References?\*\*\s*\n",  # Matches #### <span...></span>**References**
        # Patterns with numbering
        r"(?:^|\n)#+\s*\d+\.\s*REFERENCES?\s*\n",  # Matches # 8. REFERENCES
        r"(?:^|\n)####\s*\d+\.\s*REFERENCES?\s*\n",  # Matches #### 10. REFERENCES
        r"(?:^|\n)##\s*\d+\.\s*REFERENCES?\s*\n",  # Matches ## 12. REFERENCES
        r"(?:^|\n)####\s*\*\*\d+\.\s*REFERENCES?\*\*\s*\n",  # Matches #### **10. REFERENCES**
        r"(?:^|\n)##\s*\*\*\d+\.\s*REFERENCES?\*\*\s*\n",  # Matches ## **12. REFERENCES**
        r"(?:^|\n)#+\s*\*\*\d+\.\s*References?\*\*\s*\n",  # Matches # **6. REFERENCES**
        # Patterns with Roman numerals
        r"(?:^|\n)####\s*[IVX]+\.\s*REFERENCES?\s*\n",  # Matches #### VI. REFERENCES
        r"(?:^|\n)#+\s*[IVX]+\.\s*REFERENCES?\s*\n",  # Matches # VII. REFERENCES
        # Patterns with Roman numerals and formatting
        r"(?:^|\n)#+\s*\*\*[IVX]+\.\s*References?\*\*\s*\n",  # Matches # **7. References**
        # Bibliography patterns
        r"(?:^|\n)#+\s*Bibliography\s*\n",  # Matches # Bibliography
        r"(?:^|\n)####\s*Bibliography\s*\n",  # Matches #### Bibliography
        r"(?:^|\n)###\s*Bibliography\s*\n",  # Matches ### Bibliography
        r"(?:^|\n)###\s*\*\*Bibliography\*\*\s*\n",  # Matches ### **Bibliography**
        r"(?:^|\n)#+\s*\*\*Bibliography\*\*\s*\n",  # Matches # **Bibliography**
        # All caps variations
        r"(?:^|\n)#+\s*REFERENCES?\s*\n",  # Matches # REFERENCES
        r"(?:^|\n)####\s*REFERENCES?\s*\n",  # Matches #### REFERENCES
        r"(?:^|\n)##\s*REFERENCES?\s*\n",  # Matches ## REFERENCES
        r"(?:^|\n)###\s*REFERENCES?\s*\n",  # Matches ### REFERENCES
    ]

    # Try to find the references section
    for pattern in ref_header_patterns:
        match = re.search(pattern, md_content, re.IGNORECASE)
        if match:
            # Find the starting position of the references section
            start_pos = match.start()
            header_text = match.group(0).strip()

            # Get the position after the header
            content_start_pos = match.end()

            # Find the next header or end of document
            next_header = re.search(r"\n#+\s+", md_content[content_start_pos:])
            if next_header:
                end_pos = content_start_pos + next_header.start()
            else:
                end_pos = len(md_content)

            # Extract the references section with its header
            full_section = md_content[start_pos:end_pos].strip()
            ref_content = md_content[content_start_pos:end_pos].strip()

            # Extract individual reference entries
            references = extract_individual_references(ref_content, logger)

            logger.info(f"Found references section with {len(references)} references")

            return {
                "header": header_text.strip(),
                "content": ref_content,
                "references": references,
                "reference_count": len(references),
                "pattern_matched": pattern,
            }

    logger.warning("No references section found")
    return None


def remove_references_section(md_content, logger):
    """Remove the references section from markdown content."""
    # Use the same patterns as in extract_references_section
    ref_header_patterns = [
        # Basic patterns
        r"(?:^|\n)#+\s*References?\s*\n",  # Matches # References
        r"(?:^|\n)####\s*References?\s*\n",  # Matches #### References
        r"(?:^|\n)##\s*References?\s*\n",  # Matches ## References
        r"(?:^|\n)###\s*References?\s*\n",  # Matches ### References
        # Patterns with formatting
        r"(?:^|\n)#+\s*\*\*References?\*\*\s*\n",  # Matches # **References**
        r"(?:^|\n)####\s*\*\*References?\*\*\s*\n",  # Matches #### **References**
        r"(?:^|\n)####\s*\*References?\*\s*\n",  # Matches #### *References*
        r"(?:^|\n)\*\*References?\*\*\s*\n",  # Matches **References**
        # Patterns with span elements
        r"(?:^|\n)#+\s*(?:<span[^>]*>.*?</span>)*\s*References?\s*\n",  # Matches # <span...></span>References
        r"(?:^|\n)#+\s*(?:<span[^>]*>.*?</span>)*\s*\*\*References?\*\*\s*\n",  # Matches # <span...></span>**References**
        r"(?:^|\n)####\s*(?:<span[^>]*>.*?</span>)*\s*References?\s*\n",  # Matches #### <span...></span>References
        r"(?:^|\n)###\s*(?:<span[^>]*>.*?</span>)*\s*References?\s*\n",  # Matches ### <span...></span>References
        r"(?:^|\n)##\s*(?:<span[^>]*>.*?</span>)*\s*References?\s*\n",  # Matches ## <span...></span>References
        r"(?:^|\n)####\s*(?:<span[^>]*>.*?</span>)*\s*\*\*References?\*\*\s*\n",  # Matches #### <span...></span>**References**
        # Patterns with numbering
        r"(?:^|\n)#+\s*\d+\.\s*REFERENCES?\s*\n",  # Matches # 8. REFERENCES
        r"(?:^|\n)####\s*\d+\.\s*REFERENCES?\s*\n",  # Matches #### 10. REFERENCES
        r"(?:^|\n)##\s*\d+\.\s*REFERENCES?\s*\n",  # Matches ## 12. REFERENCES
        r"(?:^|\n)####\s*\*\*\d+\.\s*REFERENCES?\*\*\s*\n",  # Matches #### **10. REFERENCES**
        r"(?:^|\n)##\s*\*\*\d+\.\s*REFERENCES?\*\*\s*\n",  # Matches ## **12. REFERENCES**
        r"(?:^|\n)#+\s*\*\*\d+\.\s*References?\*\*\s*\n",  # Matches # **6. REFERENCES**
        # Patterns with Roman numerals
        r"(?:^|\n)####\s*[IVX]+\.\s*REFERENCES?\s*\n",  # Matches #### VI. REFERENCES
        r"(?:^|\n)#+\s*[IVX]+\.\s*REFERENCES?\s*\n",  # Matches # VII. REFERENCES
        # Patterns with Roman numerals and formatting
        r"(?:^|\n)#+\s*\*\*[IVX]+\.\s*References?\*\*\s*\n",  # Matches # **7. References**
        # Bibliography patterns
        r"(?:^|\n)#+\s*Bibliography\s*\n",  # Matches # Bibliography
        r"(?:^|\n)####\s*Bibliography\s*\n",  # Matches #### Bibliography
        r"(?:^|\n)###\s*Bibliography\s*\n",  # Matches ### Bibliography
        r"(?:^|\n)###\s*\*\*Bibliography\*\*\s*\n",  # Matches ### **Bibliography**
        r"(?:^|\n)#+\s*\*\*Bibliography\*\*\s*\n",  # Matches # **Bibliography**
        # All caps variations
        r"(?:^|\n)#+\s*REFERENCES?\s*\n",  # Matches # REFERENCES
        r"(?:^|\n)####\s*REFERENCES?\s*\n",  # Matches #### REFERENCES
        r"(?:^|\n)##\s*REFERENCES?\s*\n",  # Matches ## REFERENCES
        r"(?:^|\n)###\s*REFERENCES?\s*\n",  # Matches ### REFERENCES
    ]

    modified_content = md_content
    for pattern in ref_header_patterns:
        match = re.search(pattern, md_content, re.IGNORECASE)
        if match:
            # Find the starting position of the references section
            start_pos = match.start()

            # Find the next header or end of document
            content_start_pos = match.end()
            next_header = re.search(r"\n#+\s+", md_content[content_start_pos:])
            if next_header:
                end_pos = content_start_pos + next_header.start()
            else:
                end_pos = len(md_content)

            # Remove the references section
            modified_content = md_content[:start_pos] + md_content[end_pos:]
            logger.info("References section removed from document")
            return modified_content

    logger.warning("No references section found to remove")
    return modified_content


def extract_individual_references(ref_content, logger):
    """Extract individual references from the references section."""
    references = []

    # Common patterns for reference entries
    reference_patterns = [
        # Numbered references: [1] Author et al. (2000)...
        r"(?:^|\n)\[(\d+)\]\s+(.*?)(?=\n\[\d+\]|\n\n|$)",
        # Numbered references: 1. Author et al. (2000)...
        r"(?:^|\n)(\d+)\.\s+(.*?)(?=\n\d+\.|\n\n|$)",
        # Numbered with brackets: [1] Author et al. (2000)...
        r"(?:^|\n)\[(\d+)\]\s+(.*?)(?=\n\[\d+\]|\n\n|$)",
        # Bullet points: - Author et al. (2000)...
        r"(?:^|\n)-\s+(.*?)(?=\n-|\n\n|$)",
        # Simple lines (fallback): Author et al. (2000)...
        r"(?:^|\n)([A-Z][^#\n]+?)(?=\n[A-Z]|\n\n|$)",
    ]

    # Try each pattern
    for pattern in reference_patterns:
        matches = re.finditer(pattern, "\n" + ref_content, re.MULTILINE | re.DOTALL)
        temp_refs = []

        for match in matches:
            if len(match.groups()) == 2:  # Numbered reference
                ref_num, ref_text = match.groups()
                temp_refs.append({"ref_id": ref_num, "text": ref_text.strip()})
            else:  # Non-numbered reference
                ref_text = match.group(1)
                temp_refs.append(
                    {"ref_id": str(len(temp_refs) + 1), "text": ref_text.strip()}
                )

        # If we found references with this pattern, use them and stop
        if temp_refs:
            references = temp_refs
            break

    # If no patterns matched but there's content, fall back to splitting by newlines
    if not references and ref_content.strip():
        lines = [line.strip() for line in ref_content.split("\n") if line.strip()]
        for i, line in enumerate(lines):
            references.append({"ref_id": str(i + 1), "text": line})

    return references


def extract_paper_metadata(file_path):
    """Extract basic metadata from the paper file path."""
    # Extract year from filepath (assuming the directory structure includes year)
    year_match = re.search(r"/(\d{4})/", file_path)
    year = year_match.group(1) if year_match else "Unknown"

    # Extract paper title from filename
    filename = os.path.basename(file_path)
    title = os.path.splitext(filename)[0]

    return {"file_path": file_path, "filename": filename, "title": title, "year": year}


def extract_tables(md_content, logger):
    """Extract tables from markdown content and convert to JSONB-compatible format."""
    tables = []

    # First, find all potential table sections
    # Look for lines that start with | and contain at least one more |
    table_sections = []
    lines = md_content.split("\n")
    current_section = []
    in_table = False
    table_title = None
    table_number = None
    title_lines = []

    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "|" in line[1:]:
            if not in_table:
                in_table = True
                # Look for table title in preceding lines (up to 5 lines back)
                for j in range(max(0, i - 5), i):
                    prev_line = lines[j].strip()
                    if prev_line:
                        # Try to match common table title patterns
                        # Pattern 1: Table 1: Title
                        title_match = re.match(
                            r"^Table\s+(\d+)[.:]\s*(.*)$", prev_line, re.IGNORECASE
                        )
                        if title_match:
                            table_number = title_match.group(1)
                            table_title = title_match.group(2).strip()
                            break
                        # Pattern 2: TABLE I or Table I
                        roman_match = re.match(
                            r"^TABLE\s+([IVX]+)[.:]?\s*(.*)$", prev_line, re.IGNORECASE
                        )
                        if roman_match:
                            table_number = roman_match.group(1)
                            # If there's a title on the same line, use it
                            if roman_match.group(2).strip():
                                table_title = roman_match.group(2).strip()
                            else:
                                # Otherwise, collect the next line as title
                                if j + 1 < i:
                                    table_title = lines[j + 1].strip()
                            break
                        # Pattern 3: Just "Table" or "TABLE" followed by anything
                        elif re.match(r"^TABLE\s+", prev_line, re.IGNORECASE):
                            # First try to extract number
                            num_match = re.search(
                                r"TABLE\s+([IVX]+|\d+)[.:]?", prev_line, re.IGNORECASE
                            )
                            if num_match:
                                table_number = num_match.group(1)

                            # Collect all lines until we hit a blank line or table
                            title_lines = [prev_line]
                            k = j + 1
                            while (
                                k < i
                                and lines[k].strip()
                                and not lines[k].strip().startswith("|")
                            ):
                                title_lines.append(lines[k].strip())
                                k += 1

                            # Join all title lines, removing the first line if it's just the number
                            if len(title_lines) > 1:
                                table_title = " ".join(title_lines[1:])
                            else:
                                table_title = " ".join(title_lines)
                            break
            current_section.append(line)
        elif in_table:
            if line.strip() and not line.strip().startswith("|"):
                in_table = False
                if (
                    len(current_section) >= 3
                ):  # At least header, separator, and one data row
                    table_sections.append((table_number, table_title, current_section))
                current_section = []
                table_title = None
                table_number = None
                title_lines = []
            elif line.strip():
                current_section.append(line)

    # Don't forget the last table if we're still in one
    if in_table and len(current_section) >= 3:
        table_sections.append((table_number, table_title, current_section))

    # Process each table section
    for table_number, table_title, table_lines in table_sections:
        try:
            # Extract headers
            headers = [h.strip() for h in table_lines[0].split("|")[1:-1]]

            # Skip separator line
            data_rows = []
            for line in table_lines[2:]:
                if line.strip():
                    # Extract cell values and clean them
                    cells = [cell.strip() for cell in line.split("|")[1:-1]]
                    if len(cells) == len(headers):
                        # Convert cells to appropriate types
                        processed_cells = []
                        for cell in cells:
                            try:
                                # Remove math expressions and special characters for number conversion
                                clean_cell = re.sub(
                                    r"\$.*?\$", "", cell
                                )  # Remove math expressions
                                clean_cell = re.sub(
                                    r"\\#", "", clean_cell
                                )  # Remove escaped #
                                clean_cell = re.sub(
                                    r"[^\d.-]", "", clean_cell
                                ).strip()  # Keep only numbers, dots, and minus

                                if clean_cell and "." in clean_cell:
                                    processed_cells.append(float(clean_cell))
                                elif clean_cell:
                                    processed_cells.append(int(clean_cell))
                                else:
                                    processed_cells.append(cell)
                            except ValueError:
                                # Keep as string if not a number
                                processed_cells.append(cell)
                        data_rows.append(processed_cells)

            if data_rows:
                table_data = {
                    "table_number": table_number,
                    "table_title": table_title,
                    "headers": headers,
                    "rows": data_rows,
                    "row_count": len(data_rows),
                    "column_count": len(headers),
                }
                tables.append(table_data)

        except Exception as e:
            logger.warning(f"Error processing table: {str(e)}")
            continue

    logger.info(f"Extracted {len(tables)} tables from content")
    return tables


def remove_tables_section(md_content, logger):
    """Remove tables from markdown content."""
    lines = md_content.split("\n")
    modified_lines = []
    in_table = False
    skip_lines = 0

    for i, line in enumerate(lines):
        if skip_lines > 0:
            skip_lines -= 1
            continue

        if line.strip().startswith("|") and "|" in line[1:]:
            if not in_table:
                in_table = True
                # Look back up to 3 lines for table title
                for j in range(max(0, i - 3), i):
                    if lines[j].strip().startswith("Table"):
                        modified_lines.pop()  # Remove the table title line
                        break
            skip_lines = 1  # Skip the current line (table header)
        elif in_table:
            if line.strip() and not line.strip().startswith("|"):
                in_table = False
                modified_lines.append(line)
            elif not line.strip():
                in_table = False
                modified_lines.append(line)
        else:
            modified_lines.append(line)

    return "\n".join(modified_lines)


def process_markdown_file(file_path, logger):
    """Process a single markdown file to extract references and tables."""
    try:
        # Read the markdown content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract paper metadata
        metadata = extract_paper_metadata(file_path)

        # Extract references
        references_data = extract_references_section(content, logger)

        # Extract tables
        tables_data = extract_tables(content, logger)

        result = {
            "metadata": metadata,
            "references": references_data,
            "tables": tables_data,
        }

        return result

    except Exception as e:
        logger.error(f"Error processing file {file_path}: {str(e)}", exc_info=True)
        return {
            "metadata": extract_paper_metadata(file_path),
            "references": None,
            "tables": None,
            "error": str(e),
        }


def main():
    """Main function to run the reference extraction pipeline."""
    # Hardcoded paths
    input_dir = "/Users/id05309/Documents/tfm/mistral/mistral-markdown"
    output_dir = (
        "/Users/id05309/Documents/tfm/mistral/mistral-markdown-no-ref-no-tables"
    )
    references_output_dir = output_dir  # Save modified markdowns to the same output dir

    # Setup logging
    logger = setup_logging()
    logger.info(f"Starting reference extraction from {input_dir}")

    # Create output directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "papers"), exist_ok=True)
    os.makedirs(
        os.path.join(output_dir, "tables"), exist_ok=True
    )  # New directory for tables
    os.makedirs(references_output_dir, exist_ok=True)

    # Get all .md files
    markdown_files = []
    for dirpath, _, filenames in os.walk(input_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                full_path = os.path.join(dirpath, filename)
                try:
                    if os.path.getsize(full_path) > 0:
                        markdown_files.append(full_path)
                except Exception as e:
                    logger.warning(f"Error checking file {full_path}: {e}")
    logger.info(f"Found {len(markdown_files)} .md files in {input_dir}")

    # Initialize results container
    results = {
        "extraction_date": datetime.now().isoformat(),
        "total_papers": len(markdown_files),
        "papers_with_references": 0,
        "total_references_extracted": 0,
        "papers_with_tables": 0,
        "total_tables_extracted": 0,
        "papers": [],
    }

    # Initialize container for papers with missing references
    missing_references_data = {
        "extraction_date": datetime.now().isoformat(),
        "total_papers_missing_references": 0,
        "papers": [],
    }

    # Process each file
    for file_path in markdown_files:
        logger.info(f"Processing {file_path}")

        try:
            # Read the markdown content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract paper metadata
            metadata = extract_paper_metadata(file_path)

            # Extract references and tables
            references_data = extract_references_section(content, logger)
            tables_data = extract_tables(content, logger)

            paper_data = {
                "metadata": metadata,
                "references": references_data,
                "tables": tables_data,
            }

            # Create output file path with same directory structure relative to input dir
            rel_path = os.path.relpath(file_path, input_dir)
            output_file_path = os.path.join(references_output_dir, rel_path)
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

            # If references or tables found, write modified content to new location
            modified_content = content
            if references_data:
                modified_content = remove_references_section(modified_content, logger)
            if tables_data:
                modified_content = remove_tables_section(modified_content, logger)

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)
            logger.info(f"Removed references and tables, saved to: {output_file_path}")

            # Save tables separately if any found
            if tables_data:
                paper_id = metadata["title"].replace(" ", "_")
                tables_dir = os.path.join(output_dir, "tables")
                tables_output = os.path.join(tables_dir, f"{paper_id}_tables.json")
                with open(tables_output, "w", encoding="utf-8") as f:
                    json.dump(
                        {"metadata": metadata, "tables": tables_data},
                        f,
                        indent=2,
                        ensure_ascii=False,
                    )
                results["papers_with_tables"] += 1
                results["total_tables_extracted"] += len(tables_data)

            # Add to results
            results["papers"].append(paper_data)

            # Update statistics
            if paper_data.get("references"):
                results["papers_with_references"] += 1
                results["total_references_extracted"] += paper_data["references"][
                    "reference_count"
                ]

        except Exception as e:
            logger.error(f"Error processing file {file_path}: {str(e)}", exc_info=True)
            metadata = extract_paper_metadata(file_path)
            results["papers"].append(
                {
                    "metadata": metadata,
                    "references": None,
                    "tables": None,
                    "error": str(e),
                }
            )
            missing_references_data["papers"].append(
                {"metadata": metadata, "reason": f"Error: {str(e)}"}
            )

    # Update total count of papers with missing references
    missing_references_data["total_papers_missing_references"] = len(
        missing_references_data["papers"]
    )

    # Log papers without references
    papers_without_refs = [
        p["metadata"]["filename"] for p in results["papers"] if not p.get("references")
    ]
    if papers_without_refs:
        logger.info(f"Found {len(papers_without_refs)} papers without references:")
        for paper_name in papers_without_refs:
            logger.info(f"  - {paper_name}")

    # Save results to JSON file
    output_file = os.path.join(output_dir, "extracted_references.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Save missing references to a separate JSON file
    missing_refs_file = os.path.join(output_dir, "missing_references.json")
    with open(missing_refs_file, "w", encoding="utf-8") as f:
        json.dump(missing_references_data, f, indent=2, ensure_ascii=False)

    logger.info(
        f"Reference extraction complete. Processed {len(markdown_files)} papers."
    )
    logger.info(f"Found references in {results['papers_with_references']} papers.")
    logger.info(f"Extracted {results['total_references_extracted']} total references.")
    logger.info(f"Found tables in {results['papers_with_tables']} papers.")
    logger.info(f"Extracted {results['total_tables_extracted']} total tables.")
    logger.info(
        f"Papers with missing references: {missing_references_data['total_papers_missing_references']}"
    )
    logger.info(f"Results saved to {output_file}")
    logger.info(f"Missing references data saved to {missing_refs_file}")
    logger.info(f"Modified papers saved to {references_output_dir}")
    logger.info(f"Tables saved to {os.path.join(output_dir, 'tables')}")

    # Create individual files per paper
    for paper in results["papers"]:
        if paper.get("references") or paper.get("tables"):
            paper_id = paper["metadata"]["title"].replace(" ", "_")
            paper_dir = os.path.join(output_dir, "papers")
            paper_output = os.path.join(paper_dir, f"{paper_id}.json")
            with open(paper_output, "w", encoding="utf-8") as f:
                json.dump(paper, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
