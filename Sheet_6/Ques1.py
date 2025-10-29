'''Write a program to input T strings (S) from user and print count of vowels and consonants in it.
 Input:
 2
 List
 Apple
 '''
T=int(input("Enter number of strings: "))
for i in range(T):
    s=input()
    vowels=0
    consonants=0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
            vowels+=1
    else:
            consonants+=1
print(vowels, consonants)