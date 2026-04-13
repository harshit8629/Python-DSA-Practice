# you can use different questions to solve it
s = "abcde"
t = "aabcde"

s_list = list(s)
for i in t:
  if i in s_list:
    s_list.remove(i)
  else:
    print(i)
