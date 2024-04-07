class Student:
    stuNo = 0
    rank = 0
    cnt = 1
    
    def __init__(self, name, kor, eng, math,stuNo=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = int(kor+eng+math)
        # self.avg = int(self.total/3)
        self.avg = float('{:.2f}'.format(self.total/3))
        if self.stuNo == 0:
            self.stuNo = Student.cnt
            Student.cnt += 1
        else:
            self.stuNo = stuNo
    
    def __str__(self):
        return f'{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}'

students = []
with open('students1.txt','r',encoding='utf8') as f:
    while True:
        stu = f.readline()
        if stu=='': break
        student = stu.strip().split(',')
        student[0] = int(student[0])
        student[2] = int(student[2])
        student[3] = int(student[3])
        student[4] = int(student[4])
        student[5] = int(student[5])
        student[6] = float(student[6])
        student[7] = int(student[7])
        students.append(student)
print(students)
        
# with open('students1.txt','r',encoding='utf8') as f:
#     while True:
#         stu = f.readline()
#         if stu=='': break
#         student = stu.strip().split(',')

#         s_list=Student(student[1],student[2],student[3],student[4],student[0])
#         students.append(Student)


# for i in students:
#     # print(i)
#     for j in i:
#         print(j,end = ' ')