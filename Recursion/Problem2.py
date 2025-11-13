'''
Factorial of a number 
Problem: 
Write a recursive function to find the factorial of a number. 
Input Format: 
A single integer N. 
Output Format: 
Print the factorial of N. 
Sample Input: 
5 
Sample Output: 
120
'''
def fact(n):
    if n==0:
        return 1
    return fact(n-1)*n
n=int(input())  
print(fact(n))