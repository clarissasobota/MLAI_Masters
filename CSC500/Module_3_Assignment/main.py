import random

'''
    Prompts user if they want to run the program again
'''
def run_again():
    valid = False
    responses = ['y','n']

    while not valid:
        user_input = input('\n\nDo you want to run program again? (y/n): ').lower()

        if user_input not in responses:
            print("\nSorry that is not a valid option.")
        else:
            valid = True
            return user_input
        

'''
    Prompt the user to choose between Part 1 and Part 2.
    Validate that the user enters an appropriate response

    Output:  
        user_input: User operation selection
'''
def choose_operation():
    valid = False
    responses = ['1','2']
    while not valid:
        print('\nPlease one of the following operations: \
              \n 1) Restaurant calculator \
              \n 2) Alarm clock calculator')
        user_input = input('\nEnter Selection (1 or 2): ')
        if user_input in responses:
            break
        else:
            print("\nSorry that is not a valid option.")

    if user_input == '1':
        print("You have chosen the restaurant calculator.")
    else:
        print("You have chosen the alarm clock calculator.")

    return user_input


'''
    Calculates the total amount of a meal purchased at a restaurant
    Includes 18% tip and 7% sales tax
'''
def calculate_meal():
    valid = False

    while not valid:
        try:
            user_input = float(input('\nPlease enter meal amount ($): '))
            tax = round(user_input * 0.07, 2)
            tip = round(user_input * 0.18, 2)
            total = round(user_input + tax + tip, 2)

            print('\n\n================================================')
            print('\nMeal amount: $' + str(user_input))
            print('\nTax amount: $' + str(tax))
            print('\nTip amount: $' + str(tip))
            print('\nTotal amount: $' + str(total))
            print('\n\n================================================')
            valid = True
        except ValueError:
            print('\nSorry that is not valid.  Please enter a numeric value.')
            continue

'''
    Prompt for current time.  Validate for numerical value.

    Output:
        user_input: Time entered by user.
'''
def get_current_time():
    valid = False

    while not valid:
        try:
            user_input = int(input("Please enter current time (hour): "))
            if user_input >= 0 and user_input <= 24:
                return user_input
            else:
                print("\nSorry that is not a valid hour.  Please enter hour (3, 6, 15, etc)")
                continue
        except ValueError:
            print("\nSorry that is not a valid format.  Please enter hour (3, 6, 15, etc)")
            continue

'''
    Prompt for hours for alarm time.  Validate for numerical value.

    Output:
        user_input: Time entered by user.
'''
def get_alarm_time():
    valid = False

    while not valid:
        try:
            user_input = int(input("Please enter time for alarm (hour): "))
            if user_input >= 0:
                return user_input
            else:
                print("\nSorry that is not valid.  Please enter valid hour (9, 37, 152, etc)")
                continue
        except ValueError:
            print("\nSorry that is not a valid format.  Please enter hour (9, 35, 165, etc)")
            continue
        
'''
    Prompts the user for the current time and the alarm time
    Calculate the alarm time on a 24 hour clock
'''
def alarm_calculator():
    current_time = get_current_time()
    alarm_time = get_alarm_time()

    alarm_mod = alarm_time % 24
    alarm_calc = current_time + alarm_mod

    if alarm_calc > 24:
        alarm_calc = alarm_calc - 24

    print('\n\n================================================')
    print('\nCurrent time: ' + str(current_time))
    print('\nAlarm Hours: ' + str(alarm_time))
    print('\nWake Up Time: ' + str(alarm_calc))
    print('\n\n================================================')



def main():
    good_bye = ['Live long and prosper.', \
               'May the force be with you.', \
               'Adventure is out there.', \
               'Please subscribe and smash that like button.', \
               'Fare thee well.', \
               'Big Brother is watching.']
    running = True

    while running:
        choice = choose_operation()

        if choice == '1':
            calculate_meal()
        elif choice == '2':
            alarm_calculator()

        keep_running = run_again()
        if keep_running == 'y':
            continue
        else:
            break

    print('\n\n' + random.choice(good_bye) + '\n\n')
    exit

if __name__ == "__main__":
    main()