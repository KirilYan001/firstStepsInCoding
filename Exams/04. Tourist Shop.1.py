budget = float(input())
total_sum = 0
counter = 0
num_items = 0

while True:
    command_name = input()

    if command_name == 'Stop':
        print(f"You bought {num_items} products for {total_sum:.2f} leva.")
        break

    command_price = float(input())

    counter += 1
    num_items += 1

    if counter % 3 == 0:
        command_price /= 2
        budget -= command_price
        counter = 0
    else:
        budget -= command_price

    total_sum += command_price

    if budget < command_price:
        print("You don't have enough money!")
        print(f"You need {abs(budget):.2f} leva!")
        break
