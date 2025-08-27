
N=int(input("enter a number: "))
for i in range(1, N+1):
    for j in range(i-1,N):
       print("*",end=" ")
    print()