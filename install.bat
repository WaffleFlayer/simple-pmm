@echo off
cls
echo ================================================
echo Simple PMM Installer for Windows Surface
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Run the Python installer
echo Running PMM installer...
echo.
python setup.py

echo.
echo Installation complete!
pause
