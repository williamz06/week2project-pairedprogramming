import sqlite3

def store_events(events):
    
    con = sqlite3.connect("eventcache.db")
    cur = con.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS event(
                    id TEXT PRIMARY KEY, name, url, date, venue
                )
            """)
    con.commit()

    for event in events:
        event_id = event["id"]
        name = event["name"]
        url = event["url"]
        date = event["date"]
        venue = event["venue"]

        cur.execute("INSERT OR REPLACE INTO event VALUES (?, ?, ?, ?, ?)",
                    (event_id, name, url, date, venue))

    con.commit()
    con.close() 

