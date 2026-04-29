# 385.5.2 event MGMT System
# Imports
from datetime import datetime, date

# Allocation of memory for temporary db
events = {}

def  add_event():
    event_name = input('Enter the event name: ')
    date_input = input('Enter the event date (YYYY-MM-DD): ')

    try:
        event_date = datetime.strptime(date_input, '%Y-%m-%d').date()
    
    except ValueError:
        print('Invalid date format. Please use YYYY-MM-DD.')
        return
  
    events[event_name] = event_date

    print(f'🎉 Success. Added {event_name} to events!')

def get_event_date(tup):
    return tup[1]


def list_events():
    if len(events) == 0:
        print('🚨 No upcoming events 🚨')
        return
    print('\n 🌟🌟 Upcoming Events! 🌟🌟')

    sorted_events = sorted(events.items(), key=get_event_date)

    for e_name, e_date in sorted_events:
        today = date.today()
        days_remaining = (e_date - today).days

        print(f'🍾{e_name} - {e_date} - {days_remaining} days until event!!')

def delete_event():
    event_to_delete = input('Enter name of event to delete: ')

    if event_to_delete in events:
        del events[event_to_delete]
        print(f'✅ Successfully Deleted {event_to_delete}')
        return 
    else: 
        print(f'❌ Event not in database, check spelling.')  


def main():
    while True:
        print('\n 📝 Event Management System 📝')
        print('1. Add Event')
        print('2. List Events')
        print('3. Delete Event')
        print('4. Quit')

        choice = input('Enter your choice: ')

        if choice == "1":
            add_event()
        elif choice == '2':
            list_events()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            print('🛑 Program has been closed. Goodbye')
            break
        else:
            print('Invalid Option. Try again.')



# This makes sure if imported function doesnt automatically run on import
if __name__ == '__main__':
    main()