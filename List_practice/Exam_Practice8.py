n=int(input())
l=list(map(int,input().split()))
reverse_order=[]
for i in range(0, len(l)):
    if l[i]%5==0:
        reverse_order.append(l[i])
if reverse_order:
    print(*reverse_order[::-1])
else:
    print(-1)