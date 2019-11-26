x = 21/3
y = x/3 * 4
z = 24
#Keyword(s): if, else
#Uitgevoerd: Ja
#Conditie variabele(n): z
#Conditie: z < 20
#Conditie uitkomst: False
#Uitgevoerd pad(en): 6
if(z < 20):
    print("Pad 1.")
    #Keyword(s): if, else
    #Uitgevoerd: Nee
    #Conditie variabele(n): y
    #Conditie: 5 <= y
    #Conditie uitkomst: True
    if(5 <= y):
        print("Pad 2.")
        #Keyword(s): if, else
        #Uitgevoerd: Nee
        #Conditie variabele(n): x, y
        #Conditie: 50 >= x * y
        #Conditie uitkomst: False
        if(50 >= x * y):
            print("Pad 3.")
        else:
            print("Pad 4.")
    else:
        print("Pad 5.")
else:
    print("Pad 6.")
print("Einde programma.")
