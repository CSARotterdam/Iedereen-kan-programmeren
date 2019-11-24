x = 5
y = 10
z = "Hello, World!"


def sum(a, b):
    return a + b

a = sum(x, y)
#Functie naam: sum
#Functie input waarde(n): 5, 10
#Functie input type: integer
#Variabele naam: a
#Variabele waarde: 15
#Variabele Type: integer
print(a)

b = sum(y, x)
#Functie naam: sum
#Functie input waarde(n): 10, 5
#Functie input type: integer
#Variabele naam: b
#Variabele waarde: 15
#Variabele Type: integer
print(b)

c = str(x)
#Functie naam: str
#Functie input waarde: 5
#Functie input type: integer
#Variabele naam: c
#Variabele waarde: "5"
#Variabele Type: string
print(c)

d = sum(c, z)
#Functie naam: sum
#Functie input waarde(n): "5", "Hello, World!"
#Functie input type: string
#Variabele naam: d
#Variabele waarde: "5Hello, World!"
#Variabele Type: string
print(d)
