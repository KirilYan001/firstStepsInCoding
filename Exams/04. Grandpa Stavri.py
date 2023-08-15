days = int(input())

sum_of_drink = 0
degrees_sum = 0
sum_of_drink_and_degrees = 0

for day in range(days):
    liters_of_drink = float(input())
    degrees = float(input())
    sum_of_drink += liters_of_drink

    current_sum = liters_of_drink * degrees
    sum_of_drink_and_degrees += current_sum

    degrees_sum += degrees

average = sum_of_drink_and_degrees / sum_of_drink

print(f'Liter: {sum_of_drink:.2f}')
print(f'Degrees: {average:.2f}')
if average < 38:
    print("Not good, you should baking!")
elif 38 <= average <= 42:
    print("Super!")
elif average > 42:
    print("Dilution with distilled water!")
