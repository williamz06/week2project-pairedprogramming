import os 
from google import genai
from google.genai import types
import sqlalchemy as db
from eventfinder import keyword


# Set environment variables
my_api_key = os.getenv('GENAI_KEY')

genai.api_key = my_api_key

client = genai.Client(api_key=os.getenv('GENAI_KEY'))
engine = db.create_engine("sqlite:///eventcache.db")

def get_events_from_db():
    with engine.connect() as connection:
        rows = connection.execute(db.text("SELECT event_id, name, url, date, venue FROM eventcache"))
    return rows

