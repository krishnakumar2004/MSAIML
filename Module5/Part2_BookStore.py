# get integer input from user for no on books purchased this month
# create and initialize variable to store points awarded
# create one if condition to start with checking highest count of books
# create expression to check greater than equal to 8
# create 4 else if condition each to check for equality condition 6,4,2,0
# inside conditions assign awarded points to variable already created
# print in format to show books count and points awarded
noOfBooks = int(input("Enter No of books purchased this month \n"))
pointsAwarded = 0
if (noOfBooks >= 8) :
    pointsAwarded = 60
elif (noOfBooks == 6) :
    pointsAwarded = 30
elif (noOfBooks == 4) :
    pointsAwarded = 15
elif (noOfBooks == 2):
    pointsAwarded = 5
elif (noOfBooks == 0) :
    pointsAwarded = 0

print("customer purchases {} books, they awarded {} points.".format(noOfBooks,pointsAwarded))
