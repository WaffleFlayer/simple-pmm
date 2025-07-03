#!/usr/bin/env python3
"""
PMM Installer Script
Automated installer for Simple Plex Media Manager
Designed for easy deployment from GitHub to Windows Surface
"""

import os
import sys
import subprocess
import platform
import shutil
import urllib.request
import json
from pathlib import Path

def check_system_requirements():
    """Check system requirements for Windows Surface"""
    print("Checking system requirements...")
    
    # Check OS
    if platform.system() != 'Windows':
        print("⚠ This installer is optimized for Windows Surface")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 9):
        print("✗ Python 3.9+ required. Please update Python.")
        return False
    
    print(f"✓ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    return True

def check_docker():
    """Check if Docker is available or offer to install"""
    try:
        result = subprocess.run(['docker', '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"✓ Docker found: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Docker not found")
        print("Please install Docker Desktop from: https://www.docker.com/products/docker-desktop/")
        print("After installation, restart this installer.")
        return False

def check_plex_token():
    """Check if Plex token is configured"""
    env_file = Path('.env')
    if env_file.exists():
        with open(env_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if 'PLEX_TOKEN=your_plex_token_here' in content:
                print("⚠ Please configure your Plex token in .env file")
                return False
            elif 'PLEX_TOKEN=' in content and len(content.split('PLEX_TOKEN=')[1].split('\n')[0].strip()) > 0:
                print("✓ Plex token configured")
                return True
    
    print("⚠ .env file not found. Please copy .env.example to .env and configure")
    return False

def create_env_file():
    """Create .env file from example"""
    env_example = Path('.env.example')
    env_file = Path('.env')
    
    if env_example.exists() and not env_file.exists():
        shutil.copy(env_example, env_file)
        print("✓ Created .env file from .env.example")
        print("⚠ Please edit .env file with your Plex server details")
        return True
    
    return False

def install_dependencies():
    """Install Python dependencies with better error handling"""
    try:
        print("Installing Python dependencies...")
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ], capture_output=True, text=True, check=True)
        print("✓ Python dependencies installed")
        return True
    except subprocess.CalledProcessError as e:
        print("✗ Failed to install dependencies")
        print(f"Error: {e.stderr}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = ['config', 'logs', 'temp']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    print("✓ Created necessary directories")

def setup_windows_service():
    """Setup as Windows service (optional)"""
    service_script = Path('install_service.bat')
    if not service_script.exists():
        service_content = f'''@echo off
echo Installing PMM as Windows Service...
sc create "SimplePMM" binPath= "{sys.executable} {Path.cwd() / 'pmm.py'}" start= auto
echo Service installed. Use 'sc start SimplePMM' to start the service.
pause
'''
        with open(service_script, 'w', encoding='utf-8') as f:
            f.write(service_content)
        print("✓ Created Windows service installer (install_service.bat)")

def download_docker_compose():
    """Download docker-compose if not available"""
    try:
        subprocess.run(['docker-compose', '--version'], 
                      capture_output=True, text=True, check=True)
        print("✓ Docker Compose found")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠ Docker Compose not found - using 'docker compose' instead")
        return True

def test_plex_connection():
    """Test connection to Plex server"""
    env_file = Path('.env')
    if not env_file.exists():
        return False
    
    try:
        import requests
        from dotenv import load_dotenv
        
        load_dotenv()
        plex_url = os.getenv('PLEX_URL', 'http://localhost:32400')
        plex_token = os.getenv('PLEX_TOKEN')
        
        if not plex_token or plex_token == 'your_plex_token_here':
            return False
        
        response = requests.get(f"{plex_url}/identity", 
                              params={'X-Plex-Token': plex_token}, 
                              timeout=10)
        if response.status_code == 200:
            print("✓ Plex server connection successful")
            return True
        else:
            print("✗ Failed to connect to Plex server")
            return False
    except Exception as e:
        print(f"✗ Plex connection test failed: {e}")
        return False

def main():
    """Main installer function"""
    print("=" * 50)
    print("Simple PMM Installer for Windows Surface")
    print("=" * 50)
    print()
    
    # System checks
    if not check_system_requirements():
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Check Docker
    docker_ok = check_docker()
    if not docker_ok:
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Create .env file
    create_env_file()
    
    # Install dependencies
    deps_ok = install_dependencies()
    if not deps_ok:
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Check Docker Compose
    download_docker_compose()
    
    # Check Plex token
    token_ok = check_plex_token()
    
    # Test Plex connection if token is configured
    plex_ok = test_plex_connection() if token_ok else False
    
    # Setup Windows service option
    setup_windows_service()
    
    print("\n" + "=" * 50)
    print("Installation Summary:")
    print("=" * 50)
    print(f"System Requirements: ✓")
    print(f"Docker: {'✓' if docker_ok else '✗'}")
    print(f"Dependencies: {'✓' if deps_ok else '✗'}")
    print(f"Configuration: {'✓' if token_ok else '⚠'}")
    print(f"Plex Connection: {'✓' if plex_ok else '⚠'}")
    
    if all([docker_ok, deps_ok, token_ok, plex_ok]):
        print("\n🎉 Installation complete! PMM is ready to use.")
        print("\nYou can now run PMM in several ways:")
        print("1. Direct execution: python pmm.py")
        print("2. Docker: docker-compose up -d")
        print("3. Windows Service: Run install_service.bat as administrator")
        
        print("\nWould you like to start PMM now? (y/n): ", end="")
        if input().lower().startswith('y'):
            print("\nStarting PMM...")
            try:
                subprocess.run([sys.executable, 'pmm.py'], check=True)
            except KeyboardInterrupt:
                print("\nPMM stopped.")
    else:
        print("\n⚠ Installation incomplete. Please address the issues above.")
        if not token_ok:
            print("\nTo get your Plex token:")
            print("1. Go to https://app.plex.tv/desktop/")
            print("2. Open browser developer tools (F12)")
            print("3. Go to Network tab and refresh the page")
            print("4. Look for a request containing X-Plex-Token in headers")
            print("5. Edit the .env file with your token")
            print("6. Run this installer again")
    
    print("\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    main()
