#Iterator: x
#Iterable: range(10)
#Aantal iteraties: 10
#Eerste waarde van iterator: 0
#Laatste waarde van iterator: 9
for x in range(10):
    #Iterator: y
    #Iterable: range(5)
    #Aantal iteraties: 5
    #Eerste waarde van iterator: 0
    #Laatste waarde van iterator: 4
    #Aantal keer uitgevoerd: 50
    for y in range(5):
        #Iterator: z
        #Iterable: range(3)
        #Aantal iteraties: 3
        #Eerste waarde van iterator: 0
        #Laatste waarde van iterator: 2
        #Aantal keer uitgevoerd: 150
        for z in range(3):
            print(x,y,z)
