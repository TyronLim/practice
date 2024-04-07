class Student:
    stuNo = 0
    rank = 0
    cnt = 1
    
    def __init__(self, name, kor, eng, math,stuNo=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float('{:.2f}'.format(self.total/3))
        if self.stuNo == 0:
            self.stuNo = Student.cnt
            Student.cnt += 1
        else:
            self.stuNo = stuNo
    
    def __str__(self):
        return f'{self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}'


stu_list=[]
with open('students1.txt','a',encoding='utf8') as f:
    while True:
        print(stu_list)
        cnt = len(stu_list)+1
        stuNo = cnt
        name = input('이름을 입력하세요 (0.취소)>> ')
        if name == '0': break
        kor = int(input('국어점수를 입력하세요 >> '))
        eng = int(input('영어점수를 입력하세요 >> '))
        math = int(input('수학점수를 입력하세요 >> '))
        total = kor+eng+math
        avg = float('{:.2f}'.format(total/3))
        rank = 0
        stu_list.append(stuNo)
        student = f.write('{},{},{},{},{},{},{},{}\n'.format(
            stuNo,name,kor,eng,math,total,avg,rank))