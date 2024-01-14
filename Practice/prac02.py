for no in range(10):
    print(no**2)

class ItemToPurchase :
    def __init__(self):
        item_name = 'none'
        item_price = float(0)
        item_quantity = 0

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, self.item_price * self.item_quantity))


testDist = {}

listOfItemToPurchase = []

itemToPurchase1 = ItemToPurchase()
itemToPurchase1.item_name = input('Enter the item name:')
itemToPurchase1.item_price = float(input('Enter the item price:'))
itemToPurchase1.item_quantity = int(input('Enter the item quantity:'))

testDist["test"] = itemToPurchase1