# 주사위 -> 주사위 2개 경우의 수 뽑기 + n이 나올 경우의 수
'''
a = int(input('a:'))
b = int(input('b:'))
n = int(input('n:'))

for i in range(1, a+1):
    
    for j in range(1, b+1):
        if(i+j == n):
            print(f'(i : {i}, j : {j})')
'''            

'''
# 구구단 -> 2단부터 9단까지
for i in range(2, 10):
    
    for j in range(1, 10):
        print(f'({i} * {j} = {i * j})')
    print() # 모수가 바뀔때마다 엔터
'''

# 행렬 만들기
'''
li = [ [1,2,3,4], [5,6,7,8] ]
for i in range(len(li)):
    print(li[i])
'''

'''
# 배열 요소 하나씩 출력하는 방법
for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j])
'''