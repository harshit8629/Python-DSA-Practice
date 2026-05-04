nums = [1,2,3]
result = [[]]
for i in nums:
    result += [subset + [i] for subset in result]
print(result)