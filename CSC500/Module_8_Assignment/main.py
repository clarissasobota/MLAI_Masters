import random
from datetime import date


class ItemToPurchase:
 
    item_name = None
    item_description = None
    item_price = 0
    item_quantity = 0
    total_price = 0
 
    def __init__(self):
        self.item_name = None
        self.item_price = 0
        self.item_quantity = 0
        self.total_price = 0
        self.item_description = None

    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + f'{self.item_price:.2f}' + ' = $' + f'{self.total_price:.2f}')


class ShoppingCart:

    customer_name = None
    current_date = 'January 1, 2020'
    cart_items = []

    def __init__(self, customer_name = None, current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date

    '''
            Adds an item to cart_items list. 
            input:  ItemToPurchase
    '''
    def add_item(self, item : ItemToPurchase):

        self.cart_items.append(item)
        print('\n' + str(item.item_quantity) + ' ' + item.item_name + ' added to the cart.')
    
    '''
        Removes item from cart_items list.
        NOTE: Changed item_name to pass in the entire item...it was way more efficient that way
        input: item_name
    '''
    def remove_item(self, item : ItemToPurchase):
        item_name = item.item_name
        self.cart_items.remove(item)
        print('\n' + item_name + ' has been removed from cart!')
    
    '''
        Modifies an item's description, price, and/or quantity.
        NOTE:  I added in a parameter called modification because in the assignment
        we only modify cost, but i wanted to give it the ability to modify everything
        input: ItemToPurchase - Item to be modified
        modification - What value to modify (cost, quantity, name description)
        index - location of the item in the cart
    '''
    def modify_item(self, item : ItemToPurchase, modification):
        valid = False

        if modification == 'cost':
            while not valid:
                try:
                    item.item_price = float(input("Enter the item price ($): "))
                    valid = True
                    break
                except ValueError:
                    print("\nSorry that is not a valid input.")
                    continue
        elif modification == 'quantity':
            while not valid:
                try:
                    item.item_quantity = int(input("Enter the quantity of items (whole number): "))
                    valid = True
                    break
                except ValueError:
                    print("\nSorry that is not a valid input.")
                    continue
        elif modification == 'description':
            print('\nCurrent description is: ' + item.item_description)
            item.item_description = input('Please enter new description: ')

        self.cart_items.append(item)
        print(item.item_name + ' ' + modification + ' has been modified.')

    '''
        Returns the quantity of all items in cart
        output: Quantity of items in cart
    '''
    def get_num_items_in_cart(self):
            num_items = 0
            for item in self.cart_items:
                num_items += item.item_quantity

            return num_items
    
    '''
        Gets the total cost of items in the cart
        output: Returns cost of all items in cart
    '''
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.total_price

        return total
    
    '''
        Print total of objects in cart
    '''
    def print_total(self):

        print('\nSHOPPING CART')
        print(self.customer_name + '\'s Shopping Cart - ' + self.current_date)

        for item in self.cart_items:
            item.total_price = round(float(item.item_price * item.item_quantity), 2)
            item.print_item_cost()

        num_items = self.get_num_items_in_cart()
        total = self.get_cost_of_cart()

        if num_items == 0:
            print('SHOPPING CART IS EMPTY.')
        else:
            print('Number of items: ' + str(num_items))
            total = self.get_cost_of_cart()
            print('Total Cost: $' + f'{total:.2f}')

    '''
        Prints each of the item's descriptions
    '''
    def print_descriptions(self):
        print('\nITEM DESCRIPTIONS')
        print(self.customer_name + '\'s Shopping Cart - ' + self.current_date)

        if not self.cart_items:
            print('SHOPPING CART IS EMPTY.')
        else:
            for item in self.cart_items:
                print(item.item_name + ' : ' + item.item_description)

'''
    Populate details for each item
'''
def create_item():
    item = ItemToPurchase()
    item.item_name = input('\nEnter the item name: ')
    item.item_description = input('Enter the item description: ')

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

'''
    Prints the menu for users to select the function for the cart
    output: Menu selection
'''
def print_menu():

    valid_choices = ['a', 'r', 'c', 'i', 'o', 'q']
    valid_choice = False

    while not valid_choice:
        print('\nPlease select an action: \
              \na - Add item to cart \
              \nr - Remove item from cart \
              \nc - Change item quantity \
              \ni - Output item\'s descriptions \
              \no - Output shopping cart \
              \nq - Quit')
        choice = input('Please choose an option: ').lower()

        if choice not in valid_choices:
            print("\nSorry that is not a valid option.")
        else:
            valid = True
            return choice
        
'''
    Prompts for the customer name and date as well as create shopping cart
'''
def create_cart():

    # No error handling for name - it can be anything
    customer_name = str(input('Please enter your name: '))

    # Will grab and format the current date
    today_date = date.today()
    current_date = today_date.strftime("%B %d, %Y")

    return ShoppingCart(customer_name, current_date)


'''
    Prints the items in the cart with an item number so user can select item by number
'''
def cart_item_select(shopping_cart : ShoppingCart):
    valid = False
    num_unique_items = len(shopping_cart.cart_items)

    while not valid:
        item_number = 1
        print('\n')
        for item in shopping_cart.cart_items:
            print('Item # ' +  str(item_number) + ' :')
            item.print_item_cost()
            item_number += 1

        response = int(input('\nPlease select an item number: '))

        if response < 1 or response > num_unique_items:
            print('Please enter a valid selection.') 
        else:
            return response - 1

def main():

    good_bye = ['Live long and prosper.', \
               'May the force be with you.', \
               'Adventure is out there.', \
               'Please subscribe and smash that like button.', \
               'Fare thee well.', \
               'Big Brother is watching.']
    running = True

    shopping_cart = create_cart()

    while running:
        action = print_menu()
        if action == 'q':
            print('You have chosen to quit.')
            running = False
            break
        elif action == 'a':
            print('You have chosen to add an item to the cart.')
            item = create_item()
            shopping_cart.add_item(item)
        elif action == 'r':
            print('You have chosen to remove an item from the cart.')
            response = cart_item_select(shopping_cart)
            shopping_cart.remove_item(shopping_cart.cart_items[response])
        elif action == 'c':
            print('You have chosen to change an item quantity the cart.')
            response = cart_item_select(shopping_cart)
            item = shopping_cart.cart_items[response]
            shopping_cart.cart_items.pop(response)
            shopping_cart.modify_item(item, 'quantity')
        elif action == 'i':
            print('You have chosen to print the descriptions of the items in the cart.')
            shopping_cart.print_descriptions()
        elif action == 'o':
            print('You have chosen to output the items in the cart.')
            shopping_cart.print_total()

    print('\n\n' + random.choice(good_bye) + '\n\n')
    exit

if __name__ == "__main__":
    main()