food_bought_kg = int(input())
food_bought_gr = food_bought_kg * 1000
food_rest = food_bought_gr

command = input()
while command != "Adopted":
    eaten_food = int(command)
    food_rest -= eaten_food

    command = input()
if command == "Adopted":
    if food_rest >=0:
        print(f"Food is enough! Leftovers: {food_rest} grams.")
    elif food_rest < 0:
        print (f"Food is not enough. You need {abs(food_rest)} grams more.")
