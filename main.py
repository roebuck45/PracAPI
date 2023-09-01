# Practice API Call
# https://rapidapi.com/KegenGuyll/api/dad-jokes/

from pprint import pprint
import requests
from configs import dadjokesAPI

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
	"X-RapidAPI-Key": dadjokesAPI,
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

pprint(response.json())