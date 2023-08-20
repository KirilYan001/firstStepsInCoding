food_in_kg = int(input())
food_in_g = food_in_kg * 1000

eaten_food = 0

while True:
    command = input()

    if command == 'Adopted':
        break
    command = int(command)
    eaten_food += command

leftover = food_in_g - eaten_food

if leftover >= 0:
    print(f"Food is enough! Leftovers: {leftover} grams.")
else:
    print(f"Food is not enough. You need {abs(leftover)} grams more.")
