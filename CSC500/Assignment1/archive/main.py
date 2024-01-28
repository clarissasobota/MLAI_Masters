import random
import input_helper as input
import part_1 as p1
import part_2 as p2


def main():

    good_bye = ['Live long and prosper.', \
               'May the force be with you.', \
               'Adventure is out there.', \
               'Please subscribe and smash that like button.', \
               'Fare thee well.' \
               'Big Brother is watching.']
    running = True

    while running:
        selection = input.choose_operation()
        first_num = input.get_number('first')
        second_num = input.get_number('second')

        if selection == '1':
            p1.add_numbers(first_num, second_num)
            p1.subtract_numbers(first_num, second_num)
        elif selection == '2':
            p2.multiply_numbers(first_num, second_num)
            p2.divide_numbers(first_num, second_num)

        keep_running = input.run_again()
        if keep_running == 'y':
            continue
        else:
            break

    print('\n\n' + random.choice(good_bye))
    exit

if __name__ == "__main__":
    main()