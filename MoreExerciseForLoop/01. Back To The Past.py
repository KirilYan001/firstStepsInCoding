inheritance = float(input())
year_to_stay = int(input())
his_age = 18
spend_money = 12000
diff = 0
current_year = 1800

for _ in range(current_year, year_to_stay + 1):
    if current_year % 2 == 0:
        inheritance -= spend_money
        his_age += 1
        current_year += 1
    else:
        inheritance -= spend_money + (his_age * 50)
        his_age += 1
        current_year += 1
if inheritance >= 0:
    diff -= spend_money
    print(f'Yes! He will live  a carefree live and will have {inheritance} dollars left')
else:
    print(f"He will need more {abs(inheritance)} for survive")
