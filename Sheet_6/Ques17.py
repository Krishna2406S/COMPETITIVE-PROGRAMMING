''' Akash likes playing with strings. One day he thought of applying following operations on the
 string in the given order:
 Concatenate the string with itself.
 Delete all the uppercase letters.
 Replace each vowel with '#'.
 You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the
 resultant string after applying the above operations.
 NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
 Input:
 A="aeiOUz"
 Output:
 "###z###z"
 '''


A="aeiOUz"
b=A+A
res=" "
for i in range(0,len(b)):
    if b[i] not in 'AEIOU':
        if b[i] in 'aeiou':
            res+='#'
        else:
            res+=b[i]
print(res)
