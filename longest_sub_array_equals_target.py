nums = [10, -10, 20, 30]
prefixSum = 0
k = 5
firstSeen = -1
mapSum = {}
resultMax = 0
mapSum[prefixSum] = firstSeen
for i in range(0, len(nums)):
    prefixSum += nums[i]
    firstSeen = i
    mapSum[prefixSum] = firstSeen
    complement = prefixSum - k
    if complement in mapSum:
        resultMax = max(resultMax, i - mapSum[complement]) 
    
print(resultMax)