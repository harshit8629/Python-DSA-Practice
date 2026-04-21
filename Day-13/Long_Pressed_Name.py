name = "alex"
typed = "aaleex"

i = 0  # pointer for name
j = 0  # pointer for typed

while j < len(typed):
    if i < len(name) and name[i] == typed[j]:
        i += 1
        j += 1
    elif j > 0 and typed[j] == typed[j - 1]:
        j += 1
    else:
        print(False)
        break
else:
    print(i == len(name))