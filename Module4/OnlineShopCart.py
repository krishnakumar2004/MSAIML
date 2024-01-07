class ItemToPurchase :

    def __init__(self):
        item_name = 'none'
        item_price = float(0)
        item_quantity = 0

    def print_item_cost(self,total):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, total))

itemToPurchase1 = ItemToPurchase()
itemToPurchase1.item_name = input('Enter the item name:')
itemToPurchase1.item_price = float(input('Enter the item price:'))
itemToPurchase1.item_quantity = int(input('Enter the item quantity:'))

itemToPurchase2 = ItemToPurchase()
itemToPurchase2.item_name = input('Enter the item name:')
itemToPurchase2.item_price = float(input('Enter the item price:'))
itemToPurchase2.item_quantity = int(input('Enter the item quantity:'))

print('TOTAL COST')
total1 = itemToPurchase1.item_price * itemToPurchase1.item_quantity
total2 = itemToPurchase2.item_price * itemToPurchase2.item_quantity
itemToPurchase1.print_item_cost(total1)
itemToPurchase2.print_item_cost(total2)
print('Total: ${}'.format(total1 + total2))