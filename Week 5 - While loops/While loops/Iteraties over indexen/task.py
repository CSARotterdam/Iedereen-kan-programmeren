array1 = [23, 62, 94]
array2 = [55, 45, 7]

#Task 1
index = 0
#Keyword: while
#Conditie variabele(n): index, array1
#Conditie: index < len(array1)
#Aantal keer uitgevoerd: 3
while(index < len(array1)):
    print(array1[index])
    index = index + 1

#Task 2
index = len(array1) - 1
#Keyword: while
#Conditie variabele(n): index
#Conditie: index >= 0
#Aantal keer uitgevoerd: 3
while(index>=0):
    print(array1[index])
    index = index - 1

#Task 3
#Keyword(s): if
#Conditie variabele(n): array1, array2
#Conditie: len(array1) == len(array2)
#Aantal keer uitgevoerd: 1
if(len(array1) == len(array2)):
    index = 0
    #Keyword(s): while
    #Conditie variabele(n): index, array2
    #Conditie: index < len(array2)
    #Aantal keer uitgevoerd: 3
    while(index < len(array2)):
        array2[index] = array1[index] + array2[index]
        index = index + 1
    print(array2)
