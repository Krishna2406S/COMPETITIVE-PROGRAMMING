n=int(input())
l=list(map(int, input().split()))
max_count=0
current_count=0
for i in l:
    if i==0:
        current_count+=1
    else:
        if current_count>max_count:
            max_count = current_count
        current_count=0

if current_count>max_count:
    max_count = current_count
print(max_count)


