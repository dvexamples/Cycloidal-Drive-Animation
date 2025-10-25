@echo off
REM Run demo scripts with proper virtual environment activation

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Running demo_1.py...
python demo_1.py

pause