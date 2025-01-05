# 띄어쓰기 없애기
# 공백제거 및 자바 print처럼 가로로 출력
'''
text = input('text')

for i in text:
    if i != ' ':
        print(i, end='')
'''

#공백기준 잘라서 배열로 만들기
'''
b =text.split()
print(b)
'''
'''
# 대소문자 바꾸기
text = input('text')

for i in text:
    if i.isupper():
        print(i.lower(), end='')
    else :
        print(i.upper(), end='')
'''

'''
# 이름찾기
name = ['황종원','황종투', '김민희', '김철수', '안철수', '최코딩']
# i값으로 데이터 출력
for i in name:
    if '황' in i or '김' in i:
        print(i)

print()
# i의 인덱스값으로 데이터 출력
for i in name:
    if i[0] == '황':
        print(i)

'''

'''
# 이름에 '김'이 있는 경우 출력

name = ['황종원','황김투', '김민희', '김철수', '안철수', '최코딩', '윤석김']

for i in name:
    for j in range(len(i)):
        if '김' in i[j]:
            print(i)
'''