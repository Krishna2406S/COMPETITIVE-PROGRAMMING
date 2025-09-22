n=int(input())
l=list(map(int, input().split()))
count=0
avg=sum(l)/n
for i in l:
    if i>avg:
        count+=1
print(count)
        
