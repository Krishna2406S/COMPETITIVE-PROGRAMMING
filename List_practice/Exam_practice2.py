n=int(input())
A=list(map(int, input().split()))
even= []
for i in range(len(A)):
    if A[i]%2==0:
        even.append(A[i])
if even:
    print(even)
else:
    print(-1)
        