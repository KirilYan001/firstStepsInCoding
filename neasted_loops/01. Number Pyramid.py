n = int(input())

flag = False
current_num = 1
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current_num > n:
            flag = True
            break

        print(current_num, end=" ")

        current_num += 1
    print()
    if flag:
        break

