s = "acb"
t = "ahbgdc"
i = 0
for j in range(len(t)):
    if i < len(s) and s[i] == t[j]:
        i += 1
print(i == len(s))