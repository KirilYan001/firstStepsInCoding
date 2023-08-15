budget = float(input())
gender = input()
age = int(input())
sport = input()
card = 0

if gender == 'm':
    if age < 19:
        if sport == 'Gym':
            card += 42
            card = card - (card * 0.2)
        elif sport == 'Boxing':
            card += 41
            card = card - (card * 0.2)
        elif sport == 'Yoga':
            card += 45
            card = card - (card * 0.2)
        elif sport == 'Zumba':
            card += 34
            card = card - (card * 0.2)
        elif sport == 'Dances':
            card += 51
            card = card - (card * 0.2)
        elif sport == 'Pilates':
            card += 39
            card = card - (card * 0.2)
    elif age > 19:
        if sport == 'Gym':
            card += 42
        elif sport == 'Boxing':
            card += 41
        elif sport == 'Yoga':
            card += 45
        elif sport == 'Zumba':
            card += 34
        elif sport == 'Dances':
            card += 51
        elif sport == 'Pilates':
            card += 39
elif gender == 'f':
    if age < 19:
        if sport == 'Gym':
            card += 35
            card = card - (card * 0.2)
        elif sport == 'Boxing':
            card += 37
            card = card - (card * 0.2)
        elif sport == 'Yoga':
            card += 43
            card = card - (card * 0.2)
        elif sport == 'Zumba':
            card += 31
            card = card - (card * 0.2)
        elif sport == 'Dances':
            card += 53
            card = card - (card * 0.2)
        elif sport == 'Pilates':
            card += 37
            card = card - (card * 0.2)
    elif age > 19:
        if sport == 'Gym':
            card += 35
        elif sport == 'Boxing':
            card += 37
        elif sport == 'Yoga':
            card += 43
        elif sport == 'Zumba':
            card += 31
        elif sport == 'Dances':
            card += 53
        elif sport == 'Pilates':
            card += 37

if budget >= card:
    print(f"You purchased a 1 month pass for {sport}.")
elif budget < card:
    total_sum = budget - card
    total_sum = abs(total_sum)
    print(f"You don't have enough money! You need ${total_sum:.2f} more.")
