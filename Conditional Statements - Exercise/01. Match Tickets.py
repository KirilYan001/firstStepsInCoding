budget = float(input())
category = input()
count_people = int(input())

price_vip = 499.99
price_normal = 249.99
total_price = 0

if category == "vip":
    total_price = price_vip * count_people
    if count_people <= 4:
        total_price -= budget * 0.75
    elif 10 <= count_people <= 24:
        total_price -= budget * 0.50
    elif 25 <= count_people <= 49:
        total_price -= budget * 0.40
    elif count_people >= 50:
        total_price -= budget * 0.25
elif category == "normal":
    total_price = price_normal * count_people
    if count_people <= 4:
        total_price -= (budget * 0.75)
    elif 10 <= count_people <= 24:
        total_price -= (budget * 0.50)
    elif 25 <= count_people <= 49:
        total_price -= (budget * 0.40)
    elif count_people >= 50:
        total_price -= (budget * 0.25)

left_price = abs(budget - total_price)

if left_price < budget:
    print(f"Not enough money! You need {left_price} leva.")
else:
    print(f"Yes! You have {left_price} leva left.")

print("buy")
