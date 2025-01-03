import os
import pandas as pd
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Combine and split CSV files.')
    parser.add_argument('--main_path', type=str, required=True, help='The main path where the CSV files are stored.')
    parser.add_argument('--rows', type=str, default='1499', help='Number of rows per chunk or "all" to combine into one file. (default: 1499)')
    args = parser.parse_args()

    # Determine chunk size
    if args.rows.lower() == 'all':
        chunk_size = None
    else:
        try:
            chunk_size = int(args.rows)
        except ValueError:
            print("Invalid input for rows. Please enter a number or 'all'.")
            return

    # Define the output folder path
    output_folder = os.path.join(args.main_path, 'Join Output')

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create an empty list to store each CSV file's data
    combined_data = []

    # Recursively find and load all CSV files in the directory, ignoring "Join Output" folder
    for root, dirs, files in os.walk(args.main_path):
        # Remove 'Join Output' folder from the list of directories to traverse
        dirs[:] = [d for d in dirs if d != "Join Output"]

        for filename in files:
            if filename.endswith(".csv"):
                file_path = os.path.join(root, filename)
                print(f"Processing file: {file_path}")
                
                # Read the CSV file into a pandas DataFrame
                # Specify that only empty strings should be treated as NaN values
                df = pd.read_csv(file_path, na_values=[""], keep_default_na=False)

                # Append the DataFrame to the list
                combined_data.append(df)

    # Combine all the DataFrames into one long DataFrame
    combined_df = pd.concat(combined_data, ignore_index=True)

    if chunk_size is None:
        # Save the entire DataFrame to a single CSV file
        combined_df.to_csv(os.path.join(output_folder, 'Output_combined.csv'), index=False)
        print("All CSV files have been successfully combined into one file.")
    else:
        # Split the combined DataFrame into chunks
        num_chunks = (len(combined_df) // chunk_size) + 1  # Calculate how many chunks are needed

        # Loop through each chunk and save to a separate CSV file in 'Join Output' folder
        for i in range(num_chunks):
            start_row = i * chunk_size
            end_row = start_row + chunk_size
            chunk_df = combined_df.iloc[start_row:end_row]
            
            # Save the chunk to a new CSV file with a numbered extension
            chunk_df.to_csv(os.path.join(output_folder, f'Output_items_{i+1}.csv'), index=False)

        print(f"All CSV files have been successfully combined and split into {num_chunks} files.")

if __name__ == "__main__":
    main()
