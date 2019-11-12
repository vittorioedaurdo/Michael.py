# Review MathsIsFun: Leap Years. Create a program 
# that asks the user for a year, and then calculate 
# whether or not the given year is a leap year. Build an 
# array where each entry is the number of days in the corresponding month 
# (January = 31, February = 28 or 29 depending on year, March = 31, etc.).
# Build a parallel string array with the names of each month. Then ask the 
# user to enter a month number, and look up the corresponding month name 
# and number of days and display the information. Continue accepting 
# input and displaying results until the user enters a number less than 1 
# or greater than 12.[2]
 
def main():
    print("\t\t\t____________________\n") 
    print("\t\t\tIs this a leap year?")
    print("\t\t\t____________________\n")
    year = int(input("Enter year : "))
    name_month = str(input("Enter the name of the month (January, February, March...) : "))
    leap_year(year)
    days_in_month(name_month,year)
    

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    elif year % 400 == 0:
        print(year, "is a Leap Year")
    elif year % 100 == 0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")

def month_number():
    get_month = str(input())
    return get_month
    
def month(get_month):
    if get_month == 1:
        print("January")
    elif get_month == 2:
        print('February')
    elif get_month == 3:
        print("March")
    elif get_month == 4:
        print("April")
    elif get_month == 5:
        print("May")
    elif get_month == 6:
        print("June")
    elif get_month == 7:
        print("July")
    elif get_month == 8:
        print("August")
    elif get_month == 9:
        print("September")
    elif get_month == 10:
        print("October")
    elif get_month == 11:
        print("November")
    elif get_month == 12:
        print("December")
    else:
        print ("Game Over")

def days_in_month(name_month,year):
    if name_month in ['January','March', 'May', 'July', 'August','October','December']:
        print ("31 days has this month")
    elif name_month in ['April','June','September','November']:
        print ("30 days has this month")
    elif name_month == 'February' and leap_year(year) == True:
        print ("29 days has this month")
        # doesn't display
    elif name_month == 'February' and leap_year(year) == False:
        print ("28 days has this month")
        # doesn't display
    else:
        return None

main()

while True:
    get_month = int(input("Enter month number (between 1 and 12) : "))
    if not(0<get_month<13): break
    month(get_month)

# instructor's notes:
# It is not displaying the number of days in the month. 
# The leap year calculation is also incorrect.