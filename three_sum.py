def three_sum(arr, target):

    sorted_arr = sorted(arr)
    for i in range(len(sorted_arr) - 2):
        l = i + 1
        r = len(sorted_arr) - 1

        requiredSum = target - arr[i]
        while l < r:
            if arr[l] + arr[r] == requiredSum:
                return True
            elif arr[l] + arr[r] < requiredSum:
                l += 1
            else:
                r -= 1

    return False

array = [1, 4, 45, 6, 10, 8]
target = 12
print(three_sum(array, target))
