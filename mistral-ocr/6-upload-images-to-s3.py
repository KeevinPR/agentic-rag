import json
import boto3
from pathlib import Path
import os
from urllib.parse import urljoin
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AWS Configuration - Loaded from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = "tfm-figures"

# File paths
INPUT_FILE = "/Users/id05309/Documents/agentic-rag/mistral/chunked-markdown/all_papers_data_metadata_cleaned.json"
OUTPUT_FILE = "/Users/id05309/Documents/agentic-rag/mistral/chunked-markdown/all_papers_data_metadata_with_s3.json"


def setup_s3_client():
    """Create and return an S3 client."""
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    )


def get_s3_url(bucket: str, key: str) -> str:
    """Generate the S3 URL for an object."""
    return f"https://{bucket}.s3.{AWS_REGION}.amazonaws.com/{key}"


def upload_image_to_s3(
    s3_client, paper_id: str, image_filename: str, image_path: str
) -> str:
    """Upload an image to S3 and return its URL.

    Args:
        s3_client: Boto3 S3 client
        paper_id: ID of the paper
        image_filename: Original filename of the image
        image_path: Local path to the image file

    Returns:
        S3 URL of the uploaded image
    """
    # Create a unique S3 key using paper_id and image filename
    s3_key = f"{paper_id}/{image_filename}"

    try:
        # Upload the file
        s3_client.upload_file(image_path, S3_BUCKET_NAME, s3_key)

        # Generate and return the S3 URL
        return get_s3_url(S3_BUCKET_NAME, s3_key)
    except Exception as e:
        print(f"Error uploading {image_filename} for paper {paper_id}: {str(e)}")
        return None


def process_images():
    """Process all images in the JSON file and upload them to S3."""
    print("Loading data...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Initialize S3 client
    s3_client = setup_s3_client()

    print("Processing images...")
    processed_papers = 0
    processed_images = 0

    for paper in data["papers"]:
        paper_id = paper["paper"]["paper_id"]
        processed_papers += 1

        for chunk in paper["chunks"]:
            if chunk["metadata"].get("contains_image", False):
                # Create a mapping of placeholder to S3 URL
                s3_urls = {}

                for placeholder, image_filename in chunk["metadata"]["images"].items():
                    # Construct the local path to the image
                    # Assuming images are in the same directory as the markdown files
                    image_path = f"/Users/id05309/Documents/agentic-rag/data/{paper_id}/{image_filename}"

                    if os.path.exists(image_path):
                        # Upload to S3 and get URL
                        s3_url = upload_image_to_s3(
                            s3_client, paper_id, image_filename, image_path
                        )
                        if s3_url:
                            s3_urls[placeholder] = s3_url
                            processed_images += 1
                    else:
                        print(f"Warning: Image file not found: {image_path}")

                # Update the chunk metadata with S3 URLs
                chunk["metadata"]["s3_urls"] = s3_urls

    print(f"Processed {processed_papers} papers and {processed_images} images")

    print("Saving updated data...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Updated data saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    process_images()
