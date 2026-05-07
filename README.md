# 🌦 Real-Time Weather Monitoring & Analysis System

A real-time weather data pipeline project built using **Python**, **OpenWeather API**, **MySQL**, and **Power BI**.  
This project collects live weather data at regular intervals, stores it in a MySQL database, and visualizes insights through an interactive Power BI dashboard.

---

# 🚀 Project Overview

This project demonstrates an end-to-end data workflow:

1. Fetch live weather data using API
2. Store data into MySQL database
3. Perform data transformation
4. Create analytical dashboard in Power BI
5. Analyze weather trends and patterns

---

# 🛠 Technologies Used

- Python
- MySQL
- Power BI
- OpenWeather API
- Task Scheduler
- Power Query

---

# 📂 Project Workflow

## 1️⃣ Data Collection
Weather data is fetched using the OpenWeather API through a Python script.

Collected fields:
- City
- Temperature
- Humidity
- Weather Condition
- Timestamp

---

## 2️⃣ Database Storage
The fetched data is automatically stored inside a MySQL database table for further analysis.

---

## 3️⃣ Automation
Windows Task Scheduler is used to run the Python script automatically at fixed intervals.

---

## 4️⃣ Data Transformation
Using Power Query:
- Timestamp split into Date and Time
- Hour extracted for hourly analysis
- Data cleaned and formatted

---

## 5️⃣ Dashboard & Analysis
Interactive Power BI dashboard created for:
- Temperature trend analysis
- Humidity monitoring
- Hourly weather analysis
- Weather condition distribution
- KPI monitoring

---

# 📊 Dashboard Insights

The dashboard provides:
- Average Temperature
- Maximum & Minimum Temperature
- Average Humidity
- Hourly Temperature Trends
- Weather Type Frequency
- Time-based Weather Analysis

---

# 📁 Project Structure

```bash
weather-project/
│
├── weather_api.py
├── database.sql
├── powerbi_dashboard.pbix
├── README.md
└── screenshots/
