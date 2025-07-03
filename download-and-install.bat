@echo off
cls
echo ================================================
echo Simple PMM - GitHub Installer
echo ================================================
echo.
echo This script will download and install Simple PMM
echo from GitHub to your Windows Surface.
echo.

REM Check if git is available
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git not found. Downloading with PowerShell...
    echo.
    
    REM Create temp directory
    if not exist "%TEMP%\simple-pmm" mkdir "%TEMP%\simple-pmm"
    
    REM Download with PowerShell
    powershell -Command "& {Invoke-WebRequest -Uri 'https://github.com/waffleflayer/simple-pmm/archive/refs/heads/main.zip' -OutFile '%TEMP%\simple-pmm\pmm.zip'}"
    
    REM Extract
    powershell -Command "& {Expand-Archive -Path '%TEMP%\simple-pmm\pmm.zip' -DestinationPath '%TEMP%\simple-pmm\' -Force}"
    
    REM Copy to current directory
    xcopy "%TEMP%\simple-pmm\simple-pmm-main\*" "." /E /I /Y
    
    REM Cleanup
    rmdir /S /Q "%TEMP%\simple-pmm"
    
    echo Download complete!
) else (
    echo Cloning with Git...
    git clone https://github.com/waffleflayer/simple-pmm.git .
)

echo.
echo Starting installation...
echo.

REM Run the installer
if exist "install.bat" (
    call install.bat
) else (
    echo ERROR: install.bat not found after download
    echo Please check the repository URL and try again
    pause
    exit /b 1
)

echo.
echo GitHub installation complete!
pause
