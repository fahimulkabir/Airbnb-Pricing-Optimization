import os
import requests
import gzip
import shutil

def download_and_extract(url, output_folder):
    filename = url.split('/')[-1]
    gz_path = os.path.join(output_folder, filename)
    csv_path = gz_path.replace('.gz', '')

    # Download file
    print(f"Downloading {filename}...")
    response = requests.get(url, stream=True)
    with open(gz_path, 'wb') as f:
        shutil.copyfileobj(response.raw, f)

    # Extract file
    print(f"Extracting {filename}...")
    with gzip.open(gz_path, 'rb') as f_in:
        with open(csv_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Remove .gz
    os.remove(gz_path)
    print(f"Saved extracted file to {csv_path}")

# Example for NYC
os.makedirs("/Users/fahimulkabir/Github/Airbnb-Pricing-Optimization/data/raw/New York/New York City", exist_ok=True)
urls = [
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-05-01/data/listings.csv.gz",
    "https://data.insideairbnb.com/united-states/ny/new-york-city/2025-05-01/data/calendar.csv.gz"
]

for url in urls:
    download_and_extract(url, "/Users/fahimulkabir/Github/Airbnb-Pricing-Optimization/data/raw/New York/New York City")
