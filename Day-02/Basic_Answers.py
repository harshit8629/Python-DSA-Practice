# you can use different examples to test it
# Question 1
def findlargest(arr):
  largest = max(arr)
  return largest

arr = [3, 7, 2, 9, 5]
result = findlargest(arr)
print(result)

# Question 2
def EvenOdd(arr):
    Even =0
    Odd =0
    for i in arr:
        if(i%2==0):
            Even+=1
        else:
            Odd+=1
    return "Even =",Even,"Odd =",Odd
ar = [1,2,3,4,5,6]
print(EvenOdd(ar))