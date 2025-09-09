N=int(input("enter a number: "))
for i in range(N,0,-1):
    for j in range(i):
       print("*",end=" ")
    print()