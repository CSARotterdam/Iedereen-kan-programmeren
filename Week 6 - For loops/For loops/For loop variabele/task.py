#Task 1
array1 = [1, 2, 3, 4, 5]
#Iterator: element
#Iterable: array1
#Aantal iteraties: 5
#Eerste waarde van iterator: 1
#Laatste waarde van iterator: 5
for element in array1:
    print(element)

#Task 2
string1 = "abcd"
returnString = ""
#Iterator: symbol
#Iterable: string1
#Aantal iteraties: 4
#Eerste waarde van iterator: "a"
#Laatste waarde van iterator: "d"
#Uiteindelijke waarde van returnString: "abc"
for symbol in string1:
    if(len(returnString)<3):
        returnString = returnString + symbol

#Task 3
array2 = [True, False, True, True, True, False, False, True]
counter = 0
#Iterator: boolean
#Iterable: array2
#Aantal iteraties: 8
#Eerste waarde van iterator: True
#Laatste waarde van iterator: True
#Uiteindelijke waarde van counter: 3
for boolean in array2:
    if(not(boolean)):
        counter = counter + 1
print(str(counter) + " Falses counted")
