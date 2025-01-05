# 제어문 중첩
'''
# if + if
age = int(input('나이입력:'))

if age <= 7 :
    print('유아입니다')
elif age <= 19 :
    print('청소년입니다')
    if age <= 13 :
        print('초등학생')
    elif age <= 16 :
        print('중학생')
    else :
        print('고등학생')
else :
    print('성인입니다.')
'''

'''
# for + if -> if문에서 n의 배수일때 걸러줄수있을듯?
n = int(input('n:'))
for i in range(1, n+1) :
    if i % 3 == 0 :
        continue
    else :
        print(i)
'''

'''
# while + if -> num1이 num2와 같게되면 break됨
num1 = 0
num2 = int(input('n:'))

while True :
    num1 += 1
    print(num1)
    if num1 == num2 :
        break
''' 


# for + for -> 주사위 2개 경우의 수 거를수있을듯
'''
count = 0

for i in range(1,7) :
    for j in range(6,0,-1) :
        if i + j == 6:
            print(f'(i : {i}, j : {j} )')
            count += 1
        
print (count)
'''