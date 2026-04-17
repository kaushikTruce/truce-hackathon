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

# boyer moore algorithm
def usingAlgo(nums):
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0
    resList = []

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 += 1
        elif count2 == 0:
            candidate2 = num
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    freq1 = 0
    freq2 = 0
    for num in nums:
        if num == candidate1:
            freq1 += 1
        elif num == candidate2:
            freq2 += 1
    
    if freq1 > len(nums) // 3:
        resList.append(candidate1)
    if freq2 > len(nums) // 3:
        resList.append(candidate2)

    return resList

elements = [4,2,1,1]
print(usingAlgo(elements))