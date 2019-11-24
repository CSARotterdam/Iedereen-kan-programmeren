emptyArray = []

integerArray = [1, 2, 3]

stringArray = ["1", "2", "3"]

arrayOfArrays = [emptyArray, integerArray, stringArray]

emptyArray.append("first")
#Variabele naam: emptyArray
#Variabele waarde: ["first"]
#Variabele type: list

emptyArray.append("second")
#Variabele naam: emptyArray
#Variabele waarde: ["first", "second"]
#Variabele type: list

integerArray.append(1)
#Variabele naam: integerArray
#Variabele waarde: [1, 2, 3, 1]
#Variabele type: list

stringArray.append("4")
#Variabele naam: stringArray
#Variabele waarde: ["1", "2", "3", "4"]
#Variabele type: list

# The insert function inserts the value of the second argument
# at the index specified by the first argument
integerArray.insert(0, 13)
#Variabele naam: integerArray
#Variabele waarde: [13, 1, 2, 3, 1]
#Variabele type: list
