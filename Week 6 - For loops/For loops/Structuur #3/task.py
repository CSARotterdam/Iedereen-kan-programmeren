array = [1, "string", True, 5.5, False]

#Iterator: i
#Iterable: array
#Aantal iteraties: 5
#Eerste waarde van iterator: 1
#Laatste waarde van iterator: False
for i in array:
    print(i)

#Iterator: i
#Iterable: range(len(array))
#Aantal iteraties: 5
#Eerste waarde van iterator: 0
#Laatste waarde van iterator: 4
for i in range(len(array)):
    print(i, array[i])

