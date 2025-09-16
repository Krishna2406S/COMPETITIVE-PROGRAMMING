A = list(map(int,input("Enter the List: ").split()))
B = []
for i in range(len(A)):
    B.append(A[i] ** 2)

print("Input Array A:", A)
print("Output Array B:", B)