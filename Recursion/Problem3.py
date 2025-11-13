"""
Print numbers from 1 to N 
Problem: 
Using recursion, print numbers from 1 to N. 
Input Format: 
A single integer N. 
Output Format: 
Print numbers from 1 to N separated by a space. 
Sample Input: 
5 
Sample Output: 
1 2 3 4 5 
"""

def num(n):
    if n == 0:
        return 
    num(n-1)
    print (n)
n=int(input())
num(n)