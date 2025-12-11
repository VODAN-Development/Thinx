# Thinx User Guide
## For Researchers Without Programming Background

---

## 📖 Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Main Features](#main-features)
4. [Step-by-Step Workflows](#step-by-step-workflows)
5. [Understanding Your Data](#understanding-your-data)
6. [Tips & Best Practices](#tips--best-practices)
7. [Troubleshooting](#troubleshooting)
8. [Getting Help](#getting-help)

---

## Introduction

### What is Thinx?

Thinx is a web-based research platform designed specifically for social scientists and humanitarian researchers studying human trafficking. It helps you:

- **Upload and analyze interview data** without writing code
- **Standardize data** from different sources into a common format
- **Visualize patterns** in trafficking routes, victim demographics, and crimes
- **Query your data** using simple forms and pre-built queries

### Who Should Use This Guide?

This guide is for researchers who:
- Have interview or survey data about human trafficking
- Want to analyze their data without programming skills
- Need to share findings with other researchers
- Are not familiar with databases or technical systems

### What You'll Need

Before starting, make sure you have:
1. **Access to the Thinx platform** (URL provided by your administrator)
2. **Login credentials** (username and password)
3. **Database connection details** (provided by administrator)
4. **Your research data** in Excel (.xlsx) or JSON format

---

## Getting Started

### First-Time Login

1. **Open your web browser** (Chrome, Firefox, Edge, or Safari recommended)
2. **Navigate to the Thinx URL** provided by your administrator
3. **Enter your username and password**
4. **Click "Login"**

> 💡 **Tip:** Bookmark the Thinx URL for easy access later!

### Understanding the Interface

After logging in, you'll see:

- **Header Bar** (top): Shows your username and navigation
  - **Help Button** (❓): Click for quick guidance
  - **Logout Button**: Sign out when you're done
  
- **Main Area** (center): Where you work with your data
  - Tabs or sections for different features
  
- **Footer** (bottom): Links to documentation and support

### Quick Help Panel

Click the **"Help"** button in the header to see quick tips about:
- 🔌 Database connections
- 📊 Data workflow
- 🤖 AI Smart Mapper
- 📈 Viewing data

---

## Main Features

### 1. Database Connection Manager 🔌

**Purpose:** Connect to the central database where your research data is stored.

**What you need:**
- Server address (e.g., "allegrograph" or an IP like "192.168.1.100")
- Port number (usually 10035)
- Repository name (e.g., "humantrafficking")
- Username and password

**Why it matters:** This connects Thinx to your research database so you can upload and query data.

---

### 2. Data Upload & Workflow 📊

**Purpose:** Upload raw interview data and automatically process it into standardized format.

**Supported formats:**
- Excel files (.xlsx, .xls)
- JSON files (.json)

**What happens:**
1. You upload your file
2. The system shows you the columns in your data
3. You map your columns to standard fields
4. The system processes and validates your data
5. Data is stored in the database ready for analysis

---

### 3. AI Smart Mapper 🤖

**Purpose:** Automatically suggests how your data columns match the standard format.

**How it helps:**
- Saves time mapping columns manually
- Reduces errors in data standardization
- Learns from common interview data patterns

**Requirements:**
- An AI model must be downloaded (done once by admin or yourself)
- Recommended models: llama3.2, phi3, or mistral

---

### 4. Data Viewer & Queries 📈

**Purpose:** Explore your processed data and run analyses.

**What you can do:**
- View all victim records in a table
- Run pre-built queries (e.g., "victims by border crossing")
- Export results for reports
- Visualize patterns with charts

---

## Step-by-Step Workflows

### Workflow 1: Setting Up Your Database Connection

**When to do this:** First time using Thinx, or when connecting to a new database.

**Steps:**

1. **Click "Connection Manager"** (or similar tab)
   
2. **Click "➕ Add AllegroGraph Connection"**
   
3. **Fill in the connection form:**
   
   | Field | What to Enter | Example |
   |-------|--------------|---------|
   | **Connection Name** | A friendly name for this database | "Main Research Database" |
   | **Server Address** | Hostname or IP from admin | "allegrograph" or "192.168.1.100" |
   | **Port** | Port number (usually 10035) | 10035 |
   | **Repository Name** | Database name from admin | "humantrafficking" |
   | **Username** | Your database username | your_username |
   | **Password** | Your database password | your_password |
   
4. **Check "Test connection before saving"** (recommended)
   
5. **Click "💾 Save Connection"**
   
6. **Wait for confirmation:**
   - ✅ Green message = Success!
   - ❌ Red message = Check your details and try again

---

### Workflow 2: Uploading and Processing Interview Data

**When to do this:** When you have new interview data to add to the database.

**Steps:**

**Step 1: Prepare Your Data**

Before uploading, ensure your data file:
- Is in Excel (.xlsx) or JSON format
- Contains interview records (one row per interview or victim)
- Has column headers that describe each field
- Is under 50MB in size

**Step 2: Access the Workflow Manager**

1. Click **"Workflow Manager"** or **"Data Upload"** in the navigation
2. You'll see a step-by-step process guide

**Step 3: Upload Your File**

1. **Drag and drop** your file onto the upload area, or **click to browse**
2. Select your Excel or JSON file
3. Wait for upload to complete (you'll see a green checkmark)

**Step 4: Review Data Structure**

1. The system shows you the **Common Data Model** (CDM)
   - This is the standard format all data follows
   - Fields include: victim demographics, crimes, borders, traffickers
   
2. Review the **field categories:**
   - 🔴 **Sensitive fields** (require extra protection)
   - 🟡 **Moderate sensitivity**
   - 🟢 **Low sensitivity**

**Step 5: Map Your Columns**

This is where you tell Thinx which column in your file matches which standard field.

**Option A: Manual Mapping**

1. For each standard field, select the matching column from your data
2. Example:
   - Standard field: "victim_age" → Your column: "Age of Interviewee"
   - Standard field: "victim_gender" → Your column: "Gender"

**Option B: AI Smart Mapper (Recommended)**

1. Click **"🤖 Use AI Smart Mapper"**
2. Select an AI model (if not already selected)
3. Click **"Suggest Mappings"**
4. Wait 30-60 seconds for AI to analyze your columns
5. Review the suggestions
6. Approve or adjust mappings as needed

**Step 6: Process Data**

1. Click **"▶️ Process Data"**
2. The system will:
   - Validate your data
   - Standardize formats
   - Check for errors
   - Create structured records
3. Wait for completion (may take a few minutes for large files)

**Step 7: Upload to Database**

1. Review the processing summary
2. Click **"⬆️ Upload to Database"**
3. Wait for confirmation
4. Your data is now in the database and ready for analysis!

---

### Workflow 3: Viewing and Querying Your Data

**When to do this:** After data is uploaded, when you want to analyze patterns.

**Steps:**

1. **Navigate to "Data Viewer"** or similar tab
   
2. **Choose what to view:**
   - **All Records**: See everything in the database
   - **Filtered View**: Narrow down by criteria
   - **Pre-built Queries**: Run common analyses

3. **Run a pre-built query:**
   
   Example queries you might see:
   - "Top 10 borders by victim count"
   - "Victims by nationality"
   - "Total extortion amounts by border"
   - "Abuse types experienced"

4. **View results:**
   - Tables show data in rows and columns
   - Charts visualize patterns
   - Export buttons let you save results

5. **Export your findings:**
   - Click "Export to CSV" for Excel-compatible files
   - Click "Export to PDF" for reports (if available)

---

## Understanding Your Data

### The Common Data Model (CDM)

Thinx uses a standardized format called the Common Data Model. This ensures all research data follows the same structure, making it easier to:
- Compare data from different sources
- Run consistent analyses
- Share findings with other researchers

**Main data categories:**

1. **Victim Information**
   - Age, gender, nationality
   - Unique identifier (victim_id)
   
2. **Crimes & Abuses**
   - Sexual violence (experienced/witnessed)
   - Physical/psychological abuse
   - Deaths witnessed
   
3. **Trafficking Details**
   - Borders crossed
   - Trafficker names
   - Routes taken
   
4. **Financial Exploitation**
   - Money extorted (amounts and currencies)
   - Payment methods

### Data Sensitivity Levels

Thinx classifies data by sensitivity:

- 🔴 **Highly Sensitive**: Personal identifiers, specific names, locations
  - Requires strict access controls
  - Examples: Full names, exact addresses
  
- 🟡 **Moderately Sensitive**: Demographics, general experiences
  - Standard protection measures
  - Examples: Age, nationality, abuse types
  
- 🟢 **Low Sensitivity**: Aggregated statistics, anonymized patterns
  - Can be shared more freely
  - Examples: Border crossing counts, average ages

### GDPR Compliance

All data handling follows GDPR principles:
- **Consent**: Only use data you have permission to use
- **Purpose**: Use data only for stated research purposes
- **Minimization**: Collect only what you need
- **Security**: Platform protects data with encryption and access controls
- **Rights**: Participants' rights to access/delete their data must be respected

---

## Tips & Best Practices

### Data Preparation Tips

✅ **Before uploading:**
- Remove any duplicate rows
- Ensure column headers are clear and descriptive
- Fill in missing values with "Unknown" or "Not Specified" rather than leaving blank
- Use consistent formatting (e.g., all dates in same format)

✅ **Column naming:**
- Use descriptive names: "Victim Age" not "Col3"
- Avoid special characters: Use "Victim_Age" not "Victim's Age!!!"
- Be consistent: "Gender" not "Gender" in one file and "Sex" in another

### Mapping Tips

✅ **When mapping columns:**
- Take your time to ensure correct mappings
- If unsure, consult the field descriptions
- Use AI Smart Mapper for first attempt, then review
- Mark fields as "Not in my data" if you don't have that information

✅ **Common mapping mistakes to avoid:**
- ❌ Mapping "Date of Birth" to "Age" (these are different!)
- ❌ Mapping currency amounts to nationality fields
- ❌ Mapping "yes/no" fields to text description fields

### Query Tips

✅ **Getting useful results:**
- Start with pre-built queries to learn the system
- Filter by date ranges to see trends over time
- Export results regularly for your records
- Document what queries you run for reproducibility

### Security Tips

✅ **Protecting sensitive data:**
- Always log out when done
- Never share your password
- Don't take screenshots of sensitive data
- Report any suspicious activity to your administrator

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: "Connection Failed" Error

**Symptoms:** Red error message when trying to connect to database.

**Solutions:**
1. Double-check all connection details (address, port, repository, credentials)
2. Ensure the database server is running (ask administrator)
3. Check if you're on the correct network (VPN may be required)
4. Try unchecking "Test connection" and save anyway if database is temporarily down

---

#### Issue: "File Upload Failed"

**Symptoms:** Upload doesn't complete, or shows an error.

**Solutions:**
1. Check file size (must be under 50MB)
2. Ensure file format is .xlsx or .json
3. Try closing and reopening the file in Excel, then save again
4. Check if file is corrupted (try opening it first)

---

#### Issue: "AI Smart Mapper Not Working"

**Symptoms:** No suggestions appear, or error when clicking "Suggest Mappings."

**Solutions:**
1. Ensure an AI model is downloaded and selected
2. Wait longer (can take 1-2 minutes for large datasets)
3. Try a different model (smaller models like phi3 may work better)
4. Fall back to manual mapping if AI continues to fail

---

#### Issue: "No Data Showing in Viewer"

**Symptoms:** Data viewer is empty or shows "No results."

**Solutions:**
1. Verify data was successfully uploaded (check for confirmation message)
2. Ensure you're connected to the correct database
3. Try a different query or remove filters
4. Check with administrator that data is in the repository

---

#### Issue: "Query Takes Too Long"

**Symptoms:** Query runs for several minutes without results.

**Solutions:**
1. Try a simpler query first
2. Add filters to narrow down results
3. Check database server performance with administrator
4. Be patient with very large datasets (may take time)

---

### When to Contact Support

Contact your system administrator or support team if:
- You've tried troubleshooting steps and issue persists
- You get error messages you don't understand
- You need help with data interpretation
- You suspect a security issue
- You need additional training or features

---

## Getting Help

### Resources

1. **Quick Help Panel**
   - Click the "❓ Help" button in the header
   - Provides quick tips for each feature
   
2. **Documentation**
   - Full README: Detailed technical documentation
   - FAQ: Frequently asked questions
   - Architecture docs: How the system works
   
3. **Your Administrator**
   - Database connection issues
   - User account problems
   - Feature requests
   - Security questions

### Support Channels

- **Email:** [Insert support email here]
- **Help Desk:** [Insert help desk URL here]
- **Documentation:** https://github.com/Justin2280/DataScienceInPractice

### Training Resources

- **Video tutorials:** [Insert video link if available]
- **Workshops:** Ask your administrator about upcoming training sessions
- **Peer support:** Connect with other researchers using Thinx

---

## Appendix: Glossary of Terms

**AllegroGraph:** The database system that stores your research data. A "triple store" designed for linked data.

**CDM (Common Data Model):** The standardized data format used by Thinx. Ensures consistency across datasets.

**Connection:** A saved configuration for accessing a database. Includes server address, credentials, etc.

**GDPR:** General Data Protection Regulation. European law protecting personal data privacy.

**JSON:** A file format for structured data. Can be opened in text editors.

**Mapping:** The process of matching your data columns to standard CDM fields.

**Query:** A request for specific data from the database. Like asking a question of your data.

**Repository:** A database within AllegroGraph where data is stored. Like a "folder" for data.

**RDF/Turtle:** Technical formats for storing linked data. Handled automatically by Thinx.

**Smart Mapper:** AI feature that automatically suggests column mappings.

**Triple Store:** A type of database optimized for linked data and relationships.

**Workflow:** A series of steps to accomplish a task (e.g., upload and process data).

---

## Need More Help?

This guide covers the essentials, but there's always more to learn! 

- For technical details, see the main [README.md](README.md)
- For troubleshooting, see [FAQ.md](FAQ.md)
- For administrator tasks, see [ADMIN_GUIDE.md](ADMIN_GUIDE.md)

**Happy researching! 🧠📊**
