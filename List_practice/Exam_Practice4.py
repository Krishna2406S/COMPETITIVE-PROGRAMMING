# n = int(input())
# eligible_count = 0
# for i in range(n):
#     marks, attendance = list(map(int, input().split()))
#     if marks >= 75 and attendance >=80:
#         eligible_count+=1
# print("count of eligible student for schlorship: ",eligible_count)


n = int(input())
eligible_count = 0
for i in range(n):
    data = input().split()
    marks = int(data[0])
    attendance = int(data[1])
    if marks >= 75 and attendance >=80:
        eligible_count+=1
print("count of eligible student for schlorship: ",eligible_count)
