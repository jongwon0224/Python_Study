# 약수와 배수 판별
# 숫자 a,b를 입력받아 b가 a의 약수인지 확인하기 (a >= b)
# a = 8, b = 2
'''
a, b = map(int,(input('숫자입력 2개 :').split()))

# %연산자 활용
if a % b == 0 :
    print(f'({b}는 {a}의 약수입니다.)')
else :
    print('다시 확인해주세요')
'''

'''
# divmod함수 활용
c, d = divmod(a,b)
if d == 0 :
    print(f'{b}는 {a}의 약수입니다.')
else :
    print('다시확인해주세요')
'''

# 약수 구하기 => 10의 약수 : 1,2,5,10
# 숫자 n을 입력받아 n의 모든 약수 구하기
'''
n = int(input('숫자입력:'))
li = []

for i in range(1, n+1):
    if n % i == 0:
        li.append(i)

print(li)
'''

# 배수 구하기 => 10의 배수 구하기
# 숫자 n을 입력받아 n의 모든 배수 구하기 (단, 100이하)
n = int(input('숫자입력:'))
li = []

for i in range(1,101):
    if i % n == 0:
        li.append(i)

print(li)
