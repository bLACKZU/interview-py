arr = [2, 3]
k = 1
sum = sum(arr[:k])
max_sum = sum
for i in range(1, len(arr) - k + 1):
    sum = sum - arr[i - 1] + arr[i - 1 + k]
    max_sum = max(max_sum, sum)
print(max_sum)