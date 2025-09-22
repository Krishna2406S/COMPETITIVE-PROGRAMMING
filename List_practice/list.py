# List=[24,"Krishna",18,[6,9], True]
# print(List)
# print(List[1])
# print(List[-1])
# print(List[1][4])

# a=[9,18,24,6,4]
# b=[4,6,24,18,9]
# c=a+b
# print(c)


# ls=[9,18,24,6,4]
# N=len(ls)
# sum=0
# for i in range(N):
#     sum=sum+ls[i]
# print(sum)
    
# ls=[9,18,24,6,4]
# N=len(ls)
# sum=0
# for i in ls:
#     sum=sum+i
# print(sum)


# list=[1,2,3,4]
# list.insert(100, 200)
# print(list)


# l1= [1,3,78,95]
# l1.extend([16,54,66])
# print(l1)



# l2=[10,20,30,40,50]
# l2.remove(40)
# print(l2)

# l2=[10,20,30,40,50]
# l2.pop(2)
# print(l2)

# list=[1,4,7,30,"Python"]
# list.reverse()
# print(list)



# my_list=[100,200,3000,245,546,"Python"]
# reversed_list = list(reversed(my_list))
# print(reversed_list)

# list= [10,20,30,40,50,"Python"]
# reversed_list=list[::-1]
# print(reversed_list)

# list=[10,20,15,54,64,94]
# N = len(list)
# for i in range(0,N//2):
#     list[i],list[N-1-i] = list[N-1-i], list[i]
# print(list)


# str="Hello Everyone how are you"
# print(str.split())

# str="Hello - Everyone - how are you"
# print(str.split("-"))

# str="Krishna Kumar ; From Mirzapur"
# print(str.split(";"))

# t="5321"
# print(t.split())


# A=list(map(int, input().split()))
# print(A)

# Question: given an array compute the sum of all element.

# arr= list(map(int,input("Enter the list: ").split()))
# sum=0
# for i in arr:
#     sum =sum+i
# print("Sum of element: ",sum)

# arr = list(map(int, input("Enter numbers: ").split()))
# total = sum(arr)
# print("Sum of elements:", total)



# Question: given an array to fing maximum value in it.

# arr= list(map(int,input("Enter the list: ").split()))
# ans=-float("inf")
# for i in arr:
#     if (ans<i):
#         ans=i
# print(ans)



# Question: given an array and a target  number . find number of occerrence of target number in the given array.

# arr = list(map(int, input("Enter the list: ").split()))
# target = int(input("Enter the target number: "))
# count = 0
# for num in arr:
#     if num == target:
#         count += 1
# print(count)


# Question: Given an array and an increment a number , generate a new array which contains all values of original array increase by increment value.
# arr = list(map(int, input("Enter the list: ").split()))
# inc=int(input("Enter the number: "))
# new_array = []
# for i in arr:
#     new_array.append(i + inc)
# print("Original Array:", arr)
# print("Incremented Array:", new_array)


# Question: given an array filter out odd number.
# arr = list(map(int, input("Enter the list: ").split()))
# odd_num = []
# for num in arr:
#     if num % 2 != 0:
#         odd_num.append(num)

# print("Original array:", arr)
# print("Odd numbers only:", odd_num)


# Question: Given a list of integer and a target num . find and print index of the target number.
# arr = list(map(int, input("Enter the list: ").split()))
# target = int(input("Enter the target number: "))
# for i in arr:
#     if i == target:
#         print(i)
#         break


# arr = list(map(int, input("Enter the list: ").split()))
# target = int(input("Enter the target number: "))
# if target in arr:
#     print(arr.index(target))
# else:
#     print("Target not found")


 # Read number of products
n = int(input("Enter number of products: "))

# Read sales counts
sales = list(map(int, input("Enter sales counts separated by space: ").split()))

# Check if input length matches n
if len(sales) != n:
    print("Error: Number of sales counts doesn't match n.")
else:
    max_sales = max(sales)
    min_sales = min(sales)
    print("Max sales:", max_sales)
    print("Min sales:", min_sales)
