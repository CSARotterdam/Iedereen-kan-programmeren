x = 4
y = 6

expressionA = 8 * 5 + 5 / 2
#Stap 1:    40 + 5 / 2
#Stap 2:    40 + 2.5
#Stap 3:    42.5
#Type  :    Float

expressionB = x * 5 + y / 2
#Stap 1:    4 * 5 + y / 2
#Stap 2:    20 + y / 2
#Stap 3:    20 + 6 / 2
#Stap 4:    20 + 3
#Stap 5:    23
#Type  :    Integer

expressionC = expressionB >= expressionA
#Stap 1:    23 >= expressionA
#Stap 2:    23 >= 42.5
#Stap 3:    False
#Type  :    Boolean

expressionD = expressionC or expressionA > 40
#Stap 1:    False or expressionA > 40
#Stap 2:    False or 42.5 > 40
#Stap 3:    False or True
#Stap 4:    True
#Type  :    Boolean

