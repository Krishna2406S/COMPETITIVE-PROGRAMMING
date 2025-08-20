percentage = float(input("Enter your percentage: "))
if (percentage >= 85):
    grade = "A+"
elif (65 >= percentage <85):
    grade = "A"
elif (45 >= percentage <65):
    grade = "B"
elif (25 >= percentage <45):
    grade = "C"
elif (percentage < 25 ):
    grade = "D"
else:
    grade = "F (Fail)"

print("Your grade is:", grade)
