players = []

players.append(["p1", 27])
players.append(["p2", 43])
players.append(["p3", 72])
players.append(["p4", 12])
players.append(["p5", 22])
players.append(["p6", 61])

loser =players[0]

for i in (range(len(players))):
    points = players[i][1]
    if(loser[1] > points):
        loser = players[i]

winner = players[0]

for player in players:
    points = player[1]
    if(winner[1] < points):
        winner = player

print(winner[0] + " is the winner with " + str(winner[1]) + " points!")
print(loser[0] + " is the loser with " + str(loser[1]) + " points...")

