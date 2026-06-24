from database import store_events
from eventfinder import find_events
from genai_API import get_recommendation

def main():
    city = input('Enter city: ')
    keyword = input('Enter keyword (or press Enter to skip): ')
    events = find_events(city, keyword)
    store_events(events)
    recommendation = get_recommendation()
    print(recommendation)

if __name__ == "__main__":
    main()
