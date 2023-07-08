chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetable_menu_count = int(input())

price_chicken_menu = chicken_menu_count * 10.35
price_fish_menu = fish_menu_count * 12.4
price_vegetable_menu = vegetable_menu_count * 8.15

all_menu_sum = price_chicken_menu + price_fish_menu + price_vegetable_menu
dessert_price = all_menu_sum * 0.20

total_sum = all_menu_sum + dessert_price + 2.50

print(total_sum)
