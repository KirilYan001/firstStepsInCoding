type_tickets = input()
rows = int(input())
cols = int(input())

all_seats = rows * cols

price = 0
if type_tickets == "Premiere":
    price = 12
elif type_tickets == "Normal":
    price = 7.50
elif type_tickets == "Discount":
    price = 5

total_income = all_seats * price

print(f"{total_income:.2f} leva")