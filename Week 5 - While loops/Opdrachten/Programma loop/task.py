def programLoop():
    active = True
    while(active):
        print("This loop will continue forever unless you stop it")
        userInput = input("Do you want to continue? [y/n]\n")
        if(userInput == "n"):
            print("quiting")
            active = False
        elif(userInput == "y"):
            print("continuing")
            continue
        else:
            print("Please enter \"y\" or \"n\"")


programLoop()
