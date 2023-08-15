price_for_bags_over_then_20kg = float(input())
bags_kg = float(input())
days_before_trip = int(input())
bags_count = int(input())

price = 0

if bags_kg < 10:
    price = price_for_bags_over_then_20kg * 0.20
elif 10 <= bags_kg <= 20:
    price = price_for_bags_over_then_20kg * 0.50
elif bags_kg > 20:
    price = price_for_bags_over_then_20kg

total_price = 0

if days_before_trip > 30:
    total_price = price + (price * 0.1)
elif 7 <= days_before_trip <= 30:
    total_price = price + (price * 0.15)
elif days_before_trip < 7:
    total_price = price + (price * 0.4)

price_for_baggage = total_price * bags_count
print(f" The total price of bags is: {price_for_baggage:.2f} lv. ")
