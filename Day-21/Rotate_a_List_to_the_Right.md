# Rotate a List to the Right
Description

Given a list of integers nums and an integer k, rotate the list to the right by k steps.

A rotation means shifting every element of the list to the right side. Elements that move beyond the last index should wrap around and appear at the beginning of the list.

Your task is to return the rotated list after performing the operation exactly k times.

If k is greater than the size of the list, rotation should continue cyclically. This means rotating a list of size n by k steps is equivalent to rotating it by k % n steps.

You must preserve the order of elements during rotation.

Example 1
Input
nums = [1, 2, 3, 4, 5]
k = 2
Output
[4, 5, 1, 2, 3]
Explanation

After 1 rotation:

[5, 1, 2, 3, 4]

After 2 rotations:

[4, 5, 1, 2, 3]

So the final rotated list is:

[4, 5, 1, 2, 3]
Example 2
Input
nums = [10, 20, 30, 40]
k = 5
Output
[40, 10, 20, 30]
Explanation

The size of the list is 4.

Rotating by 5 steps is the same as rotating by:

5 % 4 = 1

After 1 rotation:

[40, 10, 20, 30]
Example 3
Input
nums = [7, 7, 7, 7]
k = 3
Output
[7, 7, 7, 7]
Explanation

All elements are the same, so the list remains unchanged after rotation.