# Find the elements that appears more than N/3 times in the array

def majorityElement(nums):
    resList = []
    countEle = {}

    for num in nums:
        if num in countEle:
            countEle[num] += 1
        else:
            countEle[num] = 1
    
    for item, value in countEle.items():
        if value > len(nums) // 3:
            resList.append(item)

    return resList 

nums = [3, 2, 3]
print(f"nums: {nums}")
print(majorityElement(nums))