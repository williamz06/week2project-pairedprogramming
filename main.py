from database import store_events
from eventfinder import find_events

def main():
    city = input('Enter city: ')
    keyword = input('Enter keyword (or press Enter to skip): ')
    events = find_events(city, keyword)
    store_events(events)

if __name__ == "__main__":
    main()
