intInput = input("Enter a number:\n")

try:
    intInput = int(intInput)
except:
    print("Please enter a number... try it once more...")
    intInput = int(input("Enter a number:\n"))

print(intInput)
