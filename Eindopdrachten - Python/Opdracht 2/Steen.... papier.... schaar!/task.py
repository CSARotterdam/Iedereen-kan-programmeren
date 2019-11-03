def run():
    p1Weapon = pickWeapon()
    p2Weapon = pickWeapon()
    winnerAndWeapon = RockPaperScissors(p1Weapon, p2Weapon)
    print("The winner is: "+winnerAndWeapon[0] +"\n With the weapon: "+ winnerAndWeapon[1])

def pickWeapon():
    print("Pick one of the following weapons (select the number):")
    print("[1] - Rock")
    print("[2] - Paper")
    print("[3] - Scissor")
    weaponNumber = input("Your choice: \n")
    if(weaponNumber == "1"):
        return "Rock"
    elif(weaponNumber == "2"):
        return "Paper"
    elif(weaponNumber == "3"):
        return "Scissor"
    else:
        return pickWeapon()

## input1: String, input2: String
## output: Array of two string elements
### example output: ["Player1", "Rock"]
def RockPaperScissors(player1Weapon, player2Weapon):
    return "Nope"

run()
