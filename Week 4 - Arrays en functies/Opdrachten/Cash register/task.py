products = [["Apple", 2], ["Bread", 1], ["Melon", 3]]
amounts = [0, 0, 0]

amounts[0] = int(input("How much "+products[0][0]+ " would you like?\n"))
amounts[1] = int(input("How much "+products[1][0]+ " would you like?\n"))
amounts[2] = int(input("How much "+products[0][0]+ " would you like?\n"))

total = products[0][1] * amounts[0] + products[1][1] * amounts[1] + products[2][1] * amounts[2]

print("You have to pay: "+ str(total))
