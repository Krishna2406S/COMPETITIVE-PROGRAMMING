s="Hello everyone how are you"
print(s.split())

s="Hello-everyone-how are you"
print(s.split("-"))

word='Suyash:Chaudhary:Noida'
print(word.split(':'))

t= "23456"
print(t.split())

t="2345"
print(t.split())


'''
output:
['Hello', 'everyone', 'how', 'are', 'you']
['Hello', 'everyone', 'how are you']
['Suyash', 'Chaudhary', 'Noida']
['23456']
['2345']
'''