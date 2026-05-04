import time
import requests
import mysql.connector
from datetime import datetime

api_key = "08a092eeb061620f231192726acd4cae"
city = "Noida"

while True:
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        city_name = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['main']
        time_now = datetime.fromtimestamp(data['dt'])

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

        values = (city_name, temp, humidity, weather, time_now)

        cursor.execute(query, values)
        conn.commit()

        print("Data inserted successfully ✅")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Error:", e)

    time.sleep(60)  # 60 sec = 1 minute