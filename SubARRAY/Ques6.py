"""
Problem Statement 
Given an integer array, find the sum of all subarray sums using the Contribution Technique. 
Concept 
Each element at index i contributes to several subarrays: 
Contribution of element i=arr[i]×(i+1)×(N−i)\text{Contribution of element i} = \text{arr[i]} \times (i + 1) \times (N - i)Contribution of element i=arr[i]×(i+1)×(N−i) 
Input Format 
● First line: integer N 
● Second line: N integers (array elements) 
Output Format 
● Print the total sum of all subarray sums. 
Example 
Input: 
3 
1 2 3 
Output: 
20 
Explanation 
● For element 1: 1 × (1) × (3) = 3 
● For element 2: 2 × (2) × (2) = 8 
● For element 3: 3 × (3) × (1) = 9 
Total = 3 + 8 + 9 = 20 
"""

N = int(input())
arr = list(map(int, input().split()))
total_sum = 0
for i in range(N):
    total_sum += arr[i] * (i + 1) * (N - i)
print(total_sum)