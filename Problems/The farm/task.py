money = int(input())

if 23 <= money < 678:
    animal = " chicken"
    animal_count = money // 23
elif 678 <= money < 1296:
    animal = " goat"
    animal_count = money // 678
elif 1296 <= money < 3848:
    animal = " pig"
    animal_count = money // 1296
elif 3848 <= money < 6769:
    animal = " cow"
    animal_count = money // 3848
elif money >= 6769:
    animal = " sheep"
    animal_count = money // 6769
else:
    animal = "None"
    animal_count = 0

if animal_count > 1 and animal != " sheep":
    animal = animal + "s"
    animal_count = str(animal_count)
elif animal_count == 0:
    animal_count = ""
elif animal_count == 1 or animal == " sheep":
    animal_count = str(animal_count)

print(animal_count + animal)
