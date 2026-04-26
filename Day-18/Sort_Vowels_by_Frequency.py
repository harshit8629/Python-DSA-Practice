s = "leetcode"

vowels = set("aeiou")

# Step 1: collect vowels
vowel_list = []
for ch in s:
    if ch in vowels:
        vowel_list.append(ch)

# Step 2: frequency + first occurrence
freq = {}
first_pos = {}

for i, ch in enumerate(vowel_list):
    freq[ch] = freq.get(ch, 0) + 1
    if ch not in first_pos:
        first_pos[ch] = i

# Step 3: sort vowels
unique_vowels = list(freq.keys())
unique_vowels.sort(key=lambda x: (-freq[x], first_pos[x]))

# Step 4: rebuild sorted vowels
sorted_vowels = []
for v in unique_vowels:
    sorted_vowels.extend([v] * freq[v])

# Step 5: put vowels back
res = list(s)
idx = 0

for i in range(len(res)):
    if res[i] in vowels:
        res[i] = sorted_vowels[idx]
        idx += 1

# Output
print("".join(res))