
def stu_open():

    students = []

    with open('students.txt','r',encoding='utf8') as f:
        while True:
            txt = f.readline()
            if txt == '': break
            stu_list = txt.strip().split(',')
            # print(stu_list)
            student={'stuNo':int(stu_list[0]),'name':stu_list[1],'kor':int(stu_list[2]),'eng':int(stu_list[3]),
                    'math':int(stu_list[4]),'total':int(stu_list[5]),'avg':float(stu_list[6]),'rank':int(stu_list[7])}
            students.append(student)

    # print(students)
    
    return(students)
    
    
# stu_open()