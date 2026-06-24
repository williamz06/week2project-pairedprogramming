import os 
from google import genai
from google.genai import types
import sqlalchemy as db
from eventfinder import keyword


my_api_key = os.getenv('GENAI_KEY')

genai.api_key = my_api_key

client = genai.Client(api_key=os.getenv('GENAI_KEY'))
engine = db.create_engine("sqlite:///eventcache.db")

def get_events_from_db():
    with engine.connect() as connection:
        rows = connection.execute(db.text("SELECT event_id, name, url, date, venue FROM eventcache")).fetchall()
    return rows

def build_prompt(events, user_interests):
    texts = ""
    for i, event in enumerate(events, 1):
        event_id, name, url, date, venue = event
        texts += f"""
                Event {i}:
                - Name: {name}
                - date: {date}
                - venue: {venue}
                - URL: {url}
                """
    
    prompt = f"""You are an event recommendation assistant. The user is interested in: {user_interests}. Below is a list of upcoming events. Please: 
                1. rank the events from most to least relevant based on the user's interests. 
                2. for each event give a short 1 sentence explanation of why you recommended it
                3. Please format your response cleanly using a numbered list.

                Events: {texts}
               """
    return prompt

def get_recommendation():
    events = get_events_from_db()
    user_interests = keyword

    prompt = build_prompt(events, user_interests)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text



print(get_recommendation())