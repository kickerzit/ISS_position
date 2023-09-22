import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json() # json = způsob zápisu dat, přenosu dat, nezávislý na počítačové platformě. Rychlá komunikace, malý objem dat
# print(data)
# print(data["message"]) # success
# print(data["timestamp"]) # 1695320175
# print(data["iss_position"]) # {'latitude': '-39.8646', 'longitude': '-105.9442'}
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

print(f"Současná zeměpisná šířka ISS je:{latitude}")
print(f"Současná zeměpisná délka ISS je:{longitude}")