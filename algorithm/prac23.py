#등차 수열
# 앞 항에 일정한 수를 더해 만드는 수열
#3, 8, 13, 18, 23, 28...n번째 항 구하기
# a를 일정한 값을 더해서 n이 되는 구간이면 합계가 얼마인지
'''
n = int(input('숫자입력:'))
a = 3

for i in range(n-1):
    a += 5

print(a)
'''
# 등비 수열
# 앞 항에 일정한 수를 곱해 만드는 수열
# 3,6,12,24,48,96 ....n번째 항 구하기
'''
n = int(input('숫자입력:'))
a = int(input('숫자입력a:'))
b = int(input('곱하는숫자:b'))
for i in range(n-1):
    a *= b
    
print(a)
'''

# 피보나치 수열
# 바로 앞의 두개의 항을 더해 만드는 수
# 1,1,2,3,5,8,13 ...n번째 항 구하기
n = int(input('n:'))

a,b = 1,1

for i in range(n-2):
    c = a+b
    a = b
    b = c
    
print(b)