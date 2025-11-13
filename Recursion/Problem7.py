'''
Reverse a string using recursion 
Problem: 
Write a recursive function to reverse a string. 
Input Format: 
A single string S. 
Output Format: 
Print the reversed string. 
Sample Input: 
hello 
Sample Output: 
olleh
'''
def reverse_string(s):
    if s == "":
        return s
    return s[-1] + reverse_string(s[:-1])
s = input()
print(reverse_string(s))
