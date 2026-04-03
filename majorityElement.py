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
        else:
            return None

nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
print(majorityEle(nums))