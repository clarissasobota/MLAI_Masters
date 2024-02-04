import random

class ItemToPurchase:
 
    item_name = None
    item_price = 0
    item_quantity = 0
    total_price = 0
 
    def __init__(self):
        self.item_name = None
        self.item_price = 0
        self.item_quantity = 0
        self.total_price = 0

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $' + str(self.total_price))


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
    Populate details for each item
'''
def create_item():
    item = ItemToPurchase()
    item.item_name = input('\nEnter the item name: ')

    valid_price = False
    while not valid_price:
        try:
            item.item_price = float(input("Enter the item price ($): "))
            valid_price = True
        except ValueError:
            print("\nSorry that is not a valid input.")
            continue

    valid_qty = False
    while not valid_qty:
        try:
            item.item_quantity = int(input("Enter the quantity of items (whole number): "))
            valid_qty = True
        except ValueError:
            print("\nSorry that is not a valid input.")
            continue

    item.total_price = round(float(item.item_price * item.item_quantity), 2)
    return item


def main():

    good_bye = ['Live long and prosper.', \
               'May the force be with you.', \
               'Adventure is out there.', \
               'Please subscribe and smash that like button.', \
               'Fare thee well.', \
               'Big Brother is watching.']
    running = True

    while running:
        print('\n------------Details for item one------------')
        item_1 = create_item()

        print('\n------------Details for item two------------')
        item_2 = create_item()

        total_cost = round(item_1.total_price + item_2.total_price, 2)

        print('\n\n================================================\n\n')
        print('TOTAL COST\n')
        item_1.print_item_cost()
        item_2.print_item_cost()
        print('\nTotal Cost: $' + str(total_cost))
        print('\n\n================================================')
        
        keep_running = run_again()
        if keep_running == 'y':
            continue
        else:
            break

    print('\n\n' + random.choice(good_bye) + '\n\n')
    exit

if __name__ == "__main__":
    main()