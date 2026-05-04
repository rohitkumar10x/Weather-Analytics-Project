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
        
        # 🔥 CHANGE 1 → apna current time use karo (unique banega)
        time_now = datetime.now()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rohit@89ji0",
            database="weather_db"
        )

        cursor = conn.cursor()

        # 🔥 CHANGE 2 → duplicate check
        check_query = "SELECT COUNT(*) FROM weather_data WHERE timestamp = %s"
        cursor.execute(check_query, (time_now,))
        result = cursor.fetchone()[0]

        if result == 0:
            query = """
            INSERT INTO weather_data (city, temperature, humidity, weather, timestamp)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (city_name, temp, humidity, weather, time_now)

            cursor.execute(query, values)
            conn.commit()

            print("Inserted ✅")
        else:
            print("Duplicate skipped ❌")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Error:", e)

    time.sleep(60)