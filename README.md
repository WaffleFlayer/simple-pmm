# Simple Plex Media Manager (PMM) for Windows Surface

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A lightweight, automated Plex Media Manager designed specifically for Windows Surface devices. Manage your Plex libraries with scheduled maintenance, automated scanning, and Docker support.

## ✨ Features

- **🔄 Automated Library Management**: Scan and update Plex libraries automatically
- **⏰ Scheduled Maintenance**: Run routine tasks on your preferred schedule
- **🐳 Docker Ready**: Containerized for easy deployment and isolation
- **📊 Comprehensive Logging**: Monitor all activities with detailed logs
- **⚙️ Simple Configuration**: YAML-based settings for easy customization
- **🖥️ Windows Service**: Optional installation as a Windows background service
- **🚀 One-Click Installer**: Automated setup script for quick deployment

## 🚀 Quick Installation

### Method 1: Automated Installer (Recommended)

1. **Download** this repository:
   ```powershell
   git clone https://github.com/waffleflayer/simple-pmm.git
   cd simple-pmm
   ```

2. **Run the installer**:
   ```powershell
   # Double-click install.bat or run in PowerShell:
   .\install.bat
   ```

3. **Configure your Plex settings** in the created `.env` file

4. **Start PMM**:
   ```powershell
   python pmm.py
   ```

### Method 2: Manual Setup

1. **Prerequisites**:
   - Python 3.9+
   - Docker Desktop
   - Plex Media Server

2. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```powershell
   copy .env.example .env
   # Edit .env with your Plex details
   ```

## 📋 Prerequisites

- **Windows 10/11** (optimized for Surface devices)
- **Python 3.9+** - [Download here](https://www.python.org/downloads/)
- **Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop/)
- **Plex Media Server** - Running and accessible

## ⚙️ Configuration

### Getting Your Plex Token

1. Go to [Plex Web App](https://app.plex.tv/desktop/)
2. Open browser developer tools (F12)
3. Go to Network tab and refresh the page
4. Look for a request containing `X-Plex-Token` in headers
5. Copy the token value

### Environment Variables

Edit the `.env` file created during installation:

```env
# Plex Server Configuration
PLEX_URL=http://localhost:32400
PLEX_TOKEN=your_actual_plex_token_here

# Optional: TMDb API for enhanced metadata
TMDB_API_KEY=your_tmdb_api_key

# Scheduling
AUTO_RUN_ENABLED=true
RUN_SCHEDULE=06:00
PMM_LOG_LEVEL=INFO
```

### Library Configuration

Customize `config/pmm_config.yml`:

```yaml
libraries:
  Movies:
    type: movie
    auto_scan: true
    cleanup_enabled: true
  
  TV Shows:
    type: show
    auto_scan: true
    cleanup_enabled: true

maintenance:
  enabled: true
  schedule_time: "06:00"
  tasks:
    - scan_libraries
    - cleanup_temp_files
    - optimize_database
```

## 🚀 Running PMM

### Option 1: Direct Python Execution
```powershell
python pmm.py
```

### Option 2: Docker (Recommended)
```powershell
# Build and run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f pmm
```

### Option 3: Windows Service
```powershell
# Run as administrator
.\install_service.bat

# Start the service
sc start SimplePMM
```

## 📊 Monitoring

### View Logs
```powershell
# Direct execution logs
Get-Content -Wait pmm.log

# Docker logs
docker-compose logs -f pmm
```

### Health Check
The installer creates a health check script that verifies:
- ✅ Plex server connectivity
- ✅ Library accessibility
- ✅ Docker status
- ✅ Scheduled tasks

## 📁 Project Structure

```
PMM/
├── 📄 install.bat              # Windows installer
├── 🐍 setup.py                # Python setup script
├── 🐍 pmm.py                  # Main application
├── 📋 requirements.txt        # Python dependencies
├── 🐳 Dockerfile             # Docker container config
├── 🐳 docker-compose.yml     # Docker Compose setup
├── ⚙️ .env.example           # Environment template
├── 📁 config/
│   └── 📄 pmm_config.yml     # Main configuration
├── 📁 logs/                  # Application logs
└── 📁 .github/
    └── 📄 copilot-instructions.md
```

## 🔧 Advanced Usage

### Custom Maintenance Tasks
Add custom tasks to `pmm.py`:

```python
def custom_cleanup_task(self):
    """Your custom maintenance task"""
    logger.info("Running custom cleanup")
    # Your code here
```

### Integration with Other Tools
PMM can be extended to work with:
- **Sonarr/Radarr**: Media acquisition
- **Tautulli**: Plex monitoring
- **Overseerr**: Media requests

## 🛠️ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| ❌ Cannot connect to Plex | Verify `PLEX_URL` and `PLEX_TOKEN` in `.env` |
| ❌ Docker not found | Install Docker Desktop and restart |
| ❌ Permission denied | Run PowerShell as Administrator |
| ❌ Python not found | Add Python to Windows PATH |

### Getting Support

1. **Check the logs** first - they contain detailed error information
2. **Verify configuration** - ensure `.env` and `config/pmm_config.yml` are correct
3. **Test manually** - run `python setup.py` to validate setup

## 🎯 Roadmap

- [ ] Web dashboard for monitoring
- [ ] Mobile notifications
- [ ] Integration with popular media tools
- [ ] Automated updates
- [ ] Performance metrics

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## ⭐ Support

If this project helps you manage your Plex server, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting features
- 🤝 Contributing code

---

**Made with ❤️ for Plex enthusiasts running on Windows Surface devices**
