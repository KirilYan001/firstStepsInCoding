days = int(input())
doctors = 7
# day = 1
treated = 0
untreated = 0
# current_treated = 0
for day in range(1, days + 1):
    patients = int(input())

    if day % 3 == 0:
        if patients > doctors:
            doctors += 1

    if patients > doctors:
        current_treated = 0
        patients -= doctors
        untreated += patients
        current_treated += doctors
        treated += current_treated
    elif doctors == patients:
        treated += doctors
    elif patients < doctors:
        treated += patients

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')

# 4
# 7
# 27
# 9
# 1

# 6
# 25
# 25
# 25
# 25
# 25
# 2

# 3
# 7
# 7
# 7