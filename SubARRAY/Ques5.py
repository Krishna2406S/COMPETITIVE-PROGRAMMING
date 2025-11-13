'''
Problem Statement 
Given an integer array nums, find the subarray with the largest sum, and return its sum. 
Input Format 
● First line: integer N 
● Second line: N integers (array elements) 
Output Format 
● Print the maximum subarray sum. 
Example 
Input: 
8 -2 1 -3 4 -1 2 1 -5 4 
Output: 
6 
Explanation 
The subarray [4, -1, 2, 1] has the largest sum = 6.
'''
N = int(input())
arr = list(map(int, input().split()))
max_sum = arr[0]
current_sum = 0
for num in arr:
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0
print(max_sum)