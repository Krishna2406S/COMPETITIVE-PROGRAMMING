'''
 Count digits in a number 
Problem: 
Write a recursive function to count the digits in a number. 
Input Format: 
A single integer N. 
Output Format: 
Print the number of digits. 
Sample Input: 
12345 
Sample Output: 
5
'''

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

N = int(input())
print(count_digits(N))
