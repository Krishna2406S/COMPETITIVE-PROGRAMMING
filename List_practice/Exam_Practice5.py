n = int(input())
ls = list(map(int, input().split()))
k = int(input())
count = 0
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if ls[i]+ls[j] == k:
            count +=1
print(count)
