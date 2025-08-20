N = int(input("Enter a number: "))
sum_digits = 0
while (N > 0):
    digit = N % 10
    sum_digits += digit
    N = N // 10
print("Sum of digits:", sum_digits)

