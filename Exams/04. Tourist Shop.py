budget = float(input())
product_counter = 0
spend_money = 0

brand = input()
while brand != 'Stop':
    brand_price = float(input())
    product_counter += 1

    if product_counter % 3 == 0:
        brand_price /= 2

    spend_money += brand_price
    budget -= brand_price

    if budget < 0:
        print(f"You don't have enough money!")
        print(f'You need {abs(budget):.2f} leva!')
        break
    brand = input()

if budget >= 0:
    print(f"You bought {product_counter} products for {spend_money:.2f} leva.")