# Run demo scripts with proper virtual environment activation

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

Write-Host "Running demo_1.py..." -ForegroundColor Green
python demo_1.py