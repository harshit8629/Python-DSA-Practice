s = "ab-cd"
s1 = list(s)
s2=[]
for i in range(len(s)):
    if s1[i].isalpha():
        s2.append(s1[i])
s2=s2[::-1]
j=0
for i in range(len(s)):
    if s[i].isalpha():
        s1[i]=s2[j]
        j+=1
print("".join(s1))