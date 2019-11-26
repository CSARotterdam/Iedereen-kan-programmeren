x = 9 ** 0.5
y = 8 * x
z = 6 * 4

#Keyword(s): if, elif, else
#Uitgevoerd: Ja
#Conditie variabele(n): y
#Conditie: y > 20
#Conditie uitkomst: True
#Uitgevoerd pad(en): 1
if(y > 20):
    print("Pad 1.")
    #Uitgevoerd: Nee
    #Conditie variabele(n): z,y
    #Conditie: z == y
    #Conditie uitkomst: True
elif(z == y):
    print("Pad 2.")
else:
    print("Pad 3.")
