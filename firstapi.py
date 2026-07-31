import requests

response = requests.get("https://api.github.com")

print(type(response))
print(type(response.text))

data = response.json()

print(type(data))
print(data["current_user_url"])