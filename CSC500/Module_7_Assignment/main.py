import random

'''
    Prompts user if they want to run the program again
'''
def run_again():
    valid = False
    responses = ['y','n']

    while not valid:
        user_input = input('\n\nDo you want to search for another course? (y/n): ').lower()

        if user_input not in responses:
            print("\nSorry that is not a valid option.")
        else:
            valid = True
            return user_input
        
'''
    Creates the dictionaries and prompts the user to enter a class
'''
def get_class_info():
    courses = ['CSC101', 'CSC102', 'CSC103', 'NET110', 'COM241']

    room_numbers = {
        'CSC101' : '3004',
        'CSC102' : '4501',
        'CSC103' : '6755',
        'NET110' : '1244',
        'COM241' : '1411'
    }

    instructors = {
        'CSC101' : 'Haynes',
        'CSC102' : 'Alvarado',
        'CSC103' : 'Rich',
        'NET110' : 'Burke',
        'COM241' : 'Lee'
    }

    meeting_time = {
        'CSC101' : '8:00 a.m.',
        'CSC102' : '9:00 a.m.',
        'CSC103' : '10:00 a.m.',
        'NET110' : '11:00 a.m.',
        'COM241' : '1:00 p.m.'
    }

    course = input('Please enter course number: ').upper()
    if course in courses:
        print('\n\n================================================\n\n')
        print('Course Number: ' + course)
        print('Course Instructor: ' + instructors[course])
        print('Room Number: ' + room_numbers[course])
        print('Meeting Time: ' + meeting_time[course])
        print('\n\n================================================\n\n')
    else:
        print('Sorry, course is not found.')



def main():
    good_bye = ['Live long and prosper.', \
               'May the force be with you.', \
               'Adventure is out there.', \
               'Please subscribe and smash that like button.', \
               'Fare thee well.', \
               'Big Brother is watching.']
    running = True

    while running:
        get_class_info()
        
        keep_running = run_again()
        if keep_running == 'y':
            continue
        else:
            break

    print('\n\n' + random.choice(good_bye) + '\n\n')
    exit 


if __name__ == '__main__':
    main()