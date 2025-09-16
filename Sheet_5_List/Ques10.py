A = list(map(int,input("Enter the List: ").split()))
N = len(A)
for i in range(0,N//2):
    A[i],A[N-1-i] = A[N-1-i], A[i]
print(A)