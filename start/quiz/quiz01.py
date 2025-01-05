# Jump To Python 자료형 부분 문제 퀴즈
#평균구하기
'''
score = [('국어',80),('영어',75),('수학',55)]

# dict타입변경
a = dict(score)
print(a)
# 키값 리스트화
li = list(a.keys())
print(li)
# 밸류값 리스트화
scores = list(a.values())
print(scores)
# 평균값 : 밸류값 토탈 / 키값 개수
avg = sum(scores) / len(li)
print(avg) #70
'''

'''
# 13이 홀수 인지 짝수인지 구분
if 13 % 2 == 0:
    print('짝수')
else :
    print('홀수')
'''

'''
# 주민번호 생년월일 / 숫자 나누어서 출력
pin = '881120-1068234'

index = pin.find('-') #6
birth = pin[:index]
num = pin[index+1:]

print(birth, end='')
print(num)
'''

'''
#주민번호 숫자란 1,2 구분해서 남/녀 구분하기
pin = '881120-1068234'
index = pin.find('-')

if pin[index+1] == '1':
    print('남자')
else :
    print('여자')
'''

'''
#a:b:c:d -> a#b#c#d로 바꾸기
a = 'a:b:c:d'
print(a.replace(':','#'))
'''

#[1,3,5,4,2] -> [1,2,3,4,5] -> [5,4,3,2,1]로 만들기
'''
a = [1,3,5,4,2]
a.sort()
a.reverse()

print(a)
'''

'''
# a = ['Life','is','too','short'] -> 문자열로 변경하기
a = ['Life','is','too','short']
result = ' '.join(a)
print(result)
'''

# (1,2,3)튜플에 4 추가하기 -> 튜플은 값이 바뀌는게  아닌 주소복사
'''
a = (1,2,3)
b = (4,)
c = a +b
print(c)
'''

'''
# 딕셔너리에서 'B'키값, 밸류값 추출하기
a = {'A':90,'B':80,'C':70}

result = a.pop('B')
print(result)

# del a['B'] : del은 데이터 완전 삭제
print(a)
'''

'''
# 리스트에서 중복 숫자 제거하기
a = [1,1,1,2,2,3,3,3,4,4,5,5]
b = set(a)
c = list(b)

print(c)
'''

