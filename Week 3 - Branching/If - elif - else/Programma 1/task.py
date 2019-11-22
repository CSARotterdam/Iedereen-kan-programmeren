x = 70/4
y = 80/5
z = 90/6

#Keyword(s): if, elif, else
#Uitgevoerd: Ja
#Conditie variabele(n): x,y,z
#Conditie: x >= y and x >= z
#Conditie uitkomst: True
#Uitgevoerd pad(en): 1
if(x >= y and x >= z):
    print("Pad 1.")
#Uitgevoerd: Nee
#Conditie variabele(n): x,y,z
#Conditie: y >= x and y >= z
#Conditie uitkomst: False
elif(y >= x and y >=z):
    print("Pad 2.")
else:
    print("Pad 3.")
