import file_stu

students = file_stu.stu_open()

subject = ['','국어','영어','수학']
subject_eng = ['','kor','eng','math']

#--------------------------------------메인화면 함수-------------------------------------#
def stu_main():
    print('-'*35)
    print('\t'+'[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*35)
    choice = input('원하는 번호를 입력하시오 0.종료 >>')
    if choice.isdigit():
        print('숫자를 입력해주세요')
        choice = int(choice)
    
    return choice

#--------------------------------------1. 성적입력 함수-------------------------------------#
def stu_input():
    print('[ 학생성적입력 ]')
    cnt = len(students) + 1
    num = cnt
    name = input('이름 >>')
    kor = int(input('국어 >>'))
    eng = int(input('영어 >>'))
    math = int(input('수학 >>'))
    total = kor+eng+math
    avg = float('{}'.format(total/3))
    student = {'stuNo':num,'name':name,'kor':kor,'eng':eng,
                'math':math,'total':total,'avg':avg,'rank':0}
    students.append(student)
    print('입력하신 정보입니다.')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
        student['stuNo'],student['name'],student['kor'],student['eng'],
        student['math'],student['total'],student['avg'],student['rank']
    ))
    cnt += 1
    
#--------------------------------------2.전체출력 함수-------------------------------------#
def stu_allprint():
    print('-'*50)
    print('[ 학생성적전체출력 ]')
    print('-'*50)
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
    for i in students:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
        i['stuNo'],i['name'],i['kor'],i['eng'],
        i['math'],i['total'],i['avg'],i['rank']
        ))

#--------------------------------------3.검색출력 함수-------------------------------------#
def stu_search():
    while True:
        tmp = 0
        print('[ 학생성적검색 ]')
        search = input('검색할 학생의 이름을 입력하세요(0.종료) >> ')
        if search == '0':
            break
        
        for i in students:
            if search == i['name']:
                print(f'{search}학생의 정보가 있습니다.')
                print('-'*50)
                print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
                    i['stuNo'],i['name'],i['kor'],i['eng'],
                    i['math'],i['total'],i['avg'],i['rank']
                    ))
                print('-'*50)
            else:
                tmp += 1
        
        if tmp == len(students):
            print('학생의 정보가 없습니다. 다시 입력해주세요.')
        
#--------------------------------------4.수정 함수(메인)-------------------------------------#
def stu_update():
    print('[ 학생성적수정 ]')
    while True:
        tmp = 0
        search = input('수정할 학생의 이름을 입력하세요 (0.취소)>> ')
        if search == '0':
            break
        
        for i in students:
            if search == i['name']:
                print(f'{search}학생의 정보가 있습니다.')
                print('-'*50)
                print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
                    i['stuNo'],i['name'],i['kor'],i['eng'],
                    i['math'],i['total'],i['avg'],i['rank']
                    ))
                print('-'*50)
            else :
                tmp += 1
        
        if tmp == len(students):
            print(f'입력하신 {search}학생의 정보가 없습니다.다시 입력해주세요.')
        
        else:
            s_update = input('수정할 과목을 선택하세요 (1.국어 / 2.영어 / 3.수학)>> ')
       
            if s_update.isdigit():
                s_update = int(s_update)
                
            if s_update == 0:
                break
           
            if s_update == 1:
                stu_update_suject(search,s_update)
            if s_update == 2:
                stu_update_suject(search,s_update)
            if s_update == 3:
                stu_update_suject(search,s_update)           
        
#--------------------------------------4.수정 함수(수정문)-------------------------------------#
def stu_update_suject(search,s_update):
    
        up_sub = input(f'수정할 {subject[s_update]} 점수를 입력하세요 >> ')
        if up_sub.isdigit():
            up_sub = int(up_sub)
        
        for i in students:
            if i['name'] == search:
                i[subject_eng[s_update]] == up_sub
                i[subject_eng[s_update]] = up_sub
                i['total'] = i['kor']+i['eng']+i['math']
                i['avg'] = i['total'] / 3
                
        
        print(f'{subject[s_update]} 점수가{up_sub}로 수정되었습니다.')
        for i in students:
            if search == i['name']:
                print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                print('-'*50)
                print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
                    i['stuNo'],i['name'],i['kor'],i['eng'],
                    i['math'],i['total'],i['avg'],i['rank']
                    ))
                print('-'*50)

#--------------------------------------5.등수처리 함수-------------------------------------#
def stu_rank():
    print('[ 학생성적 등수처리 ]')
    for i in students:
        i['rank'] = 1
        for j in students:
            if i['total'] < j['total']:
                i['rank'] += 1
        # print(i)
        
    stu_allprint()

#--------------------------------------6.학생삭제 함수-------------------------------------#
def stu_delete():
    print('[ 학생 삭제 ]')
    while True:
        tmp = 0
        search = input('삭제할 학생의 이름을 입력하세요 (0.취소)>> ')
        if search == '0':
            break
        
        for i in students:
            if search == i['name']:
                print(f'{i['name']}학생이 존재합니다.')
                del_choice = input('삭제하시겠습니까? (1.삭제 / 0.취소)>> ')
                if del_choice == '1':
                    del students[tmp]   
                    print('삭제되었습니다.') 
                    for i in students:
                        print('-'*50)
                        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t순위')
                        print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
                            i['stuNo'],i['name'],i['kor'],i['eng'],
                            i['math'],i['total'],i['avg'],i['rank']
                            ))
                        print('-'*50)
                elif del_choice == '0':
                    break        
                else :
                    print('잘못입력하셨습니다.')
                    break
               
            else : 
                tmp += 1
        
        if tmp == len(students):
            print(f'입력한 {search} 학생에 대한 정보가 없습니다.')
                              
#--------------------------------------본문-------------------------------------#

while True: 
    choice = stu_main()

    if choice == 0:
        print('종료되었습니다.')
        break
    
    elif choice == 1:
        stu_input()
        
    elif choice == 2:
        stu_allprint()
        
    elif choice == 3:
        stu_search()
        
    elif choice == 4:
        stu_update()
        
    elif choice == 5:
        stu_rank()
        
    elif choice == 6:
        stu_delete()


    
    

    
    
    
    
    