# Using Kadane's Algorithm: - TC: O(n) and SC: O(1)

def maxSubArray(nums):
    maxSum, currSum = float('-inf'), 0
    for i in range(len(nums)):
        currSum += nums[i]
        
        if currSum > maxSum:
            maxSum = currSum

        if currSum < 0:
            currSum = 0
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))