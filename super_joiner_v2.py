import os
import pandas as pd
import logging
from tqdm import tqdm  # Progress bar
from concurrent.futures import ThreadPoolExecutor
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_csv_files(root_dir, exclude_folder="Join Output"):
    """Finds all CSV files in a directory and its subdirectories, excluding specified folders."""
    csv_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d != exclude_folder]
        for filename in files:
            if filename.endswith(".csv"):
                csv_files.append(os.path.join(root, filename))
    return csv_files

def load_csv(file_path):
    """Loads a CSV file and returns a DataFrame without altering column capitalization."""
    try:
        return pd.read_csv(file_path, na_values=[""], keep_default_na=False)
    except Exception as e:
        logging.error(f"Failed to read {file_path}: {e}")
        return None

def save_chunks(df, output_folder, chunk_size):
    """Splits and saves a DataFrame into chunks of specified size."""
    num_chunks = (len(df) // chunk_size) + 1
    os.makedirs(output_folder, exist_ok=True)
    for i in range(num_chunks):
        chunk_df = df.iloc[i * chunk_size: (i + 1) * chunk_size]
        output_file = os.path.join(output_folder, f'Output_items_{i + 1}.csv')
        chunk_df.to_csv(output_file, index=False)
        logging.info(f"Saved chunk {i + 1} to {output_file}")

def main(main_path, chunk_size, output_folder):
    csv_files = find_csv_files(main_path)
    if not csv_files:
        logging.warning("No CSV files found.")
        return

    logging.info(f"Found {len(csv_files)} CSV files. Starting to combine...")

    combined_data = []
    with ThreadPoolExecutor() as executor:
        for df in tqdm(executor.map(load_csv, csv_files), total=len(csv_files)):
            if df is not None:
                combined_data.append(df)

    if combined_data:
        combined_df = pd.concat(combined_data, ignore_index=True)
        logging.info(f"Combined DataFrame has {len(combined_df)} rows.")
        save_chunks(combined_df, output_folder, chunk_size)
    else:
        logging.warning("No valid data to combine.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine and split CSV files.")
    parser.add_argument("--main_path", type=str, default=os.path.dirname(os.path.abspath(__file__)),
                        help="Directory to search for CSV files. Defaults to current script location.")
    parser.add_argument("--chunk_size", type=int, default=1999, help="Number of rows per output file. Defaults to 1999.")
    parser.add_argument("--output_folder", type=str, default="Join Output", help="Folder to save output files. Defaults to 'Join Output'.")

    args = parser.parse_args()

    main(args.main_path, args.chunk_size, args.output_folder)
