import random

people = ["Sasha", "Dima", "Kristina", "Olga", "Marina"]
random.shuffle(people)

for i in range(len(people) - 1):
    print(people[i], "is secret santa for:", people[i + 1])
print(people[-1], "is secret santa for:", people[0])
