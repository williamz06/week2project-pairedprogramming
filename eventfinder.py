import requests
import os


API_KEY = os.environ.get('TICKETMASTER_API_KEY')


URL = 'https://app.ticketmaster.com/discovery/v2/events.json'

city = input('Enter city: ')
keyword = input('Enter keyword (or press Enter to skip): ')

params = {
   'apikey': API_KEY,
   'city': city,
   'keyword': keyword,
   'sort': 'date,asc',
   'size': 20 # <--  number of results, we can up the number if wanted
}


response = requests.get(URL, params=params)
data = response.json()

events = data['_embedded']['events']

print(f'\n20 Upcoming Events in {city}:')
print('-' * 40)

for event in events:
   name = event['name']
   date = event['dates']['start']['localDate']
   venue = event['_embedded']['venues'][0]['name']
   url = event['url']
