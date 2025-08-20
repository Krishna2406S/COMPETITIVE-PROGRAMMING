num = int(input("Enter a number: "))
if num % 3 == 0 and num % 10 == 4:
    print(num," is divisible by 3 and its last digit is 4.")
else:
    print(num,"does not meet the conditions.")