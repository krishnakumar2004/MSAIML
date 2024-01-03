# To Calculate total price of meal
# Get food price as input and store in variable food_charge
# Create new variable Tips and store 18% of food charge
# Create new variable Sales_tax
# Calculate 7% sales tax and assign to Sales_tax
# Add all 3 variables (food_charge, Tips, Sales_tax)
# print 4 variables with format of 2 digits after decimal

# use float because price will be in 2 decimal places like 12.50
food_charge = float(input('Enter the charge for the food\n'))
Tips = food_charge * 0.18
Sales_tax = food_charge * 0.07
total_amount_meal_purchased = food_charge + Tips + Sales_tax
# in print added some space to make it readable
print('Food Price:           ${0:.2f}'.format(food_charge))
print('Tips @18 percent:     ${0:.2f}'.format(Tips))
print('Sales Tax @7 percent: ${0:.2f}'.format(Sales_tax))
print('Total Price:          ${0:.2f}'.format(total_amount_meal_purchased))