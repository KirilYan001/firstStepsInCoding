base = 5364
day_counter = 1
command = input()
while command != 'END':

    meters = int(input())

    if command == 'Yes':
        day_counter += 1
        base += meters
    elif command == 'No':
        base += meters

    if base >= 8848:
        break
    elif day_counter > 5:
        break

    command = input()

if base >= 8848:
    print(f'Goal reached for {day_counter} days!')
else:
    print('Failed!')
    print(f'{base}')


