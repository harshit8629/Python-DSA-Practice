from collections import Counter
nums = [0,1]
count = Counter(nums)
result=[]
for key,items in count.items():
    if items ==1:
        result.append(key)
print(result)