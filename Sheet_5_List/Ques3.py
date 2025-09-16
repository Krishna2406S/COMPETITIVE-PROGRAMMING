A = list(map(int,input("Enter the list: ").split()))

ans=-float("inf")
ans1=+float("inf")
for i in A:
    if (ans<i):
        ans=i

for i in A: 
    if (ans1>i):
        ans1=i
print(ans, ans1)