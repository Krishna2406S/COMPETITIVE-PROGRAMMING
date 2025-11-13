'''
 Find Nth Fibonacci number 
Problem: 
Write a recursive function to find the Nth Fibonacci number. 
Input Format: 
A single integer N. 
Output Format: 
Print the Nth Fibonacci number. 
Sample Input: 
6 
Sample Output: 
8
'''
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))