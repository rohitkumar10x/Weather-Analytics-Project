# 🌦️ Real-Time Weather Data Analytics Pipeline

![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-yellow?logo=powerbi)
![Status](https://img.shields.io/badge/Pipeline-100%25%20Automated-brightgreen)

An automated, end-to-end data analytics project that ingests real-time weather data from OpenWeather API, stores it in a MySQL database, and visualizes live trends in Power BI.

---

## 📊 Live Dashboard Preview
Designed to provide real-time insights with an on-click refresh mechanism.

<p align="center">
  <img src="https://github.com/rohitkumar10x/Weather-Analytics-Project/blob/main/Weather%20Analytics%20Dashbaord.jpg?raw=true" alt="Weather Dashboard" width="900">
</p>

---

## 🚀 Project Overview
This project demonstrates the complete **ETL (Extract, Transform, Load)** cycle. It fetches live weather parameters (Temperature, Humidity, Conditions) for Noida via API, cleans the data, and maintains a historical record for trend analysis.

### 🔹 Key Features
* **Live Data Ingestion:** Automated fetching using OpenWeatherMap API.
* **Database Automation:** Python script manages live data insertion into MySQL.
* **Scheduled Tasks:** Fully automated data pipeline using Windows Task Scheduler.
* **Advanced Analytics:** Dynamic Power BI visuals with DAX for Today/Yesterday/Historical comparisons.
* **Version Control:** Managed and tracked using Git and GitHub.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python (main.py)
* **Database:** MySQL (queries.sql)
* **Visualization:** Power BI (Weather Analytics Dashbaord.pbix)
* **API:** OpenWeather API
* **Automation:** Windows Task Scheduler
* **Version Control:** Git & GitHub

---

## 📂 Project Structure
As shown in the repository:
```bash
├── .gitattributes
├── main.py                          # Python script for API ingestion & automation
├── queries.sql                      # Database schema & analytical SQL queries
├── README.md                        # Documentation
├── Weather Analytics Dashbaord.jpg  # Dashboard preview image
└── Weather Analytics Dashbaord.pbix # Power BI project file
