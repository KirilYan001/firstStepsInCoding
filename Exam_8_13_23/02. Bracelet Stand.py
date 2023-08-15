pocket_money_daily = float(input())
money_earned_from_selling = float(input())
expenses_for_all_time = float(input())
gift_price = float(input())

saved_pocket_money = 5 * pocket_money_daily
earned_money = 5 * money_earned_from_selling
all_saved_money = saved_pocket_money + earned_money

price_after_expenses = all_saved_money - expenses_for_all_time

if price_after_expenses >= gift_price:
    print(f"Profit: {price_after_expenses:.2f} BGN, the gift has been purchased.")
else:
    needed_money = gift_price - price_after_expenses
    print(f"Insufficient money: {needed_money:.2f} BGN.")
