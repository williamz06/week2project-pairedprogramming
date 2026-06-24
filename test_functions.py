import unittest
import sqlalchemy as db
import database
from database import store_events

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








    def test_find_events(self):
        pass 

    def test_build_prompt(self):
        pass