#calculating the week years and month 
# taking the input of no days

days=int(input("enter the number of days"))
#calculating the years 
years= days//365
print( "years",years)
remaining_days=days%365
print( "days",remaining_days)
weeks=remaining_days//7
print("weeks",weeks)