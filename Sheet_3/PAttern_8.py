N = int(input("Enter a number: "))
for i in range(1, N + 1):
    for j in range(i - 1):
        print("_", end="")
    for j in range(N - i + 1):
        print("*", end="")
    print()