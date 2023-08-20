cost_to_print_one_page = float(input())
cost_to_print_one_main_page = float(input())
discount_to_print_page = int(input())
money_to_pay_to_designer = float(input())
percent_of_total_sum_what_payed_the_tem = int(input())

sum_to_print_all_pages = ((cost_to_print_one_page * 899) + (cost_to_print_one_main_page * 2))
sum_to_print_all_pages = sum_to_print_all_pages - ((discount_to_print_page / 100 ) * sum_to_print_all_pages)
sum_to_print_all_pages += money_to_pay_to_designer
tem_payment = sum_to_print_all_pages - ((percent_of_total_sum_what_payed_the_tem / 100) * sum_to_print_all_pages)

print(f'Avtonom should pay {tem_payment:.2f} BGN.')

# 0.01
# 1
# 10
# 20
# 20

# 0.05
# 1.20
# 40
# 19.99
# 20

# 0.02
# 0.50
# 18
# 21
# 50