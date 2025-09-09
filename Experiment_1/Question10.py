n = int(input("Enter the number: "))
for i in range(n):
    stars = 2 * (n - i) - 1
    print("* " * stars)
