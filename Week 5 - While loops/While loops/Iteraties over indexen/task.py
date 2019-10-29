array1 = [23, 62, 94]
array2 = [55, 45, 7]

#Task 1
index = 0

while(index < len(array1)):
    print(array1[index])
    index = index + 1

#Task 2
index = len(array1) - 1

while(index>=0):
    print(array1[index])
    index = index - 1

#Task 3
if(len(array1) == len(array2)):
    index = 0
    while(index < len(array2)):
        array2[index] = array1[index] + array2[index]
        index = index + 1
