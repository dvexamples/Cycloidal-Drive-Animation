# Cycloidal Drive Animation - Virtual Environment Setup Script
# This script creates a virtual environment and installs required dependencies

Write-Host "Setting up virtual environment for Cycloidal Drive Animation..." -ForegroundColor Green

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Cyan
} catch {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to create virtual environment" -ForegroundColor Red
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to activate virtual environment" -ForegroundColor Red
    exit 1
}

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install requirements
Write-Host "Installing requirements..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "" -ForegroundColor Green
    Write-Host "Virtual environment setup complete!" -ForegroundColor Green
    Write-Host "" -ForegroundColor Green
    Write-Host "To activate the virtual environment in the future, run:" -ForegroundColor Cyan
    Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
    Write-Host "" -ForegroundColor Green
    Write-Host "To deactivate the virtual environment, run:" -ForegroundColor Cyan
    Write-Host "  deactivate" -ForegroundColor White
    Write-Host "" -ForegroundColor Green
    Write-Host "You can now run the demo scripts:" -ForegroundColor Cyan
    Write-Host "  python demo_1.py" -ForegroundColor White
    Write-Host "  python demo_UI_ver1.1.py" -ForegroundColor White
} else {
    Write-Host "Error: Failed to install requirements" -ForegroundColor Red
    exit 1
}