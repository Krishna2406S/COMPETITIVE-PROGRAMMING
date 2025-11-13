"""
 Check if a string is a palindrome 
Problem: 
Using recursion, check whether a string is a palindrome or not. 
Input Format: 
A single string S. 
Output Format: 
Print "Palindrome" if the string is a palindrome, otherwise "Not Palindrome". 
Sample Input: 
madam 
Sample Output: 
Palindrome
"""
def is_palindrome(s):
    return s == s[::-1]

S = input()
print("Palindrome" if is_palindrome(S) else "Not Palindrome")
