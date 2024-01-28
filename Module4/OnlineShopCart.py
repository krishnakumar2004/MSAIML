class ItemToPurchase :
    def __init__(self):
        item_name = 'none'
        item_description = 'none'
        item_price = float(0)
        item_quantity = 0
        total_cost = 0
    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, self.item_price * self.item_quantity))

    def cal_item_cost(self):
        return self.item_price * self.item_quantity

listOfItemToPurchase = []
dictionaryOfTotal = {"total":0}

for i in range(2) :
    itemToPurchase1 = ItemToPurchase()
    itemToPurchase1.item_name = input('Enter the item name:')
    itemToPurchase1.item_price = float(input('Enter the item price:'))
    itemToPurchase1.item_quantity = int(input('Enter the item quantity:'))
    itemToPurchase1.total_cost = itemToPurchase1.cal_item_cost()
    listOfItemToPurchase.append(itemToPurchase1)
    dictionaryOfTotal["total"] = dictionaryOfTotal["total"] + (itemToPurchase1.item_price * itemToPurchase1.item_quantity)

print('TOTAL COST')
for itemToPurchase in listOfItemToPurchase :
    itemToPurchase.print_item_cost()
print('Total: ${}'.format(dictionaryOfTotal["total"]))