number_locations = int(input())
total_avg = 0
for location in range(1, number_locations + 1):
    avg_extraction = float(input())
    number_of_days = int(input())
    sum_extraction = 0

    for day in range(1, number_of_days + 1):
        extraction = float(input())
        sum_extraction += extraction

        total_avg = sum_extraction / number_of_days

    if total_avg >= avg_extraction:
        print(f'Good job! Average gold per day: {total_avg:.2f}.')
    else:
        needed_gold = avg_extraction - total_avg
        print(f'You need {needed_gold:.2f} gold.')


