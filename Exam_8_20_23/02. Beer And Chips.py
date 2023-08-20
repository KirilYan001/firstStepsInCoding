from math import ceil

name_football_fan = input()
budget = float(input())
count_of_bear = int(input())
count_of_chips = int(input())

total_sum_for_bear = 1.20 * count_of_bear
discount = total_sum_for_bear * 0.45
total_sum_chips = ceil(discount * count_of_chips)

total_sum = total_sum_for_bear + total_sum_chips

if budget < total_sum:
    left = total_sum - budget
    print(f"{name_football_fan} needs {left:.2f} more leva!")
elif budget >= total_sum:
    left = budget - total_sum
    print(f"{name_football_fan} bought a snack and has {left:.2f} leva left.")








# George
# 10
# 2
# 3

# Valetin
# 5
# 2
# 4