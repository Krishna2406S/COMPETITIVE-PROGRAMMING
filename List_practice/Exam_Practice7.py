n = int(input())
l = list(map(int,input().split()))
increased_days=0
if len(l)!=n:
    print("Error")
increased_count=0
for i in range(1,len(l)):
    if l[i] > l[i-1]:
        increased_count +=1
print(increased_count)

    
