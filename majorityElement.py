from collections import Counter

# Using Hashing
def majorityEle(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    print(freq)

    for item, value in freq.items():
        if value > len(nums) / 2:
            return item
    
    return None

# Using Counter
def func(nums):
    freq = Counter(nums)
    for item, value in freq.items():
        if value > len(nums) / 2:
            return item
    return None

# Using Moore's Voting Algorithm: - TC: O(n) and SC: O(1)
def mooreAlgo(nums):
    ele, count = None, 0
    for num in nums:
        if count == 0:
            ele = num
            count = 1
        elif num == ele:
            count += 1
        else:
            count -= 1
    
    # check for majority
    freq = 0
    for num in nums:
        if num == ele:
            freq += 1
    
    if freq > len(nums) // 2:
        return ele
    return None

nums = [3, 3, 1, 2, 0, 3, 3]
print(majorityEle(nums))
print(func(nums))
print(mooreAlgo(nums))