emptyArray = []

integerArray = [1, 2, 3]

stringArray = ["1", "2", "3"]

arrayOfArrays = [emptyArray, integerArray, stringArray]

integerArray[0] = 7
a = integerArray[0]
#Variabele naam: a
#Variabele waarde: 7
#Variabele type: integer

integerArray[1] = integerArray[1] * 2
b = integerArray[1]
#Variabele naam: b
#Variabele waarde: 4
#Variabele type: integer

stringArray[2] = stringArray[2] + stringArray[0]
c = stringArray[2]
#Variabele naam: c
#Variabele waarde: "31"
#Variabele type: string

stringArray[0] = "abc"
d = stringArray[0]
#Variabele naam: d
#Variabele waarde: "abc"
#Variabele type: string
