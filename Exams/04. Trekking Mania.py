numbers_of_groups = int(input())
musala = 0
monblant = 0
kilimanjaro = 0
k2 = 0
everest = 0
count_of_people = 0

for number in range(numbers_of_groups):
    number_of_members = int(input())
    count_of_people += number_of_members
    if number_of_members <= 5:
        musala += number_of_members
    elif 5 < number_of_members < 13:
        monblant += number_of_members
    elif 12 < number_of_members < 26:
        kilimanjaro += number_of_members
    elif 25 < number_of_members < 41:
        k2 += number_of_members
    elif number_of_members > 40:
        everest += number_of_members

percent_musala = (musala / count_of_people) * 100
percent_monblant = (monblant / count_of_people) * 100
percent_kilimanjaro = (kilimanjaro / count_of_people) * 100
percent_k2 = (k2 / count_of_people) * 100
percent_everest = (everest / count_of_people) * 100

print(f'{percent_musala:.2f}%\n'
      f'{percent_monblant:.2f}%\n'
      f'{percent_kilimanjaro:.2f}%\n'
      f'{percent_k2:.2f}%\n'
      f'{percent_everest:.2f}%')
