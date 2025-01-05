# 약수의 개수 구하기
# n을 입력받아 n의 약수의 개수 구하기
'''
n = int(input('n:'))
count = []

for i in range(1,n+1): # for문에 iterable -> 반복가능한 객체가 들어가야됨.. 정수만 사용 불가가
    if n % i == 0:
        count.append(i)

print(count)
print(len(count))
'''
# OX개수 구하기
# text를 입력받아 o의 개수, x의 개수 구하기
'''
# 알고리즘 사용 x -> count함수를 통해서 쉽게 풀수있음
text = list(input('text:'))
print(text.count('o'))
print(text.count('x'))
'''

'''
# 1. count함수 사용 x -> 알고리즘 사용하기 (list 사용)
text = input('text:')
oList = []
xList = []

for i in text:
    if i == 'o':
        oList.append(i)
    elif i == 'x':
        xList.append(i)

print(len(oList))
print(len(xList))
'''     

'''
# 2. 알고리즘 사용하기 (list 사용 안함)
text = list(input('text:'))

o_count, x_count = 0, 0

for i in text :
    if i == 'o':
        o_count += 1
    elif i == 'x':
        x_count += 1

print(f'(o_count : {o_count}, x_count : {x_count})')
'''

# 평균 이상 개수 구하기
# 여러개의 숫자를 입력 받아 평균을 구하고 평균 이상의 숫자 개수 구하기

n = list(map(int, input('여러개숫자:').split()))
avg = sum(n) / len(n)
count = 0

for i in n:
    if i >= avg :
        count += 1

print(avg)
print(count)


