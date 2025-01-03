@echo off
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python to continue.
    pause
    exit /b
)

echo Installing required Python packages...
pip install pandas tqdm >nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to install required packages. Please check your Python and pip installation.
    pause
    exit /b
)

set "use_defaults=Y"
set /p use_defaults="Do you want to use the default arguments? (Y/N): "

if /i "%use_defaults%"=="N" (
    echo.
    echo Please enter custom values for each argument. Press Enter to use the default shown in brackets.
    
    set "main_path=%~dp0"  :: Default to the folder where the script is located
    set /p main_path="Enter main path to search for CSV files [%main_path%]: "
    if "%main_path%"=="" set "main_path=%~dp0"

    set "chunk_size=1999"
    set /p chunk_size="Enter chunk size (number of rows per file) [%chunk_size%]: "
    if "%chunk_size%"=="" set "chunk_size=1999"

    set "output_folder=Join Output"
    set /p output_folder="Enter output folder name [%output_folder%]: "
    if "%output_folder%"=="" set "output_folder=Join Output"

    echo Running the script with custom arguments...
    python super_joiner_v2.py --main_path "%main_path%" --chunk_size %chunk_size% --output_folder "%output_folder%"
) else (
    echo Running the script with default arguments...
    python super_joiner_v2.py
)

echo Script finished.
pause
