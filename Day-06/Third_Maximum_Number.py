nums = [1,2,3]
nums = list(set(nums))

firstmaximum = max(nums)
nums.remove(firstmaximum)

if not nums:
    print(firstmaximum)

secondmaximum = max(nums)
nums.remove(secondmaximum)

if nums:
    thirdmaximum = max(nums)
    print(thirdmaximum)   
else:
    print(firstmaximum)  