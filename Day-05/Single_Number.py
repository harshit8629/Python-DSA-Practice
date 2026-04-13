#  counter is used to find the frequency of list , Strings
from collections import Counter
nums = [2,2,1]
count = Counter(nums)
# you can understad the working by print(count) it is like a dictonary
print(count)
for key,value in count.items():
  if value ==1:
    print(key)