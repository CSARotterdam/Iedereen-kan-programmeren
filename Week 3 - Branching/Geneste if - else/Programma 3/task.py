x = 21/3
y = x/3 * 4
z = 24
#Keyword(s): if, else
#Uitgevoerd: Ja
#Conditie variabele(n): z
#Conditie: x < 15
#Conditie uitkomst: False
#Uitgevoerd pad: 6
if(z < 20):
    print("Pad 1.")
    #Keyword(s): if, else
    #Uitgevoerd: Nee
    #Conditie variabele(n): y
    #Conditie: 10 >= y
    #Conditie uitkomst: False
    #Uitgevoerd pad: geen
    if(5 <= y):
        print("Pad 2.")
        #Keyword(s): if, else
        #Uitgevoerd: Nee
        #Conditie variabele(n): x, y
        #Conditie: 10 >= y
        #Conditie uitkomst: False
        #Uitgevoerd pad: geen
        if(50 >= x * y):
            print("Pad 3.")
        else:
            print("Pad 4.")
    else:
        print("Pad 5.")
else:
    print("Pad 6.")
print("Einde programma.")
