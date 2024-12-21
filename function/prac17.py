#내장 모듈 => math모듈 사용하고싶으면 import math해야됨
import math
'''
#math모듈
print(math.ceil(2.1)) #3 : 올림
print(math.floor(2.1)) #2 : 내림
print(math.factorial(10)) #3628800 : 팩토리얼(10) => 1~10까지 모두 곱한값
print(math.sqrt(4)) # 2.0 : 루트
print(math.pi) #3.1415926~~ : 원주율
'''

''' 
#math.factorial(10)을 풀어서 설명

a = 1

for i in range(1, 11) :
    a = a* i
    print(a)
'''

#random모듈
import random
'''
print(random.randint(1,5)) #범위내의 정수 랜덤값 생성 -> random.randint(시작숫자, 끝숫자)
print(random.random()) #0 <= ?? < 1 랜덤값 생성
#print(int(random.random()*10))  #응용해봄


#random.choice(리스트), random.sample(리스트, 숫자), random.shuffle(리스트)
li = ['a','b','c','d','e']
print(random.choice(li)) # 리스트 값 중 하나 랜덤 뽑기
print(random.sample(li,3)) # 리스트에서 랜덤n개 뽑기

random.shuffle(li) #리스트 순서 랜덤 섞기
print(li)
'''

'''
#random은 튜플, 리스트, 세트에서도 가능
tu = ('a','b','c')
print(set(tu))

print(random.choice(tu))

#딕셔너리는 키값 or 밸류값 따로 뽑아서 다른 타입 변환 후 사용가능한듯
di = {'a' : 3, 'b' : 4, 'c' : 5}

print(random.choice(list(di.keys())))
'''