# create shopping cart app with add, modify, remove functionality
# create 2 classes itemtopurchase and shoppingCart
# create 2 functions in itemtopurchase to print and calculate cost
# create 5 functions in shoppingCart class for add,remove,change,print,menu
# use try except when there is calculations involved
class ItemToPurchase :
    def __init__(self,name = 'none',desc= 'none',price= float(0),qnt = 0,total = 0):
        self.item_name = name
        self.item_description = desc
        self.item_price = price
        self.item_quantity = qnt
        self.total_cost = total
    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, self.item_price * self.item_quantity))

    def cal_item_cost(self):
        try :
            return self.item_price * self.item_quantity
        except :
            print("Error happen in calculate item cost")

class ShoppingCart :
    def __init__(self, name = "none", date= "January 1,2020"):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, itemToPurchase):
        itemToPurchase.item_name = input('Enter the item name:')
        itemToPurchase.item_description = input('Enter the item description:')
        itemToPurchase.item_price = float(input('Enter the item price:'))
        itemToPurchase.item_quantity = int(input('Enter the item quantity:'))
        try :
            itemToPurchase.total_cost = itemToPurchase.item_price * itemToPurchase.item_quantity
        except :
            print("Calculation error in ADD Item")
        self.cart_items.append(itemToPurchase)

    def remove_item(self,itemsName) :
        try:
            items_length = len(self.cart_items)
            for itemToPur in self.cart_items:
                if itemToPur.item_name == itemsName:
                    self.cart_items.remove(itemToPur)
            if (items_length == len(self.cart_items)) :
                print('Item not found in cart. Nothing removed.')
        except ValueError as ve :
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, itemToPurchase) :
        for itemToPur in self.cart_items:
            if itemToPur.item_name == itemToPurchase.item_name :
                if (itemToPurchase.item_description !='none' or itemToPurchase.item_price != float(0) or itemToPurchase.item_quantity != 0) :
                    try :
                        self.cart_items.remove(itemToPur)
                        itemToPur.item_quantity = itemToPurchase.item_quantity
                        itemToPur.total_cost = itemToPur.item_price * itemToPur.item_quantity
                        self.cart_items.append(itemToPur)
                    except :
                        print("Error happen in modify item")
            else :
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self) :
        total_quantity = 0
        for itemToPur in self.cart_items :
            try :
                total_quantity = total_quantity + itemToPur.item_quantity
            except :
                print("Error happen calculate no of items")
        return total_quantity

    def get_cost_of_cart(self) :
        total_cost = 0
        for itemToPur in self.cart_items:
            total_cost = total_cost + itemToPur.total_cost
        return total_cost

    def print_total(self) :
        if (len(self.cart_items) == 0) :
            print("SHOPPING CART IS EMPTY")
        else :
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            for itemToPur in self.cart_items:
                print("{} {} @ ${} = {}".format(itemToPur.item_name,itemToPur.item_quantity,itemToPur.item_price, itemToPur.total_cost))
            print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self) :
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Items Descriptions")
        for itemToPur in self.cart_items:
            print("{} : {}".format(itemToPur.item_name, itemToPur.item_description))

def print_menu(ShoppingCart) :
    menu = ("      MENU \n"
            "   a - Add item to cart \n"
            "r - Remove item from cart \n"
            "  c - Change item quantity \n"
            "i - Output items' descriptions \n"
            "   o - Output shopping cart \n"
            "         q - Quit\n"
            "   Choose an option: \n")
    menu_input = input(menu)
    print(menu_input)
    return menu_input

try :
    cust_name = input("Enter customer's name:\n")
    today_date = input("Enter today's date:\n")
    shoppingCart1 = ShoppingCart(cust_name, today_date)
    print("Customer name: {}".format(shoppingCart1.customer_name))
    print("Today's date: {}".format(shoppingCart1.current_date))

    while(True) :
        menu_input = print_menu(shoppingCart1)
        if menu_input == 'o' :
            print("OUTPUT SHOPPING CART")
            shoppingCart1.print_total()
        elif menu_input == 'i' :
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shoppingCart1.print_descriptions()
        elif menu_input == 'a' :
            print("ADD ITEM TO CART")
            itemToPurchase = ItemToPurchase()
            shoppingCart1.add_item(itemToPurchase)
        elif menu_input == 'r' :
            print("REMOVE ITEM FROM CART")
            itemToRemove = input("Enter name of item to remove:\n")
            shoppingCart1.remove_item(itemToRemove)
        elif menu_input == 'c' :
            print("CHANGE ITEM QUANTITY")
            itemToPurchase = ItemToPurchase()
            itemToPurchase.item_name = input("Enter the item name:\n")
            itemToPurchase.item_quantity = int(input("Enter the new quantity:\n"))
            shoppingCart1.modify_item(itemToPurchase)
        else :
            break
except :
    print("Error occured in main block")