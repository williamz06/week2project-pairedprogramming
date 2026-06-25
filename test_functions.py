import unittest
import sqlalchemy as db
import database
from database import store_events
from eventfinder import find_events
from unittest.mock import patch
from genai_API import build_prompt

database.engine = db.create_engine("sqlite:///:memory:")

class TestFunctions(unittest.TestCase):
    def test_store_events(self):
        with database.engine.connect() as connection:
            connection.execute(db.text("""
                CREATE TABLE IF NOT EXISTS event(
                    id TEXT PRIMARY KEY, name, url, date, venue, city)
            """))
            connection.commit()
        
        example_events = [
            {'id': 'k7vGF_k525ulu', 'name': 'Museum of Chinese in America', 
            'url': 'https://www.universe.com/events/museum-of-chinese-in-america-tickets-PZ7R68', 
            'date': '2026-03-04', 'venue': 'Museum of Chinese in America', 'city': 'New York'}
        ]

        store_events(example_events)

        with database.engine.connect() as connection: 
            row = connection.execute(db.text("SELECT id, name, url, date, venue, city FROM event")).fetchall()
        
        self.assertEqual(row[0], ('k7vGF_k525ulu', 'Museum of Chinese in America', 
            'https://www.universe.com/events/museum-of-chinese-in-america-tickets-PZ7R68', 
            '2026-03-04', 'Museum of Chinese in America', 'New York'))

    @patch('eventfinder.requests.get')
    def test_find_events(self, mock_get):
        example_json = {
                    '_embedded': {
                        'events': [
                            {
                                'id': 'rZ7HnEZ1AfPZbN',
                                'name': 'NoFun FestPass',
                                'url': 'https://www.ticketweb.com/event/nofun-festpass-berlin-tickets/14940623',
                                'dates': {'start': {'localDate': '2026-06-01'}},
                                '_embedded': {
                                    'venues': [{'name': 'Berlin', 'city': {'name': 'New York'}}]
                                }
                            }
                        ]
                    }
                }
        mock_get.return_value.json.return_value = example_json
        self.assertEqual(find_events("New York", "")[0], {
            'id': 'rZ7HnEZ1AfPZbN',
            'name': 'NoFun FestPass',
            'url': 'https://www.ticketweb.com/event/nofun-festpass-berlin-tickets/14940623',
            'date': '2026-06-01',
            'venue': 'Berlin',
            'city': 'New York'
            })

        

    def test_build_prompt(self):
        example_events = [('k7vGF_k525ulu', 'Museum of Chinese in America', 
            'https://www.universe.com/events/museum-of-chinese-in-america-tickets-PZ7R68', 
            '2026-03-04', 'Museum of Chinese in America', 'New York')]
        user_interests = "all"
        texts = f"""
                Event 1:
                - Name: Museum of Chinese in America
                - date: 2026-03-04
                - venue: Museum of Chinese in America
                - city: New York
                - URL: https://www.universe.com/events/museum-of-chinese-in-america-tickets-PZ7R68
                """
        prompt = f"""You are an event recommendation assistant. The user is interested in: {user_interests}. Below is a list of upcoming events. Please: 
                1. rank the events from most to least relevant based on the user's interests. 
                2. for each event give a short 1 sentence explanation of why you recommended it
                3. Please format your response cleanly using a numbered list.

                Events: {texts}
               """
        self.assertEqual(build_prompt(example_events, user_interests), prompt)