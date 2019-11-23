# Create a program that checks if a given year is a leap year or not.
# A year is a leap year if it is divisible by 4. (HINT: use the modulo operator)
# A year is NOT a leap year if it is divisible by 100.
# A year is a leap year if it is divisible by 400. This rule takes precedence over the above rule.

# DO NOT EDIT THE FOLLOWING LINE
if __name__ == "__main__":
    year = int(input("Which year do you want to check for a common or leap year?:\n"))

isLeapYear = False

if(year % 400 == 0):
    isLeapYear = True
else:
    if(year % 4 == 0 and year % 100 != 0):
        isLeapYear = True

if(isLeapYear):
    print(str(year) + " is a leap year!")
else:
    print(str(year) + " is a common year!")
