a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if (a + b + c == 180 and a < 90 and b < 90 and c < 90):
    print("Acute Triangle")
elif (a + b + c == 180 and a < 90 and b == 90 and c < 90):
    print("Right Triangle")
elif (a + b + c == 180 and a > 90 and b < 90 and c < 90):
    print("Obtuse Triangle")
else:
    print("Invalid Triangle")
    