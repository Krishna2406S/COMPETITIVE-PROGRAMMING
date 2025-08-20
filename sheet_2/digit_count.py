num= int(input("Enter the number: "))
digit=0
while(num>0):
    num=num//10
    digit=digit+1
print(digit)
