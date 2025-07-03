#!/usr/bin/env python3
"""
PMM Health Check Script
Verify that PMM is configured and running correctly
"""

import sys
import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import requests
import yaml

def check_files():
    """Check if required files exist"""
    required_files = [
        'pmm.py',
        'config/pmm_config.yml',
        '.env',
        'requirements.txt'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"✗ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✓ All required files present")
    return True

def check_configuration():
    """Check configuration validity"""
    try:
        with open('config/pmm_config.yml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        if 'libraries' not in config:
            print("✗ No libraries configured")
            return False
        
        print(f"✓ Configuration valid ({len(config['libraries'])} libraries configured)")
        return True
    except Exception as e:
        print(f"✗ Configuration error: {e}")
        return False

def check_environment():
    """Check environment variables"""
    load_dotenv()
    
    plex_url = os.getenv('PLEX_URL')
    plex_token = os.getenv('PLEX_TOKEN')
    
    if not plex_url:
        print("✗ PLEX_URL not configured")
        return False
    
    if not plex_token or plex_token == 'your_plex_token_here':
        print("✗ PLEX_TOKEN not configured")
        return False
    
    print("✓ Environment variables configured")
    return True

def check_plex_connection():
    """Test Plex server connection"""
    load_dotenv()
    
    try:
        plex_url = os.getenv('PLEX_URL')
        plex_token = os.getenv('PLEX_TOKEN')
        
        response = requests.get(
            f"{plex_url}/identity",
            params={'X-Plex-Token': plex_token},
            timeout=10
        )
        
        if response.status_code == 200:
            print("✓ Plex server connection successful")
            return True
        else:
            print(f"✗ Plex server returned status {response.status_code}")
            return False
    
    except requests.exceptions.RequestException as e:
        print(f"✗ Cannot connect to Plex server: {e}")
        return False

def check_docker():
    """Check Docker availability"""
    try:
        result = subprocess.run(
            ['docker', '--version'],
            capture_output=True, text=True, check=True
        )
        print(f"✓ Docker available: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Docker not available")
        return False

def check_dependencies():
    """Check Python dependencies"""
    try:
        import plexapi
        import docker
        import schedule
        print("✓ All Python dependencies available")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        return False

def main():
    """Run all health checks"""
    print("PMM Health Check")
    print("=" * 50)
    
    checks = [
        ("Files", check_files),
        ("Configuration", check_configuration),
        ("Environment", check_environment),
        ("Dependencies", check_dependencies),
        ("Docker", check_docker),
        ("Plex Connection", check_plex_connection),
    ]
    
    results = {}
    for name, check_func in checks:
        print(f"\nChecking {name}...")
        results[name] = check_func()
    
    print("\n" + "=" * 50)
    print("Health Check Summary:")
    print("=" * 50)
    
    all_passed = True
    for name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{name}: {status}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All checks passed! PMM is ready to run.")
        return 0
    else:
        print("\n⚠ Some checks failed. Please address the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
