A = list(map(int,input("Enter the List: ").split()))
B = int(input("Enter the Target Number: "))
for i in A:
    if i == B:
        print("1")
    else:
        print("0")
    break