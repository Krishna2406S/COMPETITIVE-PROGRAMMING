'''
Problem Statement 
Given an array of integers, print all possible subarrays and their elements. 
Input Format 
● First line: integer N (size of array) 
 
● Second line: N integers (array elements) 
 
Output Format 
● Print all subarrays, one per line. 
 
Example 
Input: 
5 
1 2 3 4 5 
 
Output: 
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  
2  
2 3  
2 3 4  
2 3 4 5  
3  
3 4  
3 4 5  
4  
4 5  
5 
 
Explanation 
All continuous segments of the array are printed in order.
'''
N = int(input())
arr = list(map(int, input().split()))
for i in range(N):
    for j in range(i, N):
        subarray = arr[i:j+1]
        print(' '.join(map(str, subarray)))
