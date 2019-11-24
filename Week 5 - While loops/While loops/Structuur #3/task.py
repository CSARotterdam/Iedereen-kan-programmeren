OuterCounter = 0
InnerCounter = 0

#Keyword: while
#Uitgevoerd: Ja
#Conditie variabele(n): OuterCounter
#Conditie: OuterCounter <= 4
#Aantal keer uitgevoerd: 5
while(OuterCounter <= 4):
    #Keyword(s): while
    #Uitgevoerd: Ja
    #Conditie variabele(n): InnerCounter
    #Conditie: InnerCounter <= 5
    #Aantal keer uitgevoerd: 30
    while(InnerCounter <= 5):
        print(InnerCounter)
        InnerCounter = InnerCounter + 1

    InnerCounter = 0
    OuterCounter = OuterCounter + 1

