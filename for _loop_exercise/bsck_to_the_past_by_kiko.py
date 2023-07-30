money = float(input())
years_to_stay = int(input())
years_of_the_guy = 18

for years in range(1800, years_to_stay + 1):
    if years % 2 == 0:
        money -= 12000
        years_of_the_guy += 1
    else:
        money -= 12000 + 50 * years_of_the_guy
        years_of_the_guy += 1

money_left = money
# money_left = abs(money_left)

if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')
else:
    print(f'He will need {abs(money_left):.2f} dollars to survive.')

