s = "pwwkewd"        # given string

s1 = list(s)         # convert string into list of characters
# ['p', 'w', 'w', 'k', 'e', 'w', 'd']

s2 = set(s1)         # convert list to set to remove duplicates
# {'p', 'w', 'k', 'e', 'd'}

print(len(s2))       # print number of unique characters
# output: 5