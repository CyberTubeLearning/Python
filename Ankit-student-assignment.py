d = {}
stu = int(input("Enter the number of students:"))
for i in range (stu):
    roll_no = int(input("Enter the roll number of students:"))
    name = str(input("Enter the name of students:"))
    sub1 = str(input("Enter the name of subject:"))
    sub1marks = int(input("Enter the marks:"))
    sub2 = str(input("Enter the name of second subject:"))
    sub2marks = int(input("Enter the marks:"))
    sub3 = str(input("Enter the name of third subject:"))
    sub3marks = int(input("Enter the marks:"))
    totalmarks = sub1marks+sub2marks+sub3marks
    percentage = totalmarks/3
    CGPA = percentage/9.5
    print('you got',percentage,"%")
    print("CGPA of students",CGPA)
    d[roll_no] = {name:{sub1:sub1marks,sub2:sub2marks,sub3:sub3marks}}
    print(d)


    students_pass = percentage>40
    if students_pass is True:
        print(name,"passed")
    else:
        print(name,"not get sufficient marks")


    subjectw = sub1marks/stu
    print('subject wise average of subject 1:',subjectw)
    subjectw2 = sub2marks/stu
    print('subject wise average of subject 2:',subjectw2)
    subjectw3 = sub3marks/stu
    print('subject wise average of subject 3:',subjectw3)