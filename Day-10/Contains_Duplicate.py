nums = [1,2,3,1]
def containsDuplicate(nums):
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False        
print(containsDuplicate(nums))