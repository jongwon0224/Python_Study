# 기타 제어문
'''
#continue -> 해당 단계만 건너뛰고 다음단계로
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#1~10까지 출력 (5빼고)
'''


'''
#break -> 제어문 중단 후 빠져나옴
for i in range(1,11):
    if i == 5:
        break
    print(i)

#1~4까지 출력후 중단
'''

#pass -> 아무작업안함 -> 파이썬 작업중 비워두고 싶을때 사용 (맨밑에 함수 참고)
for i in range(1,11):
    if i == 5:
        pass
    print(i)

#1~10까지 출력됨

'''
n = int(input('n:'))

if n>0 :
    pass
else :
    pass
'''