# Clean markdown files

import json
import re
from pathlib import Path

# Define paths
INPUT_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2/all_papers_data_simple_metadata.json"
OUTPUT_FILE = "/Users/id05309/Documents/tfm/mistral/chunked-markdown-simple-v2/all_papers_data_simple_metadata_cleaned.json"


def extract_images(text, paper_image_counter):
    """Extract image references and replace them with numbered placeholders.

    Args:
        text: Input text containing markdown image references
        paper_image_counter: Counter object for the paper's images

    Returns:
        tuple containing:
        - dict mapping placeholder IDs to image filenames
        - text with image references replaced by placeholders
    """
    # Find all markdown image references
    image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    images = {}

    def replace_image(match):
        image_path = match.group(2)
        placeholder = f"[IMAGE_{paper_image_counter['count']}]"
        images[placeholder] = image_path
        paper_image_counter["count"] += 1
        return placeholder

    # Replace images with placeholders
    clean_text = re.sub(image_pattern, replace_image, text)

    return images, clean_text


def clean_markdown_content(text, paper_image_counter):
    """Clean markdown content by removing unwanted tokens and formatting."""
    if not text:
        return text, {}

    # Extract images first
    images, text = extract_images(text, paper_image_counter)

    # Protect formula placeholders by temporarily replacing them
    formula_pattern = r"\[FORMULA_(\d+)\]"
    formula_placeholders = {}

    def replace_formula(match):
        placeholder = f"TEMPFORMULA{len(formula_placeholders)}PLACEHOLDER"
        formula_placeholders[placeholder] = f"[FORMULA_{match.group(1)}]"
        return placeholder

    # Replace formulas with temporary placeholders
    text = re.sub(formula_pattern, replace_formula, text)

    # First, handle the Unicode normalization in a more comprehensive way
    try:
        import unicodedata

        # Use NFKD normalization to decompose combined characters
        text = unicodedata.normalize("NFKD", text)

        # Create a function to convert Unicode to ASCII when possible
        def unicode_to_ascii(text):
            return "".join(
                [
                    c
                    for c in unicodedata.normalize("NFD", text)
                    if unicodedata.category(c)
                    != "Mn"  # Mn category represents diacritical marks
                ]
            )

        # Apply the function for an initial normalization
        text = unicode_to_ascii(text)

        # For special cases that aren't handled properly by the function above,
        # we can still use a replacement dictionary
        unicode_replacements = {
            # Special characters that might remain after normalization
            "\u00f1": "n",
            "\u00d1": "N",  # ñ/Ñ
            "\u00df": "ss",  # German eszett
            "\u20ac": "EUR",
            "\u00a3": "GBP",
            "\u00a5": "JPY",  # currency symbols
            "\u2013": "-",
            "\u2014": "--",  # en-dash and em-dash
            "\u2018": "'",
            "\u2019": "'",
            "\u201c": '"',
            "\u201d": '"',  # curved quotes
            "\u00b0": " degrees",  # degree symbol
            "\u00bd": "1/2",
            "\u00bc": "1/4",
            "\u00be": "3/4",  # fractions
            "\u00e7": "c",
            "\u00c7": "C",  # ç/Ç
            # Add more as needed
        }

        for unicode_char, ascii_replacement in unicode_replacements.items():
            text = text.replace(unicode_char, ascii_replacement)
    except ImportError:
        # If unicodedata module is not available, continue with the original text
        pass

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove markdown links but keep the text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)

    # Remove markdown headers
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)

    # Remove markdown emphasis
    text = re.sub(r"[*_]{1,2}([^*_]+)[*_]{1,2}", r"\1", text)

    # Remove markdown code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    # Remove inline code
    text = re.sub(r"`([^`]+)`", r"\1", text)

    # Remove markdown blockquotes
    text = re.sub(r"^\s*>\s*", "", text, flags=re.MULTILINE)

    # Remove horizontal rules
    text = re.sub(r"^\s*[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)

    # Remove multiple newlines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Apply the replacement dictionary
    for unicode_char, ascii_replacement in unicode_replacements.items():
        text = text.replace(unicode_char, ascii_replacement)

    try:
        # For any remaining non-ASCII characters that weren't explicitly handled,
        # either convert to closest ASCII or replace with underscore
        cleaned_text = []
        for c in text:
            if ord(c) < 128 or c.isspace():
                # ASCII characters and spaces remain unchanged
                cleaned_text.append(c)
            else:
                try:
                    # Try to convert to ASCII if possible
                    ascii_version = (
                        unicodedata.normalize("NFKD", c)
                        .encode("ascii", "ignore")
                        .decode("ascii")
                    )
                    if ascii_version:
                        cleaned_text.append(ascii_version)
                    else:
                        cleaned_text.append(
                            "_"
                        )  # Replace with underscore if no ASCII equivalent
                except:
                    cleaned_text.append("_")  # Fallback for any errors

        text = "".join(cleaned_text)
    except Exception as e:
        # If any error occurs during Unicode handling, fall back to a simpler approach
        print(f"Unicode normalization error: {e}")
        text = "".join(c if ord(c) < 128 or c.isspace() else "_" for c in text)

    # Restore formula placeholders
    for placeholder, formula in formula_placeholders.items():
        text = text.replace(placeholder, formula)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text, images


def clean_chunks():
    """Clean the content in all chunks."""
    print("Loading data...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Cleaning chunks...")
    cleaned_papers = 0
    cleaned_chunks = 0
    chunks_with_images = 0

    for paper in data["papers"]:
        cleaned_papers += 1
        # Initialize counter for this paper
        paper_image_counter = {"count": 0}

        for chunk in paper["chunks"]:
            if "page_content" in chunk:
                # Clean content and get images
                cleaned_content, images = clean_markdown_content(
                    chunk["page_content"], paper_image_counter
                )
                chunk["page_content"] = cleaned_content

                # Add image metadata
                if images:
                    chunks_with_images += 1
                    chunk["metadata"]["contains_image"] = True
                    chunk["metadata"]["images"] = (
                        images  # Store placeholder to filename mapping
                    )
                else:
                    chunk["metadata"]["contains_image"] = False
                    chunk["metadata"]["images"] = {}

                cleaned_chunks += 1

    print(f"Cleaned {cleaned_papers} papers and {cleaned_chunks} chunks")
    print(f"Found {chunks_with_images} chunks containing images")

    print("Saving cleaned data...")
    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Cleaned data saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    clean_chunks()
