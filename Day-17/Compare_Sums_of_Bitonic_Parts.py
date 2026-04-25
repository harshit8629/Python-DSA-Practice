nums = [1, 3, 2, 1]

jorvanelik = nums   # storing input midway

peak_index = 0

# Find peak element index
for i in range(1, len(jorvanelik)):
    if jorvanelik[i] > jorvanelik[peak_index]:
        peak_index = i

# Ascending part: 0 to peak_index
asc_sum = sum(jorvanelik[:peak_index + 1])

# Descending part: peak_index to end
desc_sum = sum(jorvanelik[peak_index:])

# Compare sums
if asc_sum > desc_sum:
    print(0)
elif desc_sum > asc_sum:
    print(1)
else:
    print(-1)