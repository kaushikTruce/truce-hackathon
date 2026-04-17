# Two sum II the array is sorted

def twoSum(nums, target):
    n = len(nums)
    i = 0
    j = n - 1

    while i < j:
        if nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            return i + 1, j + 1
    return None

numbers = [2,7,11,15] 
target = 13
print(twoSum(numbers, target))