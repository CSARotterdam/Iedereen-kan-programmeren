def programLoop():
    active = True
    while(active):
        print("Doing stuff")
        userInput = input("Do you want to continue? [y/n]\n")
        if(userInput == "n"):
            print("quiting")
            active = False
        elif(userInput == "y"):
            print("continueing")
            continue
        else:
            print("Please enter \"y\" or \"n\"")

programLoop()
