x = 21/3
y = x/3 * 4
z = 24
#Keyword(s): if, else
#Uitgevoerd: Ja
#Conditie variabele(n): z
#Conditie: z > 7 * 3
#Conditie uitkomst: True
#Uitgevoerd pad(en): 1,2,4
if(z > 7 * 3):
    print("Pad 1.")
    #Keyword(s): if, else
    #Uitgevoerd: Ja
    #Conditie variabele(n): y
    #Conditie: 10 <= y
    #Conditie uitkomst: True
    if(10 <= y):
        print("Pad 2.")
        #Keyword(s): if, else
        #Uitgevoerd: Ja
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
