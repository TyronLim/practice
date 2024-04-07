# 메모장 생성
students = []
f=open('students.txt','w',encoding='utf8')
while True:
    txt = input('번호 >>')
    if txt == '0':
        break

    f.write(txt)
    print(txt)
    
f.close()
    
    