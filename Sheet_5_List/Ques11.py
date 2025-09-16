A = list(map(int,input("Enter the List: ").split()))
B = list(map(int,input("Enter the List: ").split()))
sum = []
for i in range(len(A)):
    sum.append(A[i] + B[i])
print("Sum: ",sum)