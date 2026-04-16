nums =[12,32,22]
digit = 2
count = 0

for num in nums:
      while num > 0:
          if num % 10 == digit:
              count += 1
          num //= 10
print(count)