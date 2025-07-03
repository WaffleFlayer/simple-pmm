# Ready for Your Surface! 🚀

## What You Need Before Installing

### ✅ **Only 1 Required Item:**
- **Plex Token** - The only thing you need to get manually

### 🎯 **How to Get Your Plex Token:**
1. Go to https://app.plex.tv/desktop/
2. Open browser developer tools (F12)
3. Click the **Network** tab
4. Refresh the page
5. Look for any request and find `X-Plex-Token` in the headers
6. Copy that token value (long string like `xyz123abc456...`)

## ✅ **Everything Else is Automatic**

The installer will handle:
- ✅ Python version detection
- ✅ Docker Desktop verification  
- ✅ Dependency installation
- ✅ Directory creation
- ✅ Configuration file setup
- ✅ Windows service setup (optional)
- ✅ All file paths and permissions

## 📁 **File Paths (All Created Automatically)**

When you run the installer, it will create:
```
Your-Chosen-Folder/
├── .env                    # You'll paste your Plex token here
├── config/                 # Auto-generated
├── logs/                   # Auto-generated  
├── temp/                   # Auto-generated
└── (all other files)       # Downloaded from GitHub
```

## 🎯 **Installation Steps for Your Surface**

### **Method 1: Quick Download & Install**
1. Download: `download-and-install.bat` from GitHub
2. Run it in your desired folder
3. It downloads everything and installs automatically
4. Edit `.env` with your Plex token
5. Done! ✅

### **Method 2: Manual Download**
1. Download the full project from: https://github.com/waffleflayer/simple-pmm
2. Extract to your desired location
3. Double-click `install.bat`
4. Edit `.env` with your Plex token
5. Done! ✅

## ⚙️ **Configuration (.env file)**

After installation, you'll edit one file (`.env`) with:

```env
# Required - Your Plex token
PLEX_TOKEN=your_actual_token_here

# Usually correct as-is (if Plex is on your Surface)
PLEX_URL=http://localhost:32400

# Optional settings (defaults are fine)
AUTO_RUN_ENABLED=true
RUN_SCHEDULE=06:00
PMM_LOG_LEVEL=INFO
```

## 🏃‍♂️ **Running on Your Surface**

After setup, you can run PMM 3 ways:

1. **Direct**: `python pmm.py`
2. **Docker**: `docker-compose up -d`  
3. **Windows Service**: Run `install_service.bat` as admin

## 🔍 **Health Check**

Run `python health_check.py` anytime to verify everything is working.

## 🎯 **That's It!**

No complex configuration needed. Just:
1. Get your Plex token
2. Run the installer  
3. Paste the token
4. Start PMM

The installer handles all the technical details for you! 🎉

---
**GitHub Repository**: https://github.com/waffleflayer/simple-pmm
