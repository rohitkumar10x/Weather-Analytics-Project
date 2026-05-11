# 🌦️ Real-Time Weather Data Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.9+-yellow?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-yellow?logo=powerbi)
![OpenWeatherAPI](https://img.shields.io/badge/API-OpenWeather-blue?logo=icloud)
![Status](https://img.shields.io/badge/Pipeline-100%25%20Automated-brightgreen)

An automated, end-to-end data analytics project that fetches real-time weather data using the OpenWeather API, stores it in a MySQL database, and visualizes live analytics in Power BI dashboards.

---

# 📊 Live Dashboard Preview

Designed to provide real-time insights with interactive and refreshable visuals.

<p align="center">
  <img src="https://github.com/rohitkumar10x/Weather-Analytics-Project/blob/main/Weather%20Analytics%20Dashbaord.jpg?raw=true" alt="Weather Dashboard" width="900">
</p>

---

# 🚀 Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline using Python, MySQL, and Power BI.

The system automatically collects live weather data for Noida using the OpenWeather API, processes and stores the information in a MySQL database, and generates dynamic visual reports inside Power BI for analytics and trend monitoring.

The entire workflow is fully automated using Windows Task Scheduler.

---

# 🔹 Key Features

- 🌐 Real-time weather data collection using OpenWeather API
- 🐍 Automated ETL pipeline built with Python
- 🗄️ MySQL database integration for structured data storage
- 📈 Interactive Power BI dashboard with live refresh support
- ⏰ Windows Task Scheduler automation
- 📊 Historical weather trend analysis
- 🔄 Continuous data ingestion and updating
- 🧮 DAX-based calculations and comparisons
- 🧹 Data cleaning and timestamp management
- 🔗 Git & GitHub version control integration

---

# 🛠️ Tech Stack & Tools

| Category | Tools & Technologies |
|---|---|
| Programming Language | Python |
| Database | MySQL |
| Data Visualization | Power BI |
| API Source | OpenWeather API |
| Automation | Windows Task Scheduler |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```bash
├── .gitattributes
├── main.py
├── queries.sql
├── README.md
├── Weather Analytics Dashbaord.jpg
└── Weather Analytics Dashbaord.pbix
```

### 📌 File Description

| File Name | Description |
|---|---|
| `main.py` | Python script for API integration, automation, and database insertion |
| `queries.sql` | SQL queries for table creation and analysis |
| `README.md` | Project documentation |
| `Weather Analytics Dashbaord.jpg` | Dashboard preview image |
| `Weather Analytics Dashbaord.pbix` | Power BI dashboard file |

---

# ⚙️ Workflow Architecture

## 1️⃣ Extract
The Python script fetches live weather data in JSON format from the OpenWeather API.

## 2️⃣ Transform
The raw data is cleaned, formatted, timestamped, and categorized into different time slots.

## 3️⃣ Load
The processed data is inserted automatically into the MySQL database.

## 4️⃣ Visualize
Power BI connects with MySQL to generate interactive dashboards and live reports.

---

# 📈 Dashboard Insights

### 🌡️ Temperature Analysis
- Average temperature tracking
- Maximum and minimum temperature monitoring
- Daily temperature trend visualization

### 💧 Humidity Monitoring
- Humidity level comparisons
- Relationship between humidity and weather conditions

### ⏰ Time-Slot Analytics
Data categorized into:
- Morning
- Afternoon
- Evening
- Night

### 📅 Historical Comparison
- Today vs Yesterday analysis
- Historical weather trend analysis

### 🔄 Live Refresh Capability
Dashboard updates instantly with a single refresh action.

---

# 🔧 Automation Process

The complete pipeline is automated using **Windows Task Scheduler**:

1. Python script executes automatically at scheduled intervals
2. API fetches latest weather data
3. MySQL database gets updated
4. Power BI dashboard reflects updated records

This enables a fully automated real-time analytics workflow.

---

# 📚 Concepts Used

- ETL Pipeline
- API Integration
- Database Connectivity
- Data Cleaning
- Automation
- Data Analytics
- Dashboard Design
- DAX Calculations
- SQL Queries
- Real-Time Reporting

---

# 🔮 Future Improvements

- [ ] Multi-city weather tracking support
- [ ] Machine Learning-based forecasting
- [ ] Cloud database deployment (AWS/Azure)
- [ ] Email alert system for extreme weather
- [ ] Web dashboard integration
- [ ] Mobile responsive analytics dashboard

---

# 💻 How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/rohitkumar10x/Weather-Analytics-Project.git
```

## 2️⃣ Install Required Libraries

```bash
pip install requests mysql-connector-python
```

## 3️⃣ Configure MySQL Database

- Create database and tables using `queries.sql`

## 4️⃣ Add API Key

Replace your OpenWeather API key inside `main.py`

```python
api_key = "YOUR_API_KEY"
```

## 5️⃣ Run the Script

```bash
python main.py
```

## 6️⃣ Open Power BI Dashboard

Open:

```bash
Weather Analytics Dashbaord.pbix
```

Refresh the dashboard to view live analytics.

---

# 👨‍💻 Developer

## Rohit Kumar

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/rohit-kumar-93a123362/)

---

# ⭐ Project Highlights

✅ End-to-End Data Analytics Project  
✅ Real-Time API Data Pipeline  
✅ Fully Automated Workflow  
✅ Power BI Dashboard Integration  
✅ Historical Data Tracking  
✅ Industry-Level ETL Implementation  
