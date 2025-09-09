n=int(input("enter a number: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("* " * 2)
