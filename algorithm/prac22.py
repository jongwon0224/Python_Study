# 소수 판별하기
# 숫자 하나 입력 받아 소수인지 아닌지 확인하기
'''
n = int(input('n:'))
li = []


for i in range(1, n+1):
    if n % i == 0:
        li.append('i')

if len(li) != 2:
    print('소수아님')
else :
    print(f'({n}은(는) 소수입니다.)')
'''
'''
#  2 ~ n-1로 i값 범위 잡음 => 그중 약수가 없으면 소수
check = True

for i in range(2, n):
    if n % i == 0:
        check = False

print(check)
'''

# 범위 내의 소수 구하기
# a 값을 입력 받아 1~a사이 모든 소수값 구하기 (a>0)
a = int(input('a:'))
li = []
# 5
for n in range(2, a+1): # i = 2,3,4,5
    check = True

    for i in range(2, n): # j = 2, 3
        if n % i == 0:
            check = False
    
    if check:
        li.append(n)

print(li)
