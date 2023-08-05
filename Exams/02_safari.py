budget = float(input())
litre_of_gas = float(input())
day_of_week = input()
guide = 100
oil_price_liters = 2.10
total_sum = 0

if day_of_week == 'Saturday':
    litre_of_gas *= oil_price_liters
    total_sum = guide + litre_of_gas
    discount = total_sum - (total_sum * 0.10)
    budget -= discount
else:
    litre_of_gas *= oil_price_liters
    total_sum = guide + litre_of_gas
    discount = total_sum - (total_sum * 0.20)
    budget -= discount

if budget >= 0:
    print(f"Safari time! Money left: {budget:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {abs(budget):.2f} lv.")


