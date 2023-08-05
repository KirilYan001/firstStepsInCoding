contract_time = input()
contract_type = input()
added_mobile_internet = input()
count_of_months = int(input())
tax = 0

if contract_time == 'one':
    if contract_type == 'Small':
        if added_mobile_internet == 'yes':
            tax = 9.98 + 5.50
        else:
            tax = 9.98
    elif contract_type == 'Middle':
        if added_mobile_internet == 'yes':
            tax = 18.99 + 4.35
        else:
            tax = 18.99
    elif contract_type == 'Large':
        if added_mobile_internet == 'yes':
            tax = 25.98 + 4.35
        else:
            tax = 25.98
    elif contract_type == 'ExtraLarge':
        if added_mobile_internet == 'yes':
            tax = 35.99 + 3.85
        else:
            tax = 35.99

elif contract_time == 'two':
    if contract_type == 'Small':
        if added_mobile_internet == 'yes':
            tax = 8.58 + 5.50
        else:
            tax = 8.58
    elif contract_type == 'Middle':
        if added_mobile_internet == 'yes':
            tax = 17.09 + 4.35
        else:
            tax = 17.09
    elif contract_type == 'Large':
        if added_mobile_internet == 'yes':
            tax = 23.59 + 4.35
        else:
            tax = 23.59
    elif contract_type == 'ExtraLarge':
        if added_mobile_internet == 'yes':
            tax = 31.79 + 3.85
        else:
            tax = 31.79

total_sum = tax * count_of_months

if contract_time == 'one':
    print(f'{total_sum:.2f} lv.')
else:
    discount = (total_sum * 0.0375)
    discount_price = total_sum - discount
    print(f'{discount_price:.2f} lv.')
