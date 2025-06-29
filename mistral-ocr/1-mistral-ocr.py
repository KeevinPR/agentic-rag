import os
import base64
import json
from pathlib import Path
from mistralai import Mistral
import base64
from PIL import Image
import io

# Config
api_key = "DUb09JqF91eRXOZkCUd3rPCIjp9DUse2"
client = Mistral(api_key=api_key)
data_dir = Path("/Users/id05309/Documents/tfm/data")
output_dir = Path("/Users/id05309/Documents/tfm/mistral/mistral-markdown")
images_dir = output_dir / "images"
output_dir.mkdir(parents=True, exist_ok=True)
images_dir.mkdir(parents=True, exist_ok=True)


def get_pdf_files(root_dir):
    return [p for p in root_dir.rglob("*.pdf") if p.is_file()]


def save_image(base64_image, paper_id, image_index):
    """Save a base64 encoded image to disk."""
    try:
        # Decode base64 image
        image_data = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(image_data))

        # Create paper-specific image directory
        paper_image_dir = images_dir / paper_id
        paper_image_dir.mkdir(parents=True, exist_ok=True)

        # Save image
        image_path = paper_image_dir / f"img-{image_index}.png"
        image.save(image_path)
        return image_path.name
    except Exception as e:
        print(f"Error saving image: {e}")
        return None


def save_markdown(ocr_response, out_path, paper_id):
    """Save markdown content and extract images."""
    # Process each page
    markdown_parts = []
    image_mapping = {}

    for page_idx, page in enumerate(ocr_response.pages):
        # Get markdown content
        markdown_parts.append(page.markdown)

        # Process images if available
        if hasattr(page, "images") and page.images:
            for img_idx, img in enumerate(page.images):
                if hasattr(img, "base64") and img.base64:
                    image_filename = save_image(
                        img.base64, paper_id, f"{page_idx}_{img_idx}"
                    )
                    if image_filename:
                        # Add image reference to markdown
                        image_ref = (
                            f"![{image_filename}](images/{paper_id}/{image_filename})"
                        )
                        markdown_parts.append(image_ref)
                        image_mapping[f"img-{page_idx}_{img_idx}"] = image_filename

    # Combine all markdown content
    markdown = "\n\n".join(markdown_parts)

    # Save markdown
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    # Save image mapping
    mapping_path = out_path.with_suffix(".json")
    with open(mapping_path, "w", encoding="utf-8") as f:
        json.dump({"paper_id": paper_id, "image_mapping": image_mapping}, f, indent=2)


def process_pdf(pdf_path):
    """Process PDF with OCR and extract images."""
    # Upload PDF
    uploaded = client.files.upload(
        file={"file_name": pdf_path.name, "content": open(pdf_path, "rb")},
        purpose="ocr",
    )
    # Get signed URL
    signed_url = client.files.get_signed_url(file_id=uploaded.id)
    # OCR process with images
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={"type": "document_url", "document_url": signed_url.url},
        include_image_base64=True,
    )
    return ocr_response


# Main loop
pdf_files = get_pdf_files(data_dir)
for pdf_path in pdf_files:
    rel_path = pdf_path.relative_to(data_dir).with_suffix(".md")
    out_path = output_dir / rel_path
    paper_id = pdf_path.stem

    if out_path.exists():
        print(f"Skipping already processed: {pdf_path}")
        continue

    print(f"Processing: {pdf_path}")
    try:
        ocr_response = process_pdf(pdf_path)
        save_markdown(ocr_response, out_path, paper_id)
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Failed to process {pdf_path}: {e}")

print("All unprocessed PDFs have been processed.")
