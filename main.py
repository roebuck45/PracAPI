# Practice API Call
# https://rapidapi.com/theapiguy/api/national-weather-service/

import requests
from pprint import pprint

url = "https://national-weather-service.p.rapidapi.com/zones/%7Btype%7D/%7BzoneId%7D/forecast"

headers = {
	"X-RapidAPI-Key": "6d84a55e3bmsh487c9b6e29c1760p1d0072jsn49a780a77f59",
	"X-RapidAPI-Host": "national-weather-service.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

pprint(response.json())