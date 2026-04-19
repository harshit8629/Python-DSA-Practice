pattern = "abba"
s = "dog cat cat fish"

pattern1 = list(pattern)
s1 = list(s.split())

if len(pattern1) != len(s1):
    print(False)
else:
    dic1 = {}  
    dic2 = {}   
    flag = True

    for i in range(len(pattern1)):
        ch = pattern1[i]
        word = s1[i]

        if ch in dic1:
            if dic1[ch] != word:
                flag = False
                break
        else:
            dic1[ch] = word

        if word in dic2:
            if dic2[word] != ch:
                flag = False
                break
        else:
            dic2[word] = ch

    print(flag)