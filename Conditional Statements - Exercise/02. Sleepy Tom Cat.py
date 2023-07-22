import math

day_off = int(input())
norm_for_play_for_year = 30000
play_at_working_day = 63
play_at_day_off = 127

working_day_for_year = (365 - day_off) * play_at_working_day
day_off_for_year = day_off * play_at_day_off
time_playing_for_year = working_day_for_year + day_off_for_year
rest_time = (norm_for_play_for_year - time_playing_for_year) / 60


# TODO format

# if norm_for_play_for_year < time_playing_for_year:
#     print("Tom will run away")
#     print(f"{} hours and {} minutes less for play")
# else:
#     print("Tom sleeps well")
#     print(f"{} hours and {} minutes more for play")

# input("god")
