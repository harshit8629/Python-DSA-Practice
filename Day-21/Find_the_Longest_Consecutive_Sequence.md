# Find the Longest Consecutive Sequence
Description

Given an unsorted list of integers nums, find the length of the longest sequence of consecutive integers.

A consecutive sequence contains numbers that follow each other continuously without gaps.

The numbers do not need to appear next to each other in the original list. You only need to determine the longest possible consecutive chain that can be formed using the elements in the list.

Your task is to return the length of the longest consecutive sequence.

You should ignore duplicate values while forming the sequence.

Example 1
Input
nums = [100, 4, 200, 1, 3, 2]
Output
4
Explanation

The consecutive sequence is:

1, 2, 3, 4

Its length is:

4
Example 2
Input
nums = [9, 1, 4, 7, 3, 2, 6, 8, 0]
Output
5
Explanation

The longest consecutive sequence is:

0, 1, 2, 3, 4

Length:

5

Another sequence is:

6, 7, 8, 9

But its length is only 4.

Example 3
Input
nums = [1, 2, 2, 3, 4, 5]
Output
5
Explanation

Duplicate 2 is ignored.

The consecutive sequence is:

1, 2, 3, 4, 5

Length:

5