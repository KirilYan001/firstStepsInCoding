bitcoin = int(input())
chinese_yuan = float(input())
commission = float(input())

price_for_bitcoin = 1168
price_yuan_in_dolar = 0.15
price_dolar_in_leva = 1.76
price_euro = 1.95

yuan_price = price_yuan_in_dolar * chinese_yuan
dolar_in_leva = yuan_price * price_dolar_in_leva

total_price = (bitcoin * price_for_bitcoin) + dolar_in_leva
total_price /= price_euro
price_wiyh_commision = total_price * 0.05
final_price = total_price - price_wiyh_commision

print(f'{final_price:.2f}')
