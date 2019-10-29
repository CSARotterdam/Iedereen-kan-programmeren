#Task 1
array1 = [1, 2, 3, 4, 5]

for element in array1:
    print(element)

#Task 2
string1 = "abcd"

returnString = ""
for symbol in string1:
    if(len(returnString)<3):
        returnString = returnString + symbol

#Task 3
array2 = [True, False, True, True, True, False, False, True]
counter = 0
for boolean in array2:
    if(not(boolean)):
        counter = counter + 1
print(str(counter) + " Falses counted")
