A = list(map(int,input("Enter the List: ").split()))
odd = []
even = []
for num in A:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
print(*odd)
print(*even)
