@echo off
echo Welcome to the Table Joiner & Chunker CLI
echo Developed by: Ryan Satterfield

:: Read default values from config.json
for /f "tokens=2 delims=:, " %%a in ('findstr "default_main_path" config.json') do set default_main_path=%%~a
for /f "tokens=2 delims=:, " %%a in ('findstr "default_rows" config.json') do set default_rows=%%~a

:: Remove quotes from the values
set default_main_path=%default_main_path:"=%
set default_rows=%default_rows:"=%

:: Prompt user for input with default values
set /p main_path="Enter the main path where the CSV files are stored (default: %default_main_path%): "
if "%main_path%"=="" set main_path=%default_main_path%

set /p rows="Enter the number of rows per chunk (or 'all' to combine into one file) (default: %default_rows%): "
if "%rows%"=="" set rows=%default_rows%

echo Running the Python script...
python Super_joiner.py --main_path "%main_path%" --rows "%rows%"
echo Script execution complete.
