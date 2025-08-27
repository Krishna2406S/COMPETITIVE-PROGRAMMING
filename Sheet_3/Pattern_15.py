N=int(input("enter a number: "))
for i in range(0,N+1):
   for j in range(i):
       print("*",end=" ")
   print()
for i in range(1, N+1):
    for j in range(i-1,N-1):
       print("*",end=" ")
    print()