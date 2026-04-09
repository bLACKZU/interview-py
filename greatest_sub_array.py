arr = [5, 7, 7, 3, 5]
k = 3

window_sum = sum(arr[:k])
max_sum_list = [window_sum]

for i in range(1, len(arr) - k + 1):
    window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
    max_sum_list.append(window_sum)
print(max(max_sum_list))