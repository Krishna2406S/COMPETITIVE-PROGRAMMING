'''
Problem Statement 
Given an array of integers, print the sum of all possible subarrays. 
Input Format 
● First line: integer N 
 
● Second line: N integers (array elements) 
 
Output Format 
● Print the sum of each subarray, one per line. 
 
Example 
Input: 
3 
1 2 3 
 
Output: 
1 
3 
6 
2 
5 
3 
 
Explanation 
All subarrays are: 
 [1] → 1 
 [1,2] → 3 
 [1,2,3] → 6 
 [2] → 2 
 [2,3] → 5 
 [3] → 3
'''
N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    total = 0
    for j in range(i, N):
        total += arr[j]
        print(total)
