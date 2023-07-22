volume_liters = int(input())
pipe_one_per_hour = int(input())
pipe_two_per_hour = int(input())
left_time = float(input())

sum_volumes_1 = (left_time * pipe_one_per_hour)
sum_volumes_2 = (left_time * pipe_two_per_hour)
total_sum_volume = sum_volumes_1 + sum_volumes_2

percent_total_volume = (total_sum_volume / volume_liters) * 100

percent_pipe1 = (sum_volumes_1 / total_sum_volume) * 100
percent_pipe2 = (sum_volumes_2 / total_sum_volume) * 100

if volume_liters > total_sum_volume:
    print(f"The pool is {percent_total_volume:.2f}% full. Pipe 1: {percent_pipe1:.2f}%. Pipe 2: {percent_pipe2:.2f}%.")
else:
    basin_overflow = total_sum_volume - volume_liters
    print(f"For {left_time:.2f} hours the pool overflows with {basin_overflow:.2f} liters.")
# print("THANK YOU DADDY")
