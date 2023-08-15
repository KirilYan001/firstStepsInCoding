days_to_stay = int(input())
type_of_accommodation = input()
review = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35
price_discount = 0
price_to_stay = 0

if type_of_accommodation == 'room for one person':
    if days_to_stay < 10:
        price_discount = days_to_stay * room_for_one_person
    elif 10 < days_to_stay < 14:
        price_discount = days_to_stay * room_for_one_person
    elif days_to_stay > 15:
        price_discount = days_to_stay * room_for_one_person

elif type_of_accommodation == 'apartment':
    if days_to_stay < 10:
        price_to_stay = (days_to_stay - 1) * apartment
        price_discount = price_to_stay - (price_to_stay * 0.30)

    elif 10 < days_to_stay < 15:
        price_to_stay = (days_to_stay - 1) * apartment
        price_discount = price_to_stay - (price_to_stay * 0.35)

    elif days_to_stay > 15:
        price_to_stay = (days_to_stay - 1) * apartment
        price_discount = price_to_stay - (price_to_stay * 0.50)
elif type_of_accommodation == 'president apartment':
    if days_to_stay < 10:
        price_to_stay = (days_to_stay - 1) * president_apartment
        price_discount = price_to_stay - (price_to_stay * 0.10)

    elif 10 < days_to_stay < 15:
        price_to_stay = (days_to_stay - 1) * president_apartment
        price_discount = price_to_stay - (price_to_stay * 0.15)

    elif days_to_stay > 15:
        price_to_stay = (days_to_stay - 1) * president_apartment
        price_discount = price_to_stay - (price_to_stay * 0.20)

if review == 'positive':
    price_discount = (price_discount * 0.25) + price_discount
    print(f'{price_discount:.2f}')
elif review == 'negative':
    price_discount = (price_discount * 0.10) + price_discount
    print(f'{price_discount:.2f}')

