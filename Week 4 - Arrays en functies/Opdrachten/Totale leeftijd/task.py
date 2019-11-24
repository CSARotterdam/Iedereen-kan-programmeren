if __name__ == "__main__":
    persons = [["Henk", 19], ["Karel", 18], ["Jan", 22], ["Beelzebub", 21]]

person1Age = persons[0][1]
person3Name = persons[2][0]

print("person 1: " + persons[0][0] + " with age: " + str(person1Age))
print("person 2: " + persons[1][0] + " with age: " + str(persons[1][1]))
print("person 3: " + person3Name + " with age: " + str(persons[2][1]))
print("person 4: " + persons[3][0] + " with age: " + str(persons[3][1]))

print("The combined age of all persons is: " + str(persons[0][1] + persons[1][1] + persons[2][1] + persons[3][1]))
