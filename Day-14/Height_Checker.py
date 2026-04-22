heights = [5,1,2,3,4]
expected = sorted(heights)
count = 0
for i in range(len(heights)):
  if heights[i]==expected[i]:
    continue 
  else:
    count+=1
print(count)