# 최소값 구하기
'''
li = list(map(int, input('숫자여러개:').split()))

print(min(li)) # min함수로 최소값 구하기

# 알고리즘 활용하기
m = li[0]

for i in li:
    if i < m:
        m = i

print(m)
'''

# 최대값 구하기
li = list(map(int, input('숫자여러개:').split()))

print(max(li)) # max함수 사용

# 알고리즘 사용
m = li[0]

for i in li:
    if i > m:
        m = i
print(m)