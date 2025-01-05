#합 구하기
#숫자 n을 입력받아 1~n까지 합 구하기
'''
# for문 사용
n = int(input('숫자입력:'))
a = 0

for i in range(1,n+1) :
    a += i

print(a)

# sum함수 사용
n = int(input('숫자입력:'))
a = []

for i in range(1,n+1) :
    a.append(i)

print(sum(a))    
'''

#곱 구하기
#숫자 n을 입력받아 1~n까지 곱 구하기
'''
import math
# for문 사용
a = 1
n = int(input('숫자입력:'))

for i in range(1, n+1):
    a = a * i

print(a)

# 팩토리얼 함수 사용
b = math.factorial(n)
print(b)
'''

#값 누적하기
#0을 입력할때까지 반복해서 숫자를 입력받아 합 구하기
'''
num = int(input('숫자입력:'))
a = 0

while num != 0 :
    a += num
    num = int(input('숫자입력:'))

print(a)
'''

'''
li = []

while True :
    num = int(input('숫자입력:'))
    li.append(num)
    print(sum(li))

    if(num == 0):
        break
'''
