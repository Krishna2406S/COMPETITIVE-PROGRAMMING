arr = list(map(int,input("Enter the list: ").split()))
N = len(arr)
sum = 0
for i in range(N):
    sum = sum + arr[i]
print(sum)