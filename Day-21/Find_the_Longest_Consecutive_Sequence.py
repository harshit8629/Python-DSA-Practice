def longest_consecutive(nums):

    num_set = set(nums)

    longest = 0

    for num in num_set:

        # Start sequence only if previous number does not exist
        if num - 1 not in num_set:

            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

    return longest


# Example
nums = [100, 4, 200, 1, 3, 2]

result = longest_consecutive(nums)

print("Longest Consecutive Sequence Length:", result)