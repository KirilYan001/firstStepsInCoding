count_bad_grade = int(input())

bad_grades_counter = 0
sum_average = 0
counter_of_problems = 0

average = 0

flag = False

last_problem = ''

name_of_problem = input(str())
while name_of_problem != 'Enough':
    grade = int(input())

    if grade <= 4:
        bad_grades_counter += 1

    if count_bad_grade == bad_grades_counter:
        flag = True
        break

    sum_average += grade

    last_problem = name_of_problem
    counter_of_problems += 1
    name_of_problem = input()

average = sum_average / counter_of_problems

if flag:
    print(f"You need a break, {count_bad_grade} poor grades.")
else:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {counter_of_problems}")
    print(f"Last problem: {last_problem}")

# 3
# Money
# 6
# Story
# 4
# Spring Time
# 5
# Bus
# 6
# Enough

# 2
# Income
# 3
# Game Info
# 6
# Best Player
# 4
