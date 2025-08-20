num = int(input("Enter the  number: "))
reverse_num = 0
while (num > 0):
    dig = num % 10
    reverse_num = reverse_num * 10 + dig
    num = num // 10
print("reverse number: ", reverse_num)
