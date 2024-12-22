#문자 체크
# 긴 문장(text)과 한 문자(t)를 입력받아
# t가 text안에 포함되어 있는지 확인
'''
text = input('text:')
t = input('t:')

#print(t in text) # A in B를 통해서 true/false를 알수있음

# 위에 함수 알고리즘으로 풀어봄
check = False

for i in text :
    if i == t :
        check = True

print(check)
'''

#숫자 체크
#5개의 숫자를 입력받아 리스트를 만들고
# n을 입력받아 리스트 값에 n이 있는지 확인

'''
#for문 사용해서 리스트에 요소 추가

list = []

for i in range(5):
    n = int(input('숫자입력'))
    list.append(n)

print(list)
'''
'''
num = list(map(int,input('숫자5개:').split()))
n = int(input('n입력:'))

check = False

for i in num :
    if i == n :
        check = True

print(check) # == print(n in num)
'''



