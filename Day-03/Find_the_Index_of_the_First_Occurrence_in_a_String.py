# you can use another example for testing it
# First approach
import re
def FindIndex(string,target):
    matches = re.finditer(target,string)
    for match in matches:
        return match.start()
    return -1
s = "the sky is green"
target = "sky"
result = FindIndex(s,target)
print(result)

# Second approach
def Findindex(string,target):
    for i in range(len(string)):
        if (string[i:i+len(target)]==target):
            return i
    return -1

s1="sadbutsad"
Target = "sad"
result1 = Findindex(s1,Target)
print(result1)

