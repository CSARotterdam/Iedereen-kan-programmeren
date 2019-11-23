import random

# Create a program that checks if the number the user put in is higher or lower than
# a randomly generated number.

# The inputted number may not be below 0, nor may it be above 100.
# DO NOT EDIT THE FOLLOWING LINE
if __name__ == "__main__":
    number = int(input("Enter a number:\n"))
    randomNumber = random.randint(0, 100)
    print("The random number is: " + str(randomNumber))

if(number < 0):
    print("No negative numbers!")
elif(number < randomNumber):
    print("The number is below the random number.")
elif(number == randomNumber):
    print("The number is equal to the random number!")
elif(number > randomNumber and number <= 100):
    print("The number is above the random number.")
else:
    print("No numbers higher than 100!")
