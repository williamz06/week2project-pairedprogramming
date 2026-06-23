import requests
import os


API_KEY = os.environ.get('TICKETMASTER_API_KEY')


URL = 'https://app.ticketmaster.com/discovery/v2/events.json'


params = {
   'apikey': API_KEY,
   'city': input('Enter city: '),
   'size': 20
}


response = requests.get(URL, params=params)
data = response.json()


print(data)
