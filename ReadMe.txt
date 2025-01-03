Super Joiner CSV Combiner

super_joiner_v2.py is a Python script that recursively searches for all CSV files within the directory it’s placed in, combines them into a single DataFrame, and splits the result into multiple files with up to 1999 rows each. The included batch file, run_super_joiner_v2.bat, automates the script's execution, installs any required dependencies, and allows the user to use default settings or specify custom arguments.

Table of Contents
Requirements
Installation
Usage
File Structure
Script Functionality
Troubleshooting
1. Requirements
Python 3.x: Ensure Python is installed and added to your system PATH.
Pandas and tqdm: These Python packages are required for data manipulation and progress tracking. The batch file will automatically install these if they aren’t already installed.
2. Installation
Download or Copy the following files into the directory where your CSV files are stored:
super_joiner_v2.py – the main Python script.
run_super_joiner_v2.bat – the batch file to execute the script.
Place Both Files in the folder containing the CSV files you wish to combine.
3. Usage
Run the Batch File: Execute the script by double-clicking run_super_joiner_v2.bat.

The batch file will check for Python and install pandas and tqdm if necessary.

Prompt for Arguments:

The batch file will ask if you want to use default arguments or specify custom values.
Default Arguments:
main_path: The directory where the script is located.
chunk_size: 1999 rows per output file.
output_folder: Join Output (a subfolder where output files are saved).
Custom Arguments: If you choose to specify custom values, the batch file will prompt you to enter:
main_path: Path to the folder containing CSV files.
chunk_size: Number of rows per output file.
output_folder: Name of the folder where output files will be saved.
Output:

The combined CSV output files are saved in a subfolder called Join Output (or the custom folder specified), within the main directory.
Each output file is named Output_items_X.csv, where X is the chunk number.
Example Folder Structure:

markdown
Copy code
- ProjectFolder/
    - super_joiner_v2.py
    - run_super_joiner_v2.bat
    - CSV_Folder/
        - file1.csv
        - file2.csv
        - Subfolder/
            - file3.csv
Result After Running:

All CSV files will be combined and split into chunks, saved in Join Output within ProjectFolder as Output_items_1.csv, Output_items_2.csv, etc.
4. File Structure After Running
After running the batch file, the folder should look like this:

markdown
Copy code
- ProjectFolder/
    - super_joiner_v2.py
    - run_super_joiner_v2.bat
    - CSV_Folder/
        - file1.csv
        - file2.csv
        - Subfolder/
            - file3.csv
    - Join Output/
        - Output_items_1.csv
        - Output_items_2.csv
        ...
5. Script Functionality
Recursive CSV File Search:

The script searches all nested folders for files ending in .csv, ignoring any previously created Join Output folders.
Data Combination and Splitting:

Combines all CSV files into a single DataFrame.
Splits the DataFrame into chunks of up to 1999 rows each, saving each chunk as a separate CSV file.
Error Handling:

Missing CSV files: If no CSV files are found, the script will display a message and exit.
File reading errors: If a CSV file fails to load, an error message is shown, and other files continue processing.
6. Troubleshooting
Common Issues:

Python Not Installed: Ensure Python 3.x is installed and added to your system PATH.
Permission Errors: Run the batch file as an administrator if you encounter permission issues.
Package Installation Errors: If the batch file cannot install pandas or tqdm, try manually installing them:
bash
Copy code
pip install pandas tqdm