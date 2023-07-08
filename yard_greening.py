import time

area = float(input())

before_discount = area * 7.61
discount = before_discount * 0.18
after_discount = before_discount - discount
print(f'"The final price is: {after_discount} lv."')
time.sleep(1)
print(f'"The discount is: {discount} lv."')
time.sleep(2)


