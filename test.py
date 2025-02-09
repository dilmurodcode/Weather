import requests
from pprint import pprint

from ob_havo import API_KEY

url = f"https://api.openweathermap.org/data/2.5/weather?q=Samarqand&appid={API_KEY}"

response = requests.get(url)
data = response.json()
print(data)


