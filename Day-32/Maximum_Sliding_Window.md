# Maximum Sliding Window
You are given an array nums and a sliding window of size k.

The window moves from left to right by one position.

Return the maximum element in each window.

This problem is important for:

Deque usage
Sliding window optimization
Monotonic queue
Efficient list processing

Target Complexity:

O(n)

Naive solutions with nested loops are too slow.

Example 1
Input:
nums = [1,3,-1,-3,5,3,6,7]
k = 3

Output:
[3,3,5,5,6,7]
Example 2
Input:
nums = [1]
k = 1

Output:
[1]
Example 3
Input:
nums = [9,10,9,-7,-4,-8,2,-6]
k = 5

Output:
[10,10,9,2]