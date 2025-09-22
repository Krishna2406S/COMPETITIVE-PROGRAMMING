n=int(input())
code=list(map(int, input().split()))
m=[]
count=0
for i in code:
    if code.count(i)==1:
        m.append(i)
if m:
    print(*m)
else:
    print(-1)

