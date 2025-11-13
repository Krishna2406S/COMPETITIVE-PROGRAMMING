"""
Print numbers from N to 1 
Problem: 
Using recursion, print numbers from N to 1. 
Input Format: 
A single integer N. 
Output Format: 
Print numbers from N to 1 separated by a space. 
Sample Input: 
5 
Sample Output: 
5 4 3 2 1 
"""
def num(n):
    if n == 0:
        return 
    print (n)
    num(n-1)
n=int(input())
num(n)
