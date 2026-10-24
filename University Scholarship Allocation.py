#1-->University scholarship allocation
students=[]
marks=[]
attendance=[]
income=[]
for i in range(int(input("Enter how many students: "))):
    students.append((input("Enter your name: ")))
    marks.append(int(input("Enter your marks percentage: ")))
    attendance.append(int(input("Enter your attendance percentage: ")))
    income.append(int(input("Enter your income: ")))
eligible=[]
for j in marks:
    if j>60:
        a=marks.index(j)
        eligible.append(students[a])
print("The eligible students are: ")
for k in eligible:
    print(k,end=" ")
    b=students.index(k)
    if income[b]<80000:
        print("with scholarship of 70%")
    elif income[b]>120000:
        print("with scholarship of 50%")
    else:
        print("with scholarship of 30%")
