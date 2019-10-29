import random

number = int(input("Enter a number:\n"))
randomNumber = random.randint(0, 100)

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
