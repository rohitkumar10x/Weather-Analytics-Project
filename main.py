# Weather App using OpenWeatherMap API
import requests

api_key = "08a092eeb061620f231192726acd4cae"
city = "Delhi"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

# Cleaned dataset for analysis 
city = data['name']
temp = data['main']['temp']
humidity = data['main']['humidity']
weather = data['weather'][0]['main']


# Timestamp conveert into human-readable format
from datetime import datetime
time = datetime.fromtimestamp(data['dt'])

# Database connection and insertion
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohit@89ji0",
    database="weather_db"
)

cursor = conn.cursor()

query = """
INSERT INTO weather_data (city, temperature, humidity, weather, timestamp)
VALUES (%s, %s, %s, %s, %s)
"""

values = (city, temp, humidity, weather, time)

cursor.execute(query, values)
conn.commit()

print("Data inserted successfully ✅")