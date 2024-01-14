# create a months variable and assign list of 12 months
# get input to be integer for no of years
# declare 2 variables to store totalmonths and totalrainfall
# create 2 nested for loops based on year and 12 months
# inside nested loop get input to be integer for inches of rainfall each month
# inside loop calculate total no of months
# inside loop calculate total rainfall in inches
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
NoOfYears = int(input("Enter No of Years to calculate average rainfall \n"))
TotalMonths = 0
TotalRainfallInches = 0
for year in range(NoOfYears) :
    for month in range(12) :
        inchesOfRain = int(input("rainfall inches for {} in year {} \n".format(months[month],year+1)))
        TotalMonths = TotalMonths + 1
        TotalRainfallInches = TotalRainfallInches + inchesOfRain
# print total months, total rainfall and average
# calculate average rainfall per month by using / operator
print("Total No Of months",TotalMonths)
print("Total Rainfall in Inches for all months",TotalRainfallInches)
print("Average rainfall per month",TotalRainfallInches/TotalMonths)