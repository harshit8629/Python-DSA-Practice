from collections import Counter
arr = [2,2,2,3,3]
count = Counter(arr)
result =[]
for key,items in count.items():
  if key == items:
    result.append(key)
if result:
  print(max(result))
else:
  print(-1)