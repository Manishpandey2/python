import requests

city = input("Enter city: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

print(response.status_code)

data = response.json()

print("\n===== Weather Report =====")
print(f"📍 City: {city.title()}")
print(f"🌡️ Temperature: {data['current_condition'][0]['temp_C']}°C")
print(f"🤗 Feels Like: {data['current_condition'][0]['FeelsLikeC']}°C")
print(f"💧 Humidity: {data['current_condition'][0]['humidity']}%")
print(f"🌬️ Wind Speed: {data['current_condition'][0]['windspeedKmph']} km/h")
print(f"☁️ Condition: {data['current_condition'][0]['weatherDesc'][0]['value']}")