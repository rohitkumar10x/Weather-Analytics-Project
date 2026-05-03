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



