price_usd_processor = float(input())
price_usd_video_card = float(input())
price_usd_ram_memory = float(input())
num_of_ram = int(input())
percent_discount = float(input())

price_lv_processor = price_usd_processor * 1.57
price_lv_video_card = price_usd_video_card * 1.57
price_lv_ram_memory = price_usd_ram_memory * 1.57

total_price_for_ram = price_lv_ram_memory * num_of_ram
discount_price_processor = price_lv_processor - (price_lv_processor * percent_discount)
discount_price_video_card = price_lv_video_card - (price_lv_video_card * percent_discount)
total_sum = discount_price_processor + discount_price_video_card + total_price_for_ram

print(f"Money needed - {total_sum:.2f} leva.")


