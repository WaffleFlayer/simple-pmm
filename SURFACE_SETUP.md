# Surface Pre-Installation Checklist

## Required Information for Your Surface

### ✅ **What You'll Need**

1. **Plex Token** (Primary requirement)
   - Get from: https://app.plex.tv/desktop/
   - Method: F12 → Network tab → Find `X-Plex-Token` in any request
   - Format: Long alphanumeric string (e.g., `aBc123XyZ456...`)

2. **Plex Server URL** (Usually automatic)
   - Default: `http://localhost:32400` (if Plex is on your Surface)
   - Network: `http://[surface-ip]:32400` (if accessing remotely)
   - To find your Surface IP: `ipconfig` in Command Prompt

### 🔍 **Pre-Installation Verification**

#### **System Requirements** ✓
- Windows 10/11 Surface ✓
- Python 3.9+ (installer will check)
- Docker Desktop (installer will check)
- 500MB free disk space

#### **Network Access** ✓
- Internet connection for downloads
- Access to Plex server (local or network)

#### **File Paths That Will Be Created**
The installer will create these in your chosen directory:
```
📁 Your-PMM-Folder/
├── 📄 .env                    # Your secrets (Plex token)
├── 📁 config/                 # Configuration files
├── 📁 logs/                   # Application logs  
├── 📁 temp/                   # Temporary files
└── 📄 install_service.bat     # Windows service installer
```

### 🎯 **Recommended Setup Location**

**Option 1: User Documents (Recommended)**
```
C:\Users\[YourName]\Documents\PMM\
```

**Option 2: Dedicated Folder**
```
C:\PMM\
```

**Option 3: Desktop (Easy Access)**
```
C:\Users\[YourName]\Desktop\PMM\
```

### ⚙️ **Configuration You'll Customize**

#### **Required (in .env file):**
- `PLEX_TOKEN=your_actual_token_here`
- `PLEX_URL=http://localhost:32400` (adjust if needed)

#### **Optional (in .env file):**
- `TMDB_API_KEY=` (for enhanced metadata - get from themoviedb.org)
- `AUTO_RUN_ENABLED=true` (run on schedule)
- `RUN_SCHEDULE=06:00` (when to run daily)
- `PMM_LOG_LEVEL=INFO` (logging detail)

#### **Library Settings (in config/pmm_config.yml):**
- Which libraries to manage (Movies, TV Shows, Music)
- Maintenance schedule
- Cleanup preferences

### 🚀 **Installation Process Overview**

1. **Download**: Get files from GitHub
2. **Run installer**: Double-click `install.bat`
3. **Configure**: Edit `.env` with your Plex token
4. **Test**: Run health check
5. **Start**: Launch PMM

### 🔒 **Security Notes**

- **Plex Token**: Keep this private - it gives full access to your Plex server
- **Firewall**: Windows may ask to allow Python/Docker network access
- **Antivirus**: May scan downloaded files (normal)

### 📝 **What You Don't Need to Worry About**

✅ **Python paths** - Installer detects automatically  
✅ **Docker configuration** - Handled by installer  
✅ **Port conflicts** - PMM uses standard Plex ports  
✅ **File permissions** - Installer sets these up  
✅ **Dependencies** - All installed automatically  

### 🎯 **Ready to Install?**

If you have:
- [x] Plex server running on your Surface
- [x] Plex token ready to copy
- [x] Chosen installation location
- [x] Internet connection

Then you're ready to run the installer! 🚀

### 🆘 **Quick Troubleshooting**

| Issue | Quick Fix |
|-------|-----------|
| "Python not found" | Install from python.org, check "Add to PATH" |
| "Docker not found" | Install Docker Desktop, restart Surface |
| "Plex connection failed" | Verify Plex is running, check token |
| "Permission denied" | Run Command Prompt as Administrator |

---
**Next Step**: Download and run `install.bat` in your chosen folder!
