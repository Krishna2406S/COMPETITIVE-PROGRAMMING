N=int(input("enter a number: "))
for i in range(1,N+1):
    for j in range(N-i):
        print("_",end="")
    for j in range(i):
       print("*",end="")
    print()