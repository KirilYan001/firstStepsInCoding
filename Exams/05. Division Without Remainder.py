number = int(input())
sum2 = 0
sum3 = 0
sum4 = 0
counter_about_2 = 0
counter_about_3 = 0
counter_about_4 = 0

for _ in range(number):
    num_input = int(input())
    if num_input % 2 == 0:
        counter_about_2 += 1
        sum2 += num_input

    if num_input % 3 == 0:
        counter_about_3 += 1
        sum3 += num_input

    if num_input % 4 == 0:
        counter_about_4 += 1
        sum4 += num_input

percent_about_2 = (counter_about_2 / number) * 100
percent_about_3 = (counter_about_3 / number) * 100
percent_about_4 = (counter_about_4 / number) * 100

print(f'{percent_about_2:.2f}%')
print(f'{percent_about_3:.2f}%')
print(f'{percent_about_4:.2f}%')