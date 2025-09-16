A = list(map(int, input("Enter the list: ").split()))
B = int(input("Enter the number: "))
new_array = []
for i in A:
    new_array.append(i + B)
print("Original Array: ", A)
print("Incremented Array: ", new_array)