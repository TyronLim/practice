students = []
cnt = 0
while True: # 입력>출력>검색>삭제>수정
    print('-'*35)
    print('\t'+'[학생성적프로그램]')
    print('1. 학생성적입력') #####이름, 국, 영, 수 점수를 입력은 받으면 # [번호,이름,국,영,수,총합,평균,0]
    print('2. 학생성적수정') # 국, 영, 수 점수를 수정해 볼 수 있음. # (유의:국어를바꾸면, 합,평균)
    print('3. 학생성적삭제') # 도전!!
    print('4. 학생성적전체출력')  ####### 전체 출력 !!!!!!
    print('5. 학생검색출력') # 도전!!
    print('6. 등수처리')   # 얘빼고 다 할 수 는 있음.        
    print('0. 프로그램종료')  ####### 종료 !!!!
    print('-'*35)
    choice = input('원하는 번호를 입력하세요.>>')
    if choice.isdigit():
        choice = int(choice)
    
    if choice == 1:
        cnt += 1
        name = input('학생 이름을 입력하세요 >> ')
        kor = int(input('국어 성적 >> '))
        eng = int(input('영어 성적 >> '))
        math = int(input('수학 성적 >> '))
        tot = kor + eng + math
        avg = tot/3
        rank = 0
        stu = [cnt, name, kor, eng, math, tot, avg, rank]
        print(stu)
        students.append(stu)
        
    elif choice == 2:
        print('[학생 성적 수정을 선택하셨습니다.]')
        search2 = input('수정할 학생의 이름은 입력해주세요 >> ')
        k = 0
        for i in students:
            if search2 in i[1]:
                print('{}학생이 선택되었습니다.'.format(search2))
                fix = int(input('이름 >> 1, 국어 >> 2, 영어 >> 3, 수학 >> 4 >'))
                if fix == 1:
                    fixName = input('변경할 이름을 입력해주세요 >> ')
                    i[1] = fixName
                    print('{} > {} 변경되었습니다.'.format(i[2],fixName))
                elif fix == 2:
                    fixKor = int(input('변경할 국어 점수를 입력하세요 >> '))
                    i[2] = fixKor
                    i[5] = fixKor + i[3] + i[4]
                    i[6] = i[5]/3
                    print(i)
                elif fix == 3:
                    fixEng = int(input('변경할 영어 점수를 입력하세요 >> '))
                    i[3] = fixEng
                    i[5] = i[2] + fixEng + i[4]
                    i[6] = i[5]/3
                    print(i)
                elif fix == 4:
                    fixMath = int(input('변경할 수학 점수를 입력하세요 >> '))
                    i[3] = fixMath
                    i[5] = i[2] + i[3] + fixMath
                    i[6] = i[5]/3
                    print(i)
                k = 1
        if k == 0:
            print('입력한 학생의 정보가 없습니다.')
            
    elif choice == 3:
        print('[학생 삭제를 선택하셨습니다.]')
        delName = input('삭제할 학생의 이름을 입력해주세요 >> ')
        q = 0
        for i,j in enumerate(students):
            if delName in j:
                del(students[i])
                print('삭제되었습니다')
                q = 1
        if q == 0:
            print('학생 정보가 없습니다.')
        
            
    elif choice == 4:
        print('[ 전체 학생 성적 ]')
        print('[ 전체 학생 성적 ]')
        print('-'*60)
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*60)
        for i in range(len(students)):
                print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
                    students[i][0], students[i][1], students[i][2], students[i][3],
                    students[i][4], students[i][5], students[i][6], students[i][7]
                    ))
        print('-'*60)
                
    elif choice == 5:
        search = input('검색할 학생 이름 >> ')
        k2 = 0
        for i in students:    
            if search in i[1]:
                print('[{}학생을 선택하셨습니다.]'.format(search))
                print('-'*60)
                print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
                print('-'*60)
                print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
                    i[0], i[1], i[2], i[3],i[4], i[5], i[6], i[7]
                    ))
        if k2 == 0:
            print('[{}학생의 정보가 없습니다.]'.format(search))
    
    elif choice == 0:
        print('프로그램이 종료되었습니다.')
        break