import random


'''
    Prompt the user to choose between addition/subtraction and multiplication/division.
    Validate that the user enters an appropriate response

    Output:  
        user_input: User operation selection
'''
def choose_operation():
    valid = False
    responses = ['1','2']
    while not valid:
        print('\nPlease one of the following operations: \
              \n 1) Addition and Subtraction \
              \n 2) Multiplication and Division')
        user_input = input('\nEnter Selection (1 or 2): ')
        if user_input in responses:
            break
        else:
            print("\nSorry that is not a valid option.")

    if user_input == '1':
        print("You have chosen addition and subtraction.")
    else:
        print("You have chosen multiplication and division.")

    return user_input

'''
    Prompt for first number.  Validate for numerical value.

    Output:
        user_input: Number entered by user.
'''
def get_first_number():
    valid = False

    while not valid:
        try:
            user_input = float(input("Enter the First Number: ")) 
            return user_input
        except ValueError:
            print("\nSorry that is not valid.  Please enter a number.")
            continue

'''
    Prompt for second number.  Validate for numerical value.

    Output:
        user_input: Number entered by user.
'''
def get_second_number():
    valid = False

    while not valid:
        try:
            user_input = float(input("Enter the Second Number: ")) 
            return user_input
        except ValueError:
            print("\nSorry that is not valid.  Please enter a number.")
            continue

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
    Add two numbers together and print result
        Input:
            first: First number
            second: Second number

'''
def add_numbers(first,second):
    print('\n\n================================================')
    print('\nThe sum of ' + str(first) + ' and ' + str(second) + ' is: ' + str(first + second))


'''
    Subtract the two numbers and print results
'''
def subtract_numbers(first,second):
    print(str(first) + ' minus ' + str(second) + ' is: ' + str(first - second))
    print(str(second) + ' minus ' + str(first) + ' is: ' + str(second - first))
    print('\n================================================')

'''
    Multiply two numbers together and print result
        Input:
            first: First number
            second: Second number

'''
def multiply_numbers(first,second):
    print('\n\n================================================')
    print('\nThe product of ' + str(first) + ' and ' + str(second) + ' is: ' + str(first * second))


'''
    Divide the two numbers and print results
'''
def divide_numbers(first,second):
    print(str(first) + ' divided by ' + str(second) + ' is: ' + str(first / second))
    print(str(second) + ' divided by ' + str(first) + ' is: ' + str(second / first))
    print('\n================================================')

def main():

    good_bye = ['Live long and prosper.', \
               'May the force be with you.', \
               'Adventure is out there.', \
               'Please subscribe and smash that like button.', \
               'Fare thee well.', \
               'Big Brother is watching.']
    running = True

    while running:
        selection = choose_operation()
        first_num = get_first_number()
        second_num = get_second_number()

        if selection == '1':
            add_numbers(first_num, second_num)
            subtract_numbers(first_num, second_num)
        elif selection == '2':
            multiply_numbers(first_num, second_num)
            divide_numbers(first_num, second_num)

        keep_running = run_again()
        if keep_running == 'y':
            continue
        else:
            break

    print('\n\n' + random.choice(good_bye) + '\n\n')
    exit

if __name__ == "__main__":
    main()