N=int(input("enter a number: "))
for i in range(1, N+1):
    for j in range(1,1+i):
        if(j%2==0):
            print("*", end = " ")
        else:
            print(j, end=" ")
    print()