a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if (a <= b and a <= c):
    minimum = a
elif (b <= a and b <= c):
    minimum = b
else:
    minimum = c

print("The minimum number is:", minimum)
