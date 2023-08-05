name_of_series = input()
count_of_seasons = int(input())
count_of_episodes = int(input())
time_of_episode_with_out_the_adds = float(input())


# percent = time_of_episode_with_out_the_adds * 0.20
# print(percent)

time_of_episode_with_add = time_of_episode_with_out_the_adds - (0.80 * time_of_episode_with_out_the_adds)
time_of_episode_with_adds = time_of_episode_with_out_the_adds + time_of_episode_with_add
time_for_special_episodes = count_of_seasons * 10
total_sum = time_of_episode_with_adds * count_of_episodes * count_of_seasons + time_for_special_episodes

print(f"Total time needed to watch the {name_of_series} series is {total_sum:.0f} minutes.")
