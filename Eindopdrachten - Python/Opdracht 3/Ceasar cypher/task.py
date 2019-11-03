def run():
    toBeCyphered = input("Enter the phrase you would like to hide:\n")
    amountOfStepsToChange = int(input("Enter a number:\n"))
    returnValue = ceasarCypher(toBeCyphered, amountOfStepsToChange)
    print("Your ceasar cyphered message is:\n"+returnValue)

## Input1: String, input2: Integer
## Return: String
def ceasarCypher(stringInput, steps):
    return "Nope"

run()
