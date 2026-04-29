def rotate_list(nums, k):

    n = len(nums)

    # Handle rotations greater than list size
    k = k % n

    # Rotate the list
    rotated = nums[-k:] + nums[:-k]

    return rotated


# Example
nums = [1, 2, 3, 4, 5]
k = 2

result = rotate_list(nums, k)

print("Rotated List:", result)