n = int(input("Number of Student: "))
A = list(map(int, input("Enter the marks of students: ").split()))
Count_Pass = 0
Count_Fail = 0
for i in range(len(A)):
    if A[i]>=35:
        Count_Pass+=1  
    else:
        Count_Fail+=1
print(Count_Pass , Count_Fail)
