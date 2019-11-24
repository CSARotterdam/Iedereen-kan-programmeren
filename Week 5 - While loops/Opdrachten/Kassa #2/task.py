if __name__ == "__main__":
    products = [["Apple", 2], ["Bread", 1], ["Melon", 3]]
    amounts = [0, 0, 0]

    amounts[0] = int(input("How much " + products[0][0] + " would you like?\n"))
    amounts[1] = int(input("How much " + products[1][0] + " would you like?\n"))
    amounts[2] = int(input("How much " + products[2][0] + " would you like?\n"))

total = 0
index = 0

while(index < len(products)):
    total += products[index][1] * amounts[index]
    index = index + 1

print("You have to pay: " + str(total))
