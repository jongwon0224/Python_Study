# Tuple -> 데이터를 순차적으로 저장 & 값을 변경할 수 없음 (수정불가)

'''
#튜플 만들기  -> 변수 = 괄호 or tuple()함수
tu = ()
tu = tuple()
'''

'''
#튜플 인덱스
tu = ('a','b','c')
print(tu[0])
print(tu[1])
print(tu[2])

# 튜플에서는 변경불가 -> 에러발생
tu[2] = 'd'
print(tu[2])
'''

'''
#튜플 활용
tu = ('a','b','c')

print(tu.index('c')) #위치찾기 : 2
print('b' in tu) #확인하기 true/false반환 : true
print(len(tu))  #전체 개수(길이) 확인 : 3
print(tu.count('a')) #특정값 개수 세기 : 1


num = (5,7,9)
n1,n2,n3 = num  # 변수에 값 할당하기

print(n1) #5
print(n2) #7
print(n3) #9


a = 'hello'
b = 'world'
(a,b) = (b,a) #값 교환하기
print(a, b)


li = ['a','b','c','d','e','f']
print(tuple(li)) #리스트 -> 튜플 타입 변경

tu = ('a','b','c')
print(list(tu)) # 튜플 -> 리스트 타입 변경
'''

'''
num = (5,7,9)
num1 = ('a','b','c')

(num, num1) = (num1, num)

print(list(num)) #['a', 'b', 'c']
'''


'''
li = []
for i in range(1,11) :
    li.insert(i-1, i)
    
print(li)

print(tuple(li))
'''