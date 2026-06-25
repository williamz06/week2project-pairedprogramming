import requests
import os


API_KEY = os.environ.get('TICKETMASTER_API_KEY')


URL = 'https://app.ticketmaster.com/discovery/v2/events.json'



def find_events(city, keyword):
   params = {
      'apikey': API_KEY,
      'city': city,
      'keyword': keyword,
      'sort': 'date,asc',
      'size': 20 # <--  number of results, we can up the number if wanted
   }


   response = requests.get(URL, params=params)
   data = response.json()

   if '_embedded' not in data:
      print("No events found for this specifc response, sorry!")
      return [data['_embedded']['events']]


   events = data['_embedded']['events']

   event_list = []

   print(f'\n20 Upcoming Events in {city}:')
   print('-' * 60)

   for event in events:
      name = event['name']
      date = event['dates']['start']['localDate']
      venue = event['_embedded']['venues'][0]['name']
      url = event['url']
      event_id = event['id']
      city_name = event['_embedded']['venues'][0]['city']['name']

      print(f'Event: {name}')
      print(f'Date: {date}')
      print(f'Venue: {venue}')
      print(f'Tickets: {url}')
      print('-' * 40)

      event_list.append({
         'id': event_id,
         'name': name,
         'url' : url,
         'date' : date,
         'venue': venue,
         'city': city_name
      })
   return event_list
