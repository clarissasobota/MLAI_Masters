
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
        print('\nEnter Selection (1 or 2): ')
        user_input = input()
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
    Prompt for number.  Validate for integer value.

    Input: 
        order: The string value of the order of the number to be entered
    Output:
        user_input: Number entered by user.
'''
def get_number(order):
    valid = False

    while not valid:
        print("\nPlease enter " + order + " whole number: ")
        try:
            user_input = int(input())
            return user_input
        except ValueError:
            print("\nSorry that is not valid.  Please enter a whole number.")
            continue

'''
    Prompts user if they want to run the program again
'''
def run_again():
    valid = False
    responses = ['y','n']

    while not valid:
        print('\n\nDo you want to run program again? (y/n): ')
        user_input = input().lower()

        if user_input not in responses:
            print("\nSorry that is not a valid option.")
        else:
            return user_input