from database import store_events
from eventfinder import find_events
from genai_API import get_recommendation

def main():
    print('=' * 130)
    print("""
        ███████╗██╗   ██╗███████╗███╗   ██╗████████╗    ██╗    ██╗██╗  ██╗██╗███████╗██████╗ ███████╗██████╗ ███████╗██████╗ 
        ██╔════╝██║   ██║██╔════╝████╗  ██║╚══██╔══╝    ██║    ██║██║  ██║██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗
        █████╗  ██║   ██║█████╗  ██╔██╗ ██║   ██║       ██║ █╗ ██║███████║██║███████╗██████╔╝█████╗  ██████╔╝█████╗  ██████╔╝
        ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║       ██║███╗██║██╔══██║██║╚════██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗
        ███████╗ ╚████╔╝ ███████╗██║ ╚████║   ██║       ╚███╔███╔╝██║  ██║██║███████║██║     ███████╗██║  ██║███████╗██║  ██║
        ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝        ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                     
        """)
    print('=' * 130)

    while True:
        city = input('Enter city: ')
        keyword = input('Enter a keyword (or press Enter to skip): ')
        user_interests = input('Enter your interests: ')
        events = find_events(city, keyword)
        store_events(events)

        print('=' * 40)
        recommendation = get_recommendation(user_interests)
        print(recommendation)
        print('=' * 40)

        choice = input('\nLook for another set of events? (y to continue, anything else to quit): ')
        if choice.strip().lower() != 'y':
            print("""
                 ██████╗  ██████╗  ██████╗ ██████╗     ██████╗ ██╗   ██╗███████╗██╗
                ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗    ██╔══██╗╚██╗ ██╔╝██╔════╝██║
                ██║  ███╗██║   ██║██║   ██║██║  ██║    ██████╔╝ ╚████╔╝ █████╗  ██║
                ██║   ██║██║   ██║██║   ██║██║  ██║    ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
                ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝    ██████╔╝   ██║   ███████╗██╗
                ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝     ╚═════╝    ╚═╝   ╚══════╝╚═╝                                                      
                """)
            print('=' * 130)
            break
        print('=' * 130)

if __name__ == "__main__":
    main()
