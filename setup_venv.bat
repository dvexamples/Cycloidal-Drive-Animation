@echo off
REM Cycloidal Drive Animation - Virtual Environment Setup Script (Batch)
REM This script creates a virtual environment and installs required dependencies

echo Setting up virtual environment for Cycloidal Drive Animation...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Found Python installed

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo Virtual environment setup complete!
    echo.
    echo To activate the virtual environment in the future, run:
    echo   venv\Scripts\activate.bat
    echo.
    echo To deactivate the virtual environment, run:
    echo   deactivate
    echo.
    echo You can now run the demo scripts:
    echo   python demo_1.py
    echo   python demo_UI_ver1.1.py
    echo.
) else (
    echo Error: Failed to install requirements
    pause
    exit /b 1
)

pause