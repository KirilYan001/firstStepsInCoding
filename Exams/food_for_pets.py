count_of_days = int(input())
total_food = float(input())
iteration = 0
eaten_food_dog = 0
eaten_food_cat = 0
cookies = 0

for _ in range(count_of_days):
    iteration += 1
    dog_food = int(input())
    cat_food = int(input())

    eaten_food_dog += dog_food
    eaten_food_cat += cat_food

    if iteration % 3 == 0:
        current_cookies = (dog_food + cat_food) * 0.10
        cookies += current_cookies

percent_for_eaten_fod = eaten_food_dog + eaten_food_cat
percent_total = (percent_for_eaten_fod / total_food) * 100
percent_dog_food = (eaten_food_dog / percent_for_eaten_fod) * 100
percent_cat_food = (eaten_food_cat / percent_for_eaten_fod) * 100

print(f"Total eaten biscuits: {cookies:.0f}gr.\n"
      f"{percent_total:.2f}% of the food has been eaten.\n"
      f"{percent_dog_food:.2f}% eaten from the dog.\n"
      f"{percent_cat_food:.2f}% eaten from the cat.\n")
