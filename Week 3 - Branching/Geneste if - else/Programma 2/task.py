x = 21/3
y = x/3 * 4
z = 24
#Keyword(s): if, else
#Uitgevoerd: Ja
#Conditie variabele(n): z
#Conditie: x < 15
#Conditie uitkomst: True
#Uitgevoerd pad: 1
if(z > 20):
    print("Pad 1.")
    #Keyword(s): if, else
    #Uitgevoerd: Ja
    #Conditie variabele(n): y
    #Conditie: 10 >= y
    #Conditie uitkomst: False
    #Uitgevoerd pad: 2
    if(5 <= y):
        print("Pad 2.")
        #Keyword(s): if, else
        #Uitgevoerd: JA
        #Conditie variabele(n): x, y
        #Conditie: 10 >= y
        #Conditie uitkomst: False
        #Uitgevoerd pad: 4
        if(50 >= x * y):
            print("Pad 3.")
        else:
            print("Pad 4.")
    else:
        print("Pad 5.")
else:
    print("Pad 6.")
print("Einde programma.")
