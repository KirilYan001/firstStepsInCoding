month = input()
number_suspended_hours = int(input())
number_people_in_group = int(input())
time = input()
if month == "march" or month == "april" or month == "may":
    if time == "day":
        price = 10.50
        if number_people_in_group >= 4:
            price = price - (price * 0.10)
        if number_suspended_hours >= 5:
            price = price - (price * 0.50)
    elif time == "night":
        price = 8.40
        if number_people_in_group >= 4:
            price = price - (price * 0.10)
        if number_suspended_hours >= 5:
            price = price - (price * 0.50)
elif month == "june" or month == "july" or month == "august":
    if time == "day":
        price = 12.60
        if number_people_in_group >= 4:
            price = price - (price * 0.10)
        if number_suspended_hours >= 5:
            price = price - (price * 0.50)
    elif time == "night":
        price = 10.20
        if number_people_in_group >= 4:
            price = price - (price * 0.10)
        if number_suspended_hours >= 5:
            price = price - (price * 0.50)
end_sum = (price * number_people_in_group) * number_suspended_hours
print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {end_sum:.2f}")

# march
# 3
# 3
# day

# july
# 5
# 5
# night
