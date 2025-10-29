T= int(input())
result=[]
for i in range(T):
    s= input()
    if s==s[::-1]:
        result.append(1)
    else:
        result.append(0)
for r in result:
    print(r)