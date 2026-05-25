import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=-33.92&longitude=18.42&current_weather=true")
data = response.json()["current_weather"]
temp = data["temperature"]
wind = data["windspeed"]
print(f"cape town weather \nTemperature: {temp} \nWind: {wind}")



