num= int(input("Enter the number: "))
sum=0
for i in range(2,num+2,2):
    sum=sum+i
print("Sum of even numbers from 1 to", num, "is:", sum)