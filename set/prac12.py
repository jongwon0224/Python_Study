#세트 만들기 -> 세트는 순서 상관없이 들어가있음 + 중복값 없애서 만들어줌
# 특이하게 &, |, -, ^ 를 통해서 교집합, 합집합, 차집합, 대칭차집합을 구할 수 있음
'''
se = set()
print(se)
se = {} #사용 불가능
print(se)
'''

'''
# 세트 특징 (순서, 중복없음)
a = {2,4,6,8}
print(a) #순서 상관없이 들어가있음
b = {2,4,2,1,2,3}
print(b) #중복된 값 자동 없어짐 + 순서 상관없이 들어가있음

#print(a[0]) -> 인덱스로 호출 불가
'''


# 세트 활용
'''
a = {2,4,6,8}

a.add(5) # {2,4,5,6,8}
print(a)

a.remove(5) # {2,4,6,8}
print(a)

print(1 in a) # false

print(len(a)) # 4

print(sum(a)) #20
print(min(a)) #2
print(max(a)) #8

print(list(a)) #[2, 4, 6, 8]
print(tuple(a)) #(2, 4, 6, 8)
'''

a = {1,2,3}
b = {2,3,4}

print(a&b) # {2,3} : 교집합
print(a|b) # {1, 2, 3, 4} : 합집합
print(a-b) # {1} : 차집합 
print(a^b) # {1,4} : 대칭 차집합
