import random

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
              \n 1) Rainfall calculator\
              \n 2) Reward points calculator')
        user_input = input('\nEnter Selection (1 or 2): ')
        if user_input in responses:
            break
        else:
            print("\nSorry that is not a valid option.")

    if user_input == '1':
        print("You have chosen the rainfall calculator.")
    else:
        print("You have chosen the reward points calculator.")

    return user_input


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
    Calculate the average rainfall per month given the entire period
'''
def calculate_rainfall():
    valid_year = False
    num_months = 0
    total_rainfall = 0

    while not valid_year:
        try:
            years = int(input('Enter number of years: '))
            valid_year = True
        except ValueError:
            print("\nSorry that input is not valid.")
            continue

    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']

    for x in range(years):
        for month in months:
            valid_month = False
            while not valid_month:
                try:
                    rainfall = float(input('Please enter rainfall amount in inches for ' + month + ': '))
                    total_rainfall = total_rainfall + rainfall
                    num_months += 1
                    valid_month = True
                except ValueError:
                    print("\nSorry that input is not valid.")
                    continue
    
    print('\n\n================================================\n\n')
    print('Number of years: ' + str(years))
    print('Number of months: ' + str(num_months))
    print('Total rainfall: ' + str(total_rainfall))
    print('Average rainfall: ' + str(round(total_rainfall/num_months, 2)))
    print('\n\n================================================\n\n')


'''
    Calculate the number of reward points for books purchased for the month
'''
def calculate_rewards():
    valid_books = False

    while not valid_books:
        try:
            num_books = int(input('Enter number of books: '))
            valid_books = True
        except ValueError:
            print("\nSorry that input is not valid.")
            continue   

    reward_points = 0
    if num_books < 2:
        reward_points = 0
    elif num_books < 4 and num_books >= 2:
        reward_points = 5
    elif num_books < 6 and num_books >= 4:
        reward_points = 15
    elif num_books < 8 and num_books >= 6:
        reward_points = 30
    elif num_books >= 8:
        reward_points = 60

    print('\n\n================================================\n\n')
    print('Number of books purchased for the month: ' + str(num_books))
    print(str(num_books) + ' books earns ' + str(reward_points) + ' points.')

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
            calculate_rainfall()
        elif choice == '2':
            calculate_rewards()
        
        keep_running = run_again()
        if keep_running == 'y':
            continue
        else:
            break

    print('\n\n' + random.choice(good_bye) + '\n\n')
    exit

if __name__ == "__main__":
    main()