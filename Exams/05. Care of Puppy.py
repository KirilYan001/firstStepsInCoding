food_kg = int(input())
food_grams = food_kg * 1000

total_sum_food = 0
rest_of_food = food_grams - total_sum_food

command = input()
while command != 'Adopted':
    eaten_food = int(command)
    food_grams -= eaten_food

    command = input()

if food_grams < 0:
    print(f'"Food is not enough. You need {abs(food_grams)} grams more."')
else:
    total_sum_food -= food_grams
    print(f'"Food is enough! Leftovers: {food_grams} grams."')
