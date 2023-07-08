rent_year = int(input())

shoes = rent_year - (rent_year * 0.4)
equipment = shoes - (shoes * 0.2)
basket_ball = equipment / 4
basket_assessor = basket_ball / 5

total_sum_equipment = rent_year + shoes + equipment + basket_ball + basket_assessor

print(total_sum_equipment)
