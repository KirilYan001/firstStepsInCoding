name_of_company = input()
count_of_tickets_for_adults = int(input())
count_of_tickets_for_children = int(input())
price_of_ticket_for_adult = float(input())
service = float(input())

price_of_ticket_for_children = price_of_ticket_for_adult - (0.70 * price_of_ticket_for_adult)
price_of_ticket_for_adult_service =price_of_ticket_for_adult + service
price_of_ticket_for_children_service = price_of_ticket_for_children + service

total_sum = (count_of_tickets_for_children * price_of_ticket_for_children_service) + (count_of_tickets_for_adults * price_of_ticket_for_adult_service)
discount = total_sum * 0.20
print(f'The profit of your agency from {name_of_company} tickets is {discount:.2f} lv.')