# Thinx: Human Trafficking Research Platform

> **Project Name:** Thinx  
> **Course:** Data Science in Practice (Leiden University)  

[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-green.svg)](https://vuejs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

> **🚀 Quick Start:** Install Docker → Run one command → Start analyzing data in 5 minutes  
> **📚 Comprehensive Guides:**  
> • **[USER_GUIDE.md](USER_GUIDE.md)** - For researchers without programming background ⭐  
> • **[ADMIN_GUIDE.md](ADMIN_GUIDE.md)** - For system administrators deploying centrally ⭐  
> • **[FAQ.md](FAQ.md)** - Common questions answered

---

## 📖 Documentation Guide

**👉 New to Thinx? Start here:**

| I Am... | Start Here |
|---------|------------|
| 🚀 **New User** | **[QUICK_START.md](QUICK_START.md)** - Get running in 10 minutes |
| 👨‍🔬 **Researcher** | **[USER_GUIDE.md](USER_GUIDE.md)** - Learn all features (no coding needed) |
| 🔧 **Administrator** | **[ADMIN_GUIDE.md](ADMIN_GUIDE.md)** - Deploy and manage for teams |
| ❓ **Need Help** | **[FAQ.md](FAQ.md)** - Common questions answered |

**Additional Documentation:**
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - System design & components
- [docs/AI_MAPPER.md](docs/AI_MAPPER.md) - AI Smart Mapper setup & usage  
- [docs/](docs/) - Complete technical documentation
- `check-setup.ps1` / `check-setup.sh` - Validate system prerequisites

---

## 📋 Table of Contents

- [Introduction](#introduction)
- [Quick Start](#quick-start)
- [End-User Manual](#end-user-manual)
  - [Adding a Dataset Connection](#adding-a-dataset-connection)
  - [Viewing Data](#viewing-data)
- [AI Smart Mapper](#ai-smart-mapper)
  - [What It Does](#what-it-does)
  - [Quick Start with AI](#quick-start-with-ai)
  - [Finding Models](#finding-models)
- [Developer Guide](#developer-guide)
  - [Installation](#installation)
  - [Architecture](#architecture)
  - [Project Structure](#project-structure)
  - [Data Processing Pipeline](#data-processing-pipeline)
  - [Modifying the Common Data Model](#modifying-the-common-data-model)
  - [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)
- [Project Background](#project-background)
- [License](#license)

---

## Introduction

**Thinx** is a research platform designed to help social scientists and humanitarian researchers analyze human trafficking data without needing programming skills. Built at Leiden University, this tool lets you explore interview data, visualize patterns, and generate insights about refugee trafficking routes and victim experiences.

### What Can You Do With Thinx?

✅ **Connect to Research Databases** - Link to datasets provided by research partners using simple connection forms  
✅ **Visualize Data Instantly** - See statistics, charts, and tables without writing code  
✅ **AI-Assisted Data Processing** - Let AI help map your interview columns to standard formats  
✅ **Analyze Patterns** - Explore trafficking routes, victim demographics, and crime patterns  
✅ **Privacy-First Design** - All data processing happens on your computer or secure server

### Who Is This For?

- 👨‍🔬 **Researchers** studying human trafficking and migration
- 📊 **Data Analysts** working with interview and survey data
- 🏛️ **Policy Makers** needing evidence-based insights
- 🎓 **Students** learning about data science in humanitarian contexts

### Key Features

| Feature | What It Does | Why It Matters |
|---------|--------------|----------------|
| **Simple Setup** | Install with one command | No technical expertise needed |
| **Multiple Datasets** | Connect to different research databases | Compare data from different sources |
| **FAIR Data Discovery** | Browse EEPA data catalogs before requesting access | Find relevant datasets easily |
| **Interactive Dashboards** | Click-and-explore data visualization | See patterns instantly |
| **AI Smart Mapper** | Automatically organize your data columns | Save hours of manual work |
| **Privacy Protected** | All data stays on your infrastructure | GDPR compliant, secure |

> **💡 New to this?** Start with the [Quick Start Guide](QUICK_START.md) - you'll be exploring data in 5 minutes!
> 
> **📚 Looking for data?** See [FAIR Data Point Integration](docs/FAIR_DATA_POINT.md) to browse available EEPA datasets

---

## Quick Start

### Pre-Flight Check: Is Your System Ready?

**Not sure if you have everything?** Run our automated checker:

**Windows:**
```powershell
.\check-setup.ps1
```

**Mac/Linux:**
```bash
chmod +x check-setup.sh
./check-setup.sh
```

This script checks:
- ✅ Docker installation and status
- ✅ Available disk space
- ✅ Port availability
- ✅ Project files integrity

### What You Need Before Starting

| Requirement | Why You Need It | Where to Get It |
|------------|-----------------|-----------------|
| **Docker Desktop** | Runs the application | [docker.com/get-started](https://docker.com/get-started) |
| **Web Browser** | Access the interface | Chrome, Firefox, Edge, or Safari |
| **2GB Free Disk Space** | Store the application | Check your hard drive |
| **Dataset Credentials** | Connect to research data | Contact your data provider |

💡 **Tip:** Run `check-setup.ps1` (Windows) or `check-setup.sh` (Mac/Linux) to verify your system automatically!

### Installation Steps

**Step 1: Check if Docker is Running**
- Look for the Docker whale icon in your taskbar/menu bar
- If not visible, open Docker Desktop application

**Step 2: Download This Project**
- If you have Git: `git clone [repository-url]`
- Or download the ZIP file and extract it

**Step 3: Open Terminal/Command Prompt**
- **Windows**: Search for "PowerShell" or "Command Prompt"
- **Mac**: Search for "Terminal"
- Navigate to the project folder: `cd path/to/DataScienceInPractice`

**Step 4: Start the Application**

Choose one option based on what you need:

**🌟 Option A: Full System (Recommended for First-Time Users)**
Includes everything: Database, AI features, and interface
```bash
docker-compose --profile full up --build
```

**Option B: Without AI Features**
Faster to start, but no automatic data mapping
```bash
docker-compose --profile no-ai up --build
```

**Step 5: Wait for Startup**
You'll see text scrolling in the terminal. Wait until you see messages like:
- ✅ `frontend_1 | ready in XXX ms`
- ✅ `backend_1 | Running on http://0.0.0.0:5000`

This usually takes 2-5 minutes on first startup.

**Step 6: Open Your Browser**
Once everything is ready, visit: **http://localhost**

### 🎉 Success! You should see the Thinx homepage.

---

## Accessing the Application

After startup, these web addresses are available:

| Service | URL | What It's For |
|---------|-----|---------------|
| **🌐 Main Interface** | http://localhost | **Start here** - This is where you work |
| ⚙️ API Server | http://localhost:5000 | Backend (usually don't need to visit) |
| 🗄️ Database Admin | http://localhost:10035 | Advanced users - view raw data |

---

# 🎯 User Guide for Researchers

This section explains how to use Thinx **without any programming knowledge**. If you've never worked with databases or web applications before, don't worry - we'll guide you through every step!

## Understanding Connections

Think of a **connection** like a bookmark to a research database. Just like you save website bookmarks in your browser, Thinx saves database connections so you can easily switch between different datasets.

**Why do I need this?** Your research data lives in a secure database (AllegroGraph). To view that data, you need to tell Thinx:
- Where is the database? (server address)
- What's it called? (repository name)
- How do I log in? (username and password)

You typically get these details from your research coordinator or data provider.

## Adding a Dataset Connection

### Step 1: Click "Add New Connection"

On the main screen, look for the **"➕ Add New Connection"** button (it's purple).

### Step 2: Fill in the Connection Form

You'll see a form with several fields. Here's a plain-English explanation of each:

| Field | What It Means | What to Enter | Example |
|-------|---------------|---------------|---------|
| **Connection Name** | A nickname for this dataset (you choose this) | Any memorable name | `"Libya Study 2024"` or `"Main Dataset"` |
| **Server URL/IP** | Where the database is located | Get from data provider | `allegrograph` (if using Docker)<br>`192.168.1.100` (if remote server) |
| **Port** | Technical gateway number | Usually `10035` | `10035` |
| **Repository Name** | The specific database name | Get from data provider | `humantrafficking` or `research_data` |
| **Username** | Your login name | Get from data provider | `researcher1` |
| **Password** | Your password | Get from data provider | `••••••••` |

**🔒 Security Note:** Your password is never shown on screen and is stored securely.

### Step 3: Save the Connection

1. Click **"Save Connection"** (button at the bottom of the form)
2. Wait a few seconds while Thinx tests the connection
3. If successful: ✅ "Connection created successfully"
4. Your new connection appears in the list below

### ⚠️ Connection Problems?

If you see **"Failed to connect"** or an error message, try these solutions:

| Problem | What to Check | How to Fix |
|---------|--------------|------------|
| **"Connection refused"** | Is the database running? | Contact your data provider or restart Docker |
| **"Invalid credentials"** | Username/password wrong? | Double-check the credentials (copy-paste to avoid typos) |
| **"Unknown host"** | Server address wrong? | Verify the server URL with your data provider |
| **"Timeout"** | Network issue? | Check your internet connection or firewall settings |

**💡 Still stuck?** See the [Troubleshooting section](#troubleshooting) below for detailed help.

## Viewing and Exploring Data

### Step 1: Select a Connection

In the **Connections List** on the main page, find the dataset you want to explore.

### Step 2: Activate and View

Click the **"📊 View Data"** button next to your chosen connection.

**What happens now:**
1. Thinx connects to the database ⚡
2. The connection becomes **active** (you'll see a purple "Active" badge)
3. The **Data Viewer** screen opens

### Step 3: Understand What You're Seeing

The Data Viewer has three main sections:

#### 📊 Statistics Dashboard (Top of Page)

Four key metrics in colored boxes:

| Metric | What It Means | Why It Matters |
|--------|--------------|----------------|
| **Victims** | Total victims in this dataset | Understand the scale of your research |
| **Crimes** | Total criminal incidents recorded | See how many abuse events are documented |
| **Borders** | Unique border crossings mentioned | Identify migration routes |
| **Total Triples** | Database size (technical) | Roughly = total data points × 3 |

#### 📋 Data Table (Middle of Page)

A spreadsheet-style view of victim records:

- **Victim ID** - Unique code for each victim (e.g., `victim_001`)
- **Age** - Age at time of interview (or "N/A" if not recorded)
- **Gender** - Gender identity (Male, Female, Non-binary, or Unknown)
- **Nationality** - Country of origin

**💡 Tip:** Click column headers to sort by that field (feature may vary).

#### 🔧 Navigation Controls (Bottom of Page)

- **🔄 Refresh Data** - Reload if the database has been updated
- **Results per page** - Show 25, 50, 100, or 200 rows at once
- **← Previous / Next →** - Move between pages of results
- **Page X of Y** - Shows which page you're on

### Managing Multiple Connections

You can add multiple connections for different datasets:

1. Go back to the **Connection Manager** (click "← Back to Connections")
2. All your saved connections are listed
3. Click **"✓ Activate"** to switch between datasets
4. Click **"✏️ Edit"** to modify connection details
5. Click **"🗑️ Delete"** to remove a connection

## FAIR-OLR Compliance

This system adheres to **FAIR-OLR** (Findable, Accessible, Interoperable, Reusable - Ontology-based Layered Routing) principles.

- **Findable:** Datasets are discoverable through external FAIR Data Points (FDPs).
- **Accessible:** Data is accessible via standard protocols (SPARQL, HTTP) with proper authentication.
- **Interoperable:** Data uses the `hds_cdm.ttl` Common Data Model for semantic consistency.
- **Reusable:** Data is structured with clear licensing and provenance metadata.


# 🤖 AI Smart Mapper

## What It Does

The **AI Smart Mapper** is an experimental feature that uses local Large Language Models (LLMs) to automatically suggest mappings between your data columns and the Common Data Model (CDM) fields. This significantly reduces manual work when structuring your interview data.

**Key Features:**
- 🔒 **100% Local Processing** - All data stays on your infrastructure (GDPR compliant)
- 🧠 **Intelligent Mapping** - AI understands context and suggests best matches
- ⚡ **Fast Setup** - Download models directly from the UI
- 🎯 **High Accuracy** - Uses state-of-the-art open-source models

## Quick Start with AI

### 1. Start with Full Profile

The AI mapper requires Ollama to be running:

```bash
docker-compose --profile full up --build
```

This starts all services including the Ollama container.

### 2. Navigate to Step 3

1. Upload your data file in **Step 2**
2. Go to **Step 3: Schema & Validation**
3. Find the **"AI Smart Mapper"** section

### 3. Download a Model

In the "Download New Model" section:

1. Enter a model name (e.g., `llama3.2`)
2. Click **"Download"**
3. Wait 5-15 minutes for download (depends on model size)
4. Click **"Refresh"** to see it in the list

### 4. Generate Mappings

1. Select your downloaded model from the dropdown
2. Click **"Suggest Mappings"**
3. Review the AI's suggestions in the table
4. Click **"Apply Mapping to File"** to restructure your data

## Finding Models

Browse the complete model library at **[ollama.com/library](https://ollama.com/library)**

### Recommended Models

| Model Name | Size | Best For | Command |
|------------|------|----------|---------|
| `llama3.2` | 2GB | General use, good accuracy | Most users ⭐ |
| `phi3` | 2.3GB | Fast processing | Limited resources |
| `mistral` | 4GB | High accuracy | Better results needed |
| `gemma2:2b` | 1.6GB | Lightweight | Quick testing |

**How to choose:**
- **New users**: Start with `llama3.2` - best balance of speed and quality
- **Better accuracy needed**: Try `mistral` or `llama3:8b`
- **Fast processing**: Use `phi3` or `gemma2:2b`

## How It Works

```
Your Data File → AI Analyzer → Suggested Mappings → Apply → Structured Data
                     ↓
              (Ollama + LLM Model)
```

1. **Upload**: Your Excel/JSON file with arbitrary column names
2. **Analyze**: AI compares your columns to CDM schema
3. **Suggest**: Returns a mapping (e.g., "name" → "victim_name")
4. **Apply**: Automatically renames columns in your file
5. **Process**: Continue to RDF generation with structured data

**Privacy Note:** All processing happens locally in Docker containers. Your sensitive data never leaves your infrastructure.

## Detailed Documentation

For comprehensive information including:
- Technical details and API reference
- Troubleshooting guide
- Advanced configuration
- Performance tuning
- Custom model setup

See the complete guide: **[docs/AI_MAPPER.md](docs/AI_MAPPER.md)**

---

# 💻 Developer Guide

This section is for **developers and maintainers** who need to install, modify, or extend the application.

## Installation

### Prerequisites

- **Docker** (20.10+) and **Docker Compose** (2.0+)
- **Git** (optional, for cloning)
- **Node.js** (20.x LTS) - only for local frontend development
- **Python** (3.11+) - only for local backend development

### Development Mode

For active development with hot-reload:

**Backend (Flask):**
```bash
cd backend
pip install -r requirements.txt
python app.py
# Server runs on http://localhost:5000
```

**Frontend (Vue.js):**
```bash
cd frontend
npm install
npm run dev
# Server runs on http://localhost:80
```

### Stopping the Application

```bash
# Stop containers (keeps data)
docker-compose stop

# Stop and remove containers (keeps data in volumes)
docker-compose down

# Stop and remove everything including data
docker-compose down -v
```

## Architecture

The application uses a **microservices architecture** with three containers:

```
┌─────────────────────────────────────────────────────────┐
│                  Docker Compose Network                  │
│                                                           │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────┐ │
│  │   Frontend   │◄──►│   Backend    │◄──►│AllegroGraph│
│  │   Vue.js     │    │   Flask API  │    │  Database  │
│  │   (Port 80)  │    │  (Port 5000) │    │(Port 10035)│
│  └──────────────┘    └──────────────┘    └───────────┘ │
└─────────────────────────────────────────────────────────┘
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Vue.js 3 + Vite | User interface |
| **Backend** | Flask 3.0 | REST API |
| **Database** | AllegroGraph 8.0 | RDF triple store |
| **Web Server** | Nginx (Alpine) | Frontend serving |
| **Containerization** | Docker Compose | Orchestration |

For detailed architecture documentation, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).


## Data Processing Pipeline

The project includes a complete data processing pipeline for converting raw interview data into RDF format:

### 1. Data Extraction & Cleaning

**Purpose:** Clean and organize raw data into a structured format.

- **Input:** Raw interview data in Excel format
- **Process:**
  - `processing.ipynb`: Cleans and standardizes the data
  - `json_creator.ipynb`: Merges duplicate records and creates final JSON
- **Outputs:**
  - `victims.json`: Structured dataset with one entry per interview
  - `cleaned_data.json`: Final clean dataset with one record per victim

### 2. Data Storage (RDF Conversion)

**Purpose:** Convert structured data into RDF format and store it in AllegroGraph.

**Key Steps:**
1. **Loading the CDM (hds_cdm.ttl):** Load the Common Data Model ontology to define relationships and structure
2. **RDF Triple Generation:** Transform victim attributes into RDF triples according to the CDM
3. **Saving RDF Data:** Save as `Human_trafficking_output.ttl`
4. **Uploading to AllegroGraph:** Push data to the database

**Script:** `push_to_allegrograph.py`

```python
# Basic usage
python push_to_allegrograph.py
```

### 3. Data Analytics

**Purpose:** Analyze and visualize the structured data using SPARQL queries.

The `sparql queries/` folder contains sample queries:

**Production Queries** (for full datasets):
- **count_abuse_witnessed.rq** - Calculates total victims who witnessed abuses
- **top10_highest_victim_borders.rq** - Identifies top 10 borders by victim count
- **victim_count_by_border_and_trafficker.rq** - Trafficker-border relationships
- **total_extortion_amount_per_border.rq** - Total extortion amounts by border
- **max_extortion_amount_per_border.rq** - Maximum extortion per border

**Mock Data Queries** (for testing with `Mock data/`):
- **mock_data_test.rq** - Basic victim information retrieval
- **mock_extortion_analysis.rq** - Extortion statistics by nationality
- **mock_crime_stats.rq** - Crime type frequency analysis

💡 **Tip:** Use the mock data queries when testing the system with files from `Mock data/` folder!

## Modifying the Common Data Model

The Common Data Model (CDM) is defined in `hds_cdm.ttl` and also reflected in `backend/models.py`. The CDM defines the structure of victim data. To modify it:

### Adding a New Field to Existing Entity

**Example:** Add a `birthdate` field to the Victim entity

#### Step 1: Update the CDM Schema

**File:** `backend/models.py`

```python
CDM_SCHEMA = {
    'Victim': {
        'description': 'Personal information about trafficking victims',
        'fields': [
            # ... existing fields ...
            {'name': 'birthdate', 'type': 'string', 'required': False, 
             'sensitive': True, 'gdpr_category': 'personal'},  # ✅ ADD THIS
        ]
    },
    # ... rest of schema ...
}
```

#### Step 2: Update the Backend Query

**File:** `backend/app.py` - Find the `get_data()` function:

```python
query = f"""
PREFIX ht: <http://example.org/humantrafficking/>

SELECT DISTINCT ?victim ?age ?gender ?nationality ?birthdate
WHERE {{
    ?victim a ht:Victim .
    OPTIONAL {{ ?victim ht:age ?age }}
    OPTIONAL {{ ?victim ht:gender ?gender }}
    OPTIONAL {{ ?victim ht:nationality ?nationality }}
    OPTIONAL {{ ?victim ht:birthdate ?birthdate }}  # ✅ ADD THIS
}}
LIMIT {limit}
OFFSET {offset}
"""
```

#### Step 3: Update the Frontend DataViewer

**File:** `frontend/src/components/DataViewer.vue`

```vue
<template>
  <table class="data-table">
    <thead>
      <tr>
        <th>Victim ID</th>
        <th>Age</th>
        <th>Gender</th>
        <th>Nationality</th>
        <th>Birth Date</th> <!-- ✅ ADD THIS -->
      </tr>
    </thead>
    <tbody>
      <tr v-for="(row, index) in data" :key="index">
        <td>{{ truncateUri(row.victim) }}</td>
        <td>{{ row.age || 'N/A' }}</td>
        <td>{{ row.gender || 'N/A' }}</td>
        <td>{{ row.nationality || 'N/A' }}</td>
        <td>{{ row.birthdate || 'N/A' }}</td> <!-- ✅ ADD THIS -->
      </tr>
    </tbody>
  </table>
</template>
```

#### Step 4: Rebuild and Test

```bash
# Rebuild containers
docker-compose up --build

# Test the application at http://localhost
```

### GDPR Categories

Use these categories for sensitive data:

- `'personal'` - Name, age, contact info
- `'special_category'` - Race, ethnicity, sexual orientation
- `'criminal_offense'` - Crime details
- `None` - Non-sensitive data

## API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### Connection Management

**GET /api/connections**
- Get all saved connections
- Response: `{ success: true, connections: [...], count: 2 }`

**POST /api/connections**
- Create new connection
- Body: `{ name, host, port, repository, username, password }`
- Response: `{ success: true, message: "...", connection: {...} }`

**GET /api/connections/:id**
- Get specific connection
- Response: `{ success: true, connection: {...} }`

**PUT /api/connections/:id**
- Update connection
- Response: `{ success: true, connection: {...} }`

**DELETE /api/connections/:id**
- Delete connection
- Response: `{ success: true, message: "..." }`

**POST /api/connections/:id/activate**
- Set active connection
- Response: `{ success: true, message: "..." }`

**GET /api/connections/active**
- Get active connection
- Response: `{ success: true, connection: {...} }`

#### Data Operations

**GET /api/data**
- Query victim data
- Params: `connection_id` (optional), `limit`, `offset`
- Response: `{ success: true, data: [...], count: 50 }`

**POST /api/query**
- Execute custom SPARQL query
- Body: `{ query: "SELECT ...", connection_id: "..." }`
- Response: `{ success: true, results: [...] }`

**GET /api/statistics**
- Get dataset statistics
- Params: `connection_id` (optional)
- Response: `{ success: true, statistics: {...} }`

#### Metadata

**GET /api/ontology**
- Get CDM structure
- Response: `{ success: true, ontology: {...} }`

**GET /api/health**
- Health check
- Response: `{ status: "healthy", service: "flask_api", timestamp: "..." }`

---

## Troubleshooting

### Problem: "Connection refused" when accessing http://localhost

**Solution:**
1. Check if containers are running: `docker-compose ps`
2. Restart services: `docker-compose restart`
3. Check logs: `docker-compose logs frontend`

### Problem: "Failed to connect to AllegroGraph"

**Solution:**
1. Verify AllegroGraph is running: `docker-compose logs allegrograph`
2. Check credentials are correct
3. Try accessing directly: http://localhost:10035

### Problem: Frontend shows "API Error: No response from server"

**Solution:**
1. Check backend is running: `docker-compose ps backend`
2. Check backend logs: `docker-compose logs backend`
3. Verify CORS is enabled in `backend/app.py`

### Problem: "No data found in repository"

**Solution:**
1. Verify you've uploaded data to AllegroGraph using `push_to_allegrograph.py`
2. Check the repository name matches
3. Test with a simple SPARQL query in AllegroGraph console

### Problem: Changes not appearing after editing code

**Solution:**
```bash
# Rebuild containers
docker-compose up --build

# Or rebuild specific service
docker-compose up --build backend
```

### Problem: Port already in use

**Solution:**
```bash
# Find process using port 80 (Windows)
netstat -ano | findstr :80

# Find process using port 80 (Mac/Linux)
lsof -i :80

# Stop other services or change ports in docker-compose.yml
```

---

## Project Background

**Thinx** is a course project for **Data Science in Practice** at Leiden University's Master's programme. The project demonstrates practical application of:
- 📊 Data engineering and ETL pipelines
- 🔗 Semantic web technologies (RDF, SPARQL, ontologies)
- 🏗️ Modern web architecture (microservices, containerization)
- 🔒 Ethical data management
- 🎨 Full-stack development (Flask backend + Vue.js frontend)

The platform focuses on analyzing, cleaning, and visualizing data about human trafficking, particularly in North Africa.

### Research Context

Human trafficking is a serious humanitarian crisis affecting refugees fleeing difficult situations. Many refugees are promised safe passage but are instead taken hostage, exploited, or abused. This application helps researchers:

- **Document trafficking patterns** through structured data
- **Analyze migration routes** and identify high-risk areas
- **Support humanitarian efforts** with actionable insights
- **Inform policy-making** with evidence-based research

### Dataset

The dataset is based on interviews with refugees and contains:
- Transit routes through Libya and North Africa
- Trafficker information and criminal networks
- Abuse reports (sexual violence, extortion, deaths)
- Border crossing details and geographic data

### Mock Data for Testing

The `Mock data/` folder contains **sample datasets** for testing and learning:

**📊 Interview_mock_comprehensive.csv** ⭐ **RECOMMENDED**
- Complete CDM-aligned dataset with 10 realistic cases
- Covers all entities: Victim, Incident, Trafficker, Location
- Perfect for testing AI Smart Mapper with proper Entity.field mappings
- Includes varied scenarios: trafficking, smuggling, kidnapping

**📁 Legacy Excel files** (Interview_mock_1.xlsx, Interview_mock_2.xlsx, Interview_mock_3.xlsx)
- Original test files (may need column updates)

**Use mock data for:**
- 🧪 **Testing** the AI mapping and data transformation features
- 📚 **Learning** how Thinx works with realistic data
- 🔒 **Development** without exposing sensitive information
- 📊 **Demonstrations** of the platform capabilities

See `Mock data/README.md` for detailed usage instructions and CDM mapping examples.

### Ethical Considerations

All data is:
- ✅ **Anonymized** - No personally identifiable information
- ✅ **Consent-based** - Collected with participant permission
- ✅ **GDPR compliant** - Sensitive fields marked and protected
- ✅ **Research-only** - For academic and humanitarian purposes
- 🧪 **Mock data available** - Safe testing data in `Mock data/` folder

---

## 🧠 Experimental AI Features

This project includes an **experimental AI integration** using [Ollama](https://ollama.com/) to provide "Smart Mapping" capabilities. This allows the system to automatically suggest mappings between your uploaded file columns and the Common Data Model (CDM).

### Enabling AI Features

1. Start the application with the AI profile:
   ```bash
   docker-compose --profile ai up --build
   ```

2. Once running, you need to pull the LLM model (first time only):
   ```bash
   docker exec -it ollama_service ollama pull llama3
   ```
   *(Note: This requires ~4GB of disk space and may take time depending on your internet connection)*

3. The "Smart Map" feature will now be available in the API.

---

## Querying Multiple Repositories (Federated Queries)

AllegroGraph doesn't support SPARQL SERVICE clauses for cross-repository queries on the same server. To query multiple repositories (e.g., danieltesfa, Kai Smits, Morgana), use the Python script approach:

**Usage:**
```bash
pip install -r federated_requirements.txt
python federated_query.py
```

This script uses AllegroGraph's REST API to query all repositories and combines results into CSV files for aggregate statistics, border analysis, and demographics.

---

## License

MIT License - See LICENSE file for details

---

## Additional Documentation

For a complete documentation index, see **[docs/README.md](docs/README.md)**.

Core documentation:
- **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Detailed architecture documentation
- **[docs/DOCKER_USAGE.md](docs/DOCKER_USAGE.md)** - Docker deployment guide
- **[docs/MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md)** - Migrating from old Flask template version
- **[docs/IMPLEMENTATION_SUMMARY.md](docs/IMPLEMENTATION_SUMMARY.md)** - Implementation details
- **[docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)** - Detailed file structure
- **[docs/DIAGRAMS.md](docs/DIAGRAMS.md)** - Visual diagrams

---

## Support & Contact

- **GitHub Repository:** https://github.com/Justin2280/DataScienceInPractice
- **Documentation:** See additional markdown files in the repository
- **Issues:** Report bugs or request features via GitHub Issues

---

## Acknowledgments

- **Leiden University** - Data Science in Practice course
- **FIELD Lab** - Human trafficking research initiative
- **AllegroGraph** - RDF database platform

---

**Last Updated:** December 2025  
**Version:** 2.0.0  
**Refactored:** Monolithic Flask → Flask API + Vue.js SPA
