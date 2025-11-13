'''
Sum of first N natural numbers 
Problem: 
Write a recursive function to find the sum of the first N natural numbers. 
Input Format: 
A single integer N. 
Output Format: 
Print the sum of the first N natural numbers. 
Sample Input: 
5 
Sample Output: 
15
'''
def sum_natural(n):
    if n == 1:
        return 1
    return (sum_natural(n-1)+n)

N = int(input())
print(sum_natural(N))

