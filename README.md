# Table Joiner & Chunker CLI

This project is a command-line interface (CLI) application designed to combine and split CSV files. It processes CSV files from a specified directory, combines them into a single DataFrame, and then splits this DataFrame into chunks of a specified number of rows, saving each chunk as a separate CSV file.

## Features

- Combine multiple CSV files into a single DataFrame.
- Split the combined DataFrame into chunks of a specified number of rows.
- Option to combine all data into a single CSV file.
- Outputs the processed files into a designated output folder.

## Requirements

- Python 3.x (WITH PATH)
- `pandas` library

## Setup

1. **Install Python Dependencies**

   Run the `install.bat` file to install the required Python dependencies:

   ```bash
   install.bat
   ```

   This will install the dependencies listed in `requirements.txt`.

## Usage

### Running the Script

To run the script, execute the `run.bat` file. This batch file will prompt you for the main path where the CSV files are stored and the number of rows per chunk. If you do not provide input, it will use default values specified in `config.json`.

```bash
run.bat
```

### Adjusting Default Settings

The default settings for the script are stored in `config.json`. You can easily adjust these settings by editing the file:

- `default_main_path`: The default path where the CSV files are stored.
- `default_rows`: The default number of rows per chunk or "all" to combine into one file.

Example `config.json`:

```json
{
  "default_main_path": "working folder",
  "default_rows": "1499"
}
```

### Example Commands

1. **Split CSV files into chunks of 1999 rows:**

   ```bash
   python Super_joiner.py --main_path "C:/path/to/csv/files" --rows 1999
   ```

2. **Combine all CSV files into a single file:**

   ```bash
   python Super_joiner.py --main_path "C:/path/to/csv/files" --rows all
   ```

## Output

The processed CSV files will be saved in a folder named `Join Output` within the specified main path.

## Notes

- Ensure that the specified main path contains the CSV files you wish to process.
- The `Join Output` folder will be created automatically if it does not exist.

## License

This project is for internal wfm use only.
