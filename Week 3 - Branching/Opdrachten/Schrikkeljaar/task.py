isLeapYear = False
year = int(input("Which year do you want to check for a common or leap year?:\n"))


if(year % 400 == 0):
    isLeapYear = True
else:
    if(year % 4 == 0 and year % 100 != 0):
        isLeapYear = True

if(isLeapYear):
    print(str(year) + " is a leap year!")
else:
    print(str(year) + " is a common year!")
