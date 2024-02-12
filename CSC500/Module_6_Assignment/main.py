import random


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
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $' + str(self.total_price))


class ShoppingCart:

    customer_name = None
    current_date = 'January 1, 2020'
    cart_items = []

    #TODO:  Implement customer name and date
    def __init__(self, customer_name = None, current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date

    '''
            Adds an item to cart_items list. 
            input:  ItemToPurchase
    '''
    def add_item(self, item : ItemToPurchase):

        self.cart_items.append(item)
        print(str(item.item_quantity) + ' ' + item.item_name + ' added to the cart.')
    
    '''
        Removes item from cart_items list.
        input: item_name
    '''
    def remove_item(self, item_name):
        print('Will be implemented in a later iteration!')
    
    '''
        Modifies an item's description, price, and/or quantity.
        input: ItemToPurchase
    '''
    def modify_item(self, item : ItemToPurchase):
        print('Will be implemented in a later iteration!')

    '''
        Returns the quantity of all items in cart
        output: Quantity of items in cart
    '''
    def get_num_items_in_cart(self):
        print('Will be implemented in a later iteration!')
    
    '''
        Gets the total cost of items in the cart
        output: Returns cost of all items in cart
    '''
    def get_cost_of_cart(self):
        print('Will be implemented in a later iteration!')
    
    '''
        Print total of objects in cart
    '''
    def print_total(self):
        num_items = 0
        total = 0
        print('\nSHOPPING CART')
        print(self.customer_name + '\'s Shopping Cart - ' + self.current_date)

        for item in self.cart_items:
            item.total_price = round(float(item.item_price * item.item_quantity), 2)
            num_items += item.item_quantity
            total += item.total_price
            item.print_item_cost()

        if num_items == 0:
            print('SHOPPING CART IS EMPTY.')
        else:
            print('Number of items: ' + str(num_items))
            print('Total Cost: $' + str(total))

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

def main():

    good_bye = ['Live long and prosper.', \
               'May the force be with you.', \
               'Adventure is out there.', \
               'Please subscribe and smash that like button.', \
               'Fare thee well.', \
               'Big Brother is watching.']
    running = True

    #TODO:  Implement prompt for customer name and date
    shopping_cart = ShoppingCart('Test User')

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
        #TODO:  Implement removing an item
        elif action == 'r':
            print('You have chosen to remove an item from the cart.')
            shopping_cart.remove_item(None)
        #TODO:  Implement modifying item quantity
        elif action == 'c':
            print('You have chosen to change an item quantity the cart.')
            shopping_cart.modify_item(None)
        #TODO:  Implement printing item descriptions in cart.
        elif action == 'i':
            print('You have chosen to print the descriptions of the items in the cart.')
            shopping_cart.print_descriptions()
        #TODO:  Implement outputting the shopping cart
        elif action == 'o':
            print('You have chosen to output the items in the cart.')
            shopping_cart.print_total()

    print('\n\n' + random.choice(good_bye) + '\n\n')
    exit

if __name__ == "__main__":
    main()