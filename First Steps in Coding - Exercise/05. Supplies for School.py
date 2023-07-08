price_pen = 5.80
price_marker = 7.20
price_detergent =1.20
count_pen = int(input())
count_markers = int(input())
detergents_liters = int(input())
discount = int(input())

total_price_pen = count_pen * price_pen
total_price_marker = count_markers * price_marker
total_price_detergent = detergents_liters * price_detergent

total_sum = total_price_pen + total_price_marker + total_price_detergent
total_sum = total_sum - (total_sum * discount / 100)
print(total_sum)