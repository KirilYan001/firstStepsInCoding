flag = False

for hour in range(0, 24):
    for minutes in range(0, 60):
        for seconds in range(0, 60):
            if hour == 5 and minutes == 0:
                print(f'{hour}:{minutes:02d}:{seconds:02d}')
                flag = True
                break
        if flag:
            break

    if flag:
        break
