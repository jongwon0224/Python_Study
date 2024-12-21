#list

#리스트 만들기 -> 변수명 = [] or list()함수 사용
'''
li = []
li = list()

print(li)
'''
'''
#리스트 인덱스
li = ['a','b','c']

print(li)
print(li[0])
print(li[1])
print(li[2])

li[2] = 'd'
print(li[2])
'''
'''
#리스트 활용
li = ['a','b','c','d','e']

print(li.index('c')) #2 : 인덱스 위치찾기

li.append('f') # 추가하기1 -> 맨뒤에 추가 (push개념)
print(li)

li.insert(0, 'aa') # 추가하기2 -> 넣고자하는 인덱스번호에 aa추가
print(li)

li.remove('aa') #삭제하기1 -> aa삭제됨
print(li)

del li[2] #삭제하기1 -> 인덱스 번호로 삭제
print(li) 

print('b' in li) # 확인하기 -> b가 li에 있나요? -> true/false반환

print(len(li)) # 리스트 전체 개수 -> 5

print(li.count('a')) # 특정값 개수 세기 -> a는 1개

'''

num = []

for i in range(1,11) :
    num.insert(i-1, i)
    
print(num)

print(sum(num)) #55 : 합계
print(min(num)) # 1 : 최소값
print(max(num)) #10 : 최대값

num.reverse() # 거꾸로 (배열 상태 그대로 뒤집기)
print(num) 


# sort() -> 괄호안에 reverse=True면 역순 / false면 sort실행
num.sort() # 순서대로 정렬
print(num)

num.sort(reverse=True) # 내림차순으로 정렬
print(num)

