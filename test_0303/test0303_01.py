lotto = []   # 1~45까지
sel = []

from random import*

ran = []
for i in range(1,46):
    ran.append(i)

for i in range(500):
    tmp = randint(0,44)
    ran[0], ran[tmp] = ran[tmp], ran[0]

for i in range(6):
    lotto.append(ran[i])

for i in range(6):
    choice = int(input('{}번째 숫자를 입력하세요 >> '.format(i+1)))
    sel.append(choice)

ok = []

for i in range(len(sel)):
    if sel[i] in lotto:
        ok.append(sel[i])

print(lotto)
print(sel)
print('당첨된 숫자는 {}입니다.'.format(ok))
