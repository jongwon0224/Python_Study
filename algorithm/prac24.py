# 계단
# python에서 문자열 + 숫자는 안되기때문에 -> end =''를 사용하면 두 문장을 붙혀줌
# ex. print('hello, end='') print('hi') => hellohi됨
'''
n = int(input('n:'))
c = '*'

for i in range(n):
    print(' ' * i, end='')
    print(c * n)
'''
'''
# 별찍기
n = int(input('n:'))

for i in range(n+1):
    print('*' * i)

# 거꾸로 별찍기 응용
for i in range(n+1):
    print(' ' * (n-i), end='')
    print('*' * i)
'''

#역삼각형
#두개똑같음 -> range값에 따라 코드가 다름
'''
n = int(input('n:'))

for i in range(n, 0, -1):
    print('*' * i)
    
    
for i in range(n, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * i)    
    
for i in range(n):
    print('*' * (n-i))
    
for i in range(n):
    print(' ' * i, end='')
    print('*' * (n-i))
'''

# 피라미드
'''
n = int(input('n:'))

for i in range(n):
    print(' ' * (n-i), end='')
    print('*' * (i*2 + 1)) #별의 개수는 홀수로 필요함
'''

