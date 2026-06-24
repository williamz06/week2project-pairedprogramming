import sqlalchemy as db

engine = db.create_engine("sqlite:///eventcache.db")

def store_events(events):
    with engine.connect() as connection:
        connection.execute(db.text("""
                CREATE TABLE IF NOT EXISTS event(
                    id TEXT PRIMARY KEY, name, url, date, venue
                )
            """))
        connection.commit()

        for event in events:
            event_id = event["id"]
            name = event["name"]
            url = event["url"]
            date = event["date"]
            venue = event["venue"]
            city = event["city"]

            connection.execute(db.text("INSERT OR REPLACE INTO event VALUES (:id, :name, :url, :date, :venue, :city)"),
                    {"id": event_id, "name": name, "url": url, "date": date, "venue": venue, "city": city})
        connection.commit()
