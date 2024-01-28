class ItemToPurchase :
    def __init__(self):
        item_name = 'none'
        item_description = 'none'
        item_price = float(0)
        item_quantity = 0
        total_cost = 0
    def __init__(self,name,desc,price,qnt,total):
        self.item_name = name
        self.item_description = desc
        self.item_price = price
        self.item_quantity = qnt
        self.total_cost = total
    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, self.item_price * self.item_quantity))

    def cal_item_cost(self):
        return self.item_price * self.item_quantity

class ShoppingCart :
    def __init__(self):
        customer_name = "none"
        current_date = "January 1,2020"
        cart_items = []

    def __init__(self, name , date):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self,itemsName) :
        try:
            self.cart_items.remove(itemsName)
        except ValueError as ve :
            return 'Item not found in cart. Nothing removed.'

    def modify_item(self, itemToPurchase) :
        for itemToPur in self.cart_items:
            if itemToPur.item_name == itemToPurchase.item_name :
                if (itemToPurchase.item_description !='none' or itemToPurchase.item_price != float(0) or itemToPurchase.item_quantity != 0) :
                    self.cart_items.remove(itemToPur)
                    self.cart_items.append(itemToPurchase)
            else :
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self) :
        total_quantity = 0
        for itemToPur in self.cart_items :
            total_quantity = total_quantity + itemToPur.item_quantity
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

while(True) :
    shoppingCart1 = ShoppingCart("John Doe", "February 1,2020")
    itemToPurchase1 = ItemToPurchase("Nike Romaleos","Volt color, Weightlifting shoes",189,2,378)
    itemToPurchase2 = ItemToPurchase("Chocolate Chips", "Semi-sweet", 3, 5, 15)
    itemToPurchase3 = ItemToPurchase("Powerbeats 2 Headphones", "Bluetooth headphones", 128, 1, 128)
    cart_items = [itemToPurchase1,itemToPurchase2,itemToPurchase3]
    shoppingCart1.cart_items = cart_items

    menu_input = print_menu(shoppingCart1)
    if menu_input == 'o' :
        print("OUTPUT SHOPPING CART")
        shoppingCart1.print_total()
    elif menu_input == 'i' :
        print("OUTPUT ITEMS' DESCRIPTIONS")
        shoppingCart1.print_descriptions()
    else :
        break