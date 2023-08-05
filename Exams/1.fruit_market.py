
strawberry_price_lv = float(input())
banana_in_kg = float(input())
orange_in_kg = float(input())
raspberries_in_kg = float(input())
strawberry_in_kg = float(input())

raspberries_in_lv = strawberry_price_lv / 2
orange_in_lv = raspberries_in_lv - (0.4 * raspberries_in_lv)
banana_in_lv = raspberries_in_lv - (0.8 * raspberries_in_lv)

sum_price_raspberries = raspberries_in_kg * raspberries_in_lv
sum_price_orange = orange_in_kg * orange_in_lv
sum_price_banana = banana_in_kg * banana_in_lv
sum_price_strawberry = strawberry_in_kg * strawberry_price_lv

total_sum = sum_price_strawberry + sum_price_banana + sum_price_raspberries + sum_price_orange

print(f'{total_sum:.2f}')