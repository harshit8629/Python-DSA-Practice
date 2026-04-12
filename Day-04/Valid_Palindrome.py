# you can use the examples as you want
s = "A man, a plan, a canal: Panama"
# split is used for converting the string into list by removing the whitespace
# join is used for attach the list into one element
# lower is for converting string into lowercase
s1 = ''.join(s.split()).lower()
s2=''
for i in s1:
    # isalnum is used to check the string consist of alphabets and numbers
  if i.isalnum():
    s2+=i
if(s2[::-1]==s2):
  print(True)
else:
  print(False)