# Thinx - Quick Start Guide

**🎯 Goal:** Get Thinx running in under 10 minutes

**👋 New to this?** This guide assumes zero technical knowledge. We'll walk you through every step.

---

## What You'll Do

By the end of this guide, you'll:
- ✅ Start Thinx on your computer
- ✅ Create an account and log in
- ✅ Connect to a research database
- ✅ Be ready to upload and explore data

**Time needed:** ~10 minutes

---

## Prerequisites

### ✅ Checklist

- [ ] **Docker Desktop** installed and running (look for whale icon 🐳 in taskbar)
- [ ] **2GB free disk space**
- [ ] **Web browser** (Chrome, Firefox, Edge, or Safari)

**Don't have Docker?** 
1. Download from [docker.com/get-started](https://docker.com/get-started)
2. Install and restart your computer
3. Open Docker Desktop and wait for "Running" status

---

## Step 1: Open Terminal (1 minute)

**Windows:**
1. Press `Windows Key + R`
2. Type `powershell` and press Enter

**Mac:**
1. Press `Command + Space`
2. Type `terminal` and press Enter

**💡 What's a terminal?** A window where you type commands to your computer.

## Step 2: Navigate to Thinx Folder (1 minute)

In the terminal, type (replace with your actual path):
```bash
cd "C:\Users\YourName\Documents\DataScienceInPractice"
```

**💡 Tip:** Drag the Thinx folder into the terminal window to auto-fill the path!

---

## Step 3: Start Thinx (3-5 minutes)

**Copy and paste this command:**
```bash
docker-compose --profile full up --build
```

**Press Enter** and wait. You'll see lots of text scrolling - this is normal!

**What you're starting:**
- 🎨 **Frontend** - The web interface
- ⚙️ **Backend** - The API server  
- 💾 **Database** - AllegroGraph for data storage
- 🤖 **AI** - Smart mapping features

**First time:** 3-7 minutes (downloading images)  
**After that:** 30-60 seconds

**When ready, you'll see:**
```
frontend_1  | ready in 1234 ms
backend_1   | Running on http://0.0.0.0:5000
```

**⚠️ Don't close this terminal window!** Leave it running in the background.

**Alternative: Faster startup without AI**
```bash
docker-compose --profile no-ai up --build

---

## Step 4: Open Thinx in Browser (1 minute)

Open your web browser and go to: **http://localhost**

**🎉 Success!** You should see the Thinx login page with a purple gradient header.

**If you see an error:** Wait 30 seconds and refresh - services may still be starting.

---

## Step 5: Create Your Account (2 minutes)

### First Time User

1. Click "**Register**" (below the login form)
2. Fill in:
   - **Username:** e.g., "marie_research"
   - **Password:** At least 6 characters
3. Click "**Register**"
4. You'll be logged in automatically

### Returning User

Just enter your username and password and click "**Login**"

**💡 Tip:** Bookmark `http://localhost` for easy access!

---

## Step 6: Connect to Database (3 minutes)

### Setup AllegroGraph Repository

1. Open **http://localhost:10035** in a new tab
2. Login with: `admin` / `admin123`
3. Click "**Create Repository**"
4. Repository Name: `humantrafficking`
5. Click "**Create**"

### Connect Thinx to Database

1. Go back to **http://localhost**
2. Click "**➕ Add AllegroGraph Connection**"
3. Fill in:
   - **Name:** `My Research Database`
   - **Host:** `allegrograph`
   - **Port:** `10035`
   - **Repository:** `humantrafficking`
   - **Username:** `admin`
   - **Password:** `admin123`
4. Click "**Save**"

**🎉 You're connected!** You should see a green "✓ Active" indicator.

---

## Step 7: Try It Out! (5 minutes)

### Option A: Upload Sample Data

1. Go to `Mock data/` folder in your Thinx directory
2. Find `Interview_mock_comprehensive.csv`
3. Upload through "**Step 2: Upload Data**"
4. Follow the AI mapping workflow

### Option B: Explore the Interface

Click the "**❓ Help**" button to see:
- 🔌 Database Connection tips
- 📊 Data Workflow guide
- 🤖 AI Smart Mapper overview
- 📈 Data Viewer features

---

## Stopping Thinx

**When done for the day:**

1. Go to the terminal window
2. Press `Ctrl+C`
3. Wait for services to stop (10 seconds)
4. Type: `docker-compose down`

**Your data is safe!** Next time, just run: `docker-compose --profile full up`

---

## Common Problems & Solutions

### ❌ "Port already in use"

Another program is using port 80. Stop XAMPP, IIS, or Apache and try again.

**Windows - find what's using the port:**
```bash
netstat -ano | findstr :80
taskkill /PID [number] /F
```

### ❌ "Cannot connect to Docker daemon"

Docker isn't running. Open Docker Desktop and wait for it to start.

### ❌ "502 Bad Gateway"

Backend is still starting. Wait 30 seconds and refresh your browser.

### ❌ "No data found"

Your database is empty. Upload sample data from `Mock data/` folder.

### 🔄 Start fresh / Reset everything

```bash
docker-compose down -v    # ⚠️ Deletes all data!
docker-compose --profile full up --build
```

**More help:** See [FAQ.md](FAQ.md) or [README.md#troubleshooting](README.md#troubleshooting)

---

## What's Next?

### 📚 Learn More

| I want to... | Read this |
|-------------|-----------|
| Learn all features | [USER_GUIDE.md](USER_GUIDE.md) |
| Deploy for a team | [ADMIN_GUIDE.md](ADMIN_GUIDE.md) |
| Quick answers | [FAQ.md](FAQ.md) |
| Understand the system | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |

### 🎯 Common Next Steps

1. **Upload sample data** - Try `Mock data/Interview_mock_comprehensive.csv`
2. **Try the AI mapper** - Let AI organize your columns automatically
3. **Connect to real data** - Get credentials from your research coordinator
4. **Write queries** - Explore patterns in your data

**Remember:** You can't break anything by exploring. Click around and learn!

---

## Quick Reference

**Start:** `docker-compose --profile full up --build`  
**Stop:** `Ctrl+C` then `docker-compose down`

**URLs:**
- Main app: http://localhost
- Database admin: http://localhost:10035
- Default login: `admin` / `admin123`

**Need help?** Check [FAQ.md](FAQ.md) first!
