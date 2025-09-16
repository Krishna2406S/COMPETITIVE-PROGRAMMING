A = list(map(int,input("Enter the List: ").split()))
even = 0
odd = 0
for i in A:
    if i%2==0:
        even+=1
        
    else:
        odd+=1
    result=even-odd
print(result)
