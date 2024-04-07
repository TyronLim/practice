import random

num = [i for i in range(1,46)]
# print(num)

random.shuffle(num)
# print(num)

lotto = []
for i in range(6):
    # print(num[i])
    lotto.append(num[i])

# lotto.sort()
print(lotto)
sel_num = []
for i in range(6):
    choice = int(input(f'{i+1}번째 번호를 입력하세요 >> '))
    sel_num.append(choice)

# print(sel_num)
corr_num = []
cnt = 0
for i in lotto:
    for j in sel_num:
        if i == j:
            # print(i)
            corr_num.append(i)
            cnt += 1

corr_num.sort()
print(f'{cnt}개를 맞혔습니다.')
print('맞춘 번호 = ',corr_num)
    

