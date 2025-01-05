# for문
'''
for 변수 in 열거형 :
    실행코드
'''

#range() 함수 -> range(11) : 0 ~ 11-1까지 / range(1,11) : 1 ~ 11-1 / range(1,11,2) : 1 ~ 11-1, 2씩 증가
'''
print(list(range(5))) # [0,1,2,3,4]
print(list(range(1,11))) # [1,2,3,4,5,6,7,8,9,10]
print(list(range(3,10,3))) # [3,6,9]
print(list(range(5,0,-1))) # [5,4,3,2,1]
print(list(range(10,-11,-5))) # [10,5,0,-5,-10]
'''

#for문 활용
'''
for i in range(10):
    print(i) # 0~9까지 출력
'''


# 1에서 n까지 출력
'''
num = int(input('숫자를 입력해주세요:'))

for i in range(1,num+1):
    print(i)
'''

# a에서 b까지 출력
'''
a,b = map(int,(input('a b:').split()))

for i in range(a, b+1):
    print(i)
'''

# n에서 0까지 출력 => 거꾸로 출력

n = int(input('n:'))

for i in range(n, -1, -1):
    print(i)