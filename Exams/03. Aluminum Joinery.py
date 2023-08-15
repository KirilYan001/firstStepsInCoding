count_of_frame = int(input())
type_of_frame = input()
type_of_delivery = input()

cost_of_frame = 0
total_price = 0
discount = 0

if count_of_frame < 10:
    print('Invalid order')
else:
    if type_of_frame == '90X130':
        cost_of_frame = 110
        if cost_of_frame > 30 and count_of_frame < 60:
            cost_of_frame *= count_of_frame
            discount = cost_of_frame * 0.05
        elif cost_of_frame > 60:
            cost_of_frame *= count_of_frame
            discount = cost_of_frame * 0.08
    elif type_of_frame == '100X150':
        cost_of_frame = 140
        if cost_of_frame > 40 and count_of_frame < 80:
            cost_of_frame *= count_of_frame
            discount = cost_of_frame * 0.06
        elif cost_of_frame > 80:
            cost_of_frame *= count_of_frame
            discount = cost_of_frame * 0.10
    elif type_of_frame == '130X180':
        count_of_frame = 190
        cost_of_frame = 140
        if cost_of_frame > 20 and count_of_frame < 50:
            cost_of_frame *= count_of_frame
            discount = cost_of_frame * 0.07
        elif cost_of_frame > 50:
            cost_of_frame *= count_of_frame
            discount = cost_of_frame * 0.12
    elif type_of_frame == '200X300':
        count_of_frame = 250
        cost_of_frame = 140
        if cost_of_frame > 25 and count_of_frame < 50:
            cost_of_frame *= count_of_frame
            discount = cost_of_frame * 0.09
        elif cost_of_frame > 50:
            cost_of_frame *= count_of_frame
            discount = cost_of_frame * 0.14

    total_price = cost_of_frame - discount

    if type_of_delivery == "With delivery":
        total_price += 60

    input(f'{total_price:.2f} BGN')

if count_of_frame > 99:
    total_price -= total_price * 0.04
