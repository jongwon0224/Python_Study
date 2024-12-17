#문자열 다루기
# 파이썬은 문자열도 인덱스가있음...신기

#문자열 인덱스
'''
text = 'abc'

print(text[0]) #a
print(text[1]) #b
print(text[2]) #c

print(text[-1]) #c
print(text[-2]) #b
print(text[-3]) #a
'''

#문자열 슬라이스
'''
text = 'abc defg hijk'

print(text[0:3]) #abc
print(text[:3]) #abc
print(text[3:]) # defg hijk
print(text[-5:]) #hijk
print(text[:]) #전체출력
print(text[0:8:2]) #0부터 7까지 2칸 간격으로 출력 -> acdf
print(text[8:0:-1]) #8에서부터 0까지 거꾸로 한개씩 출력 -> gfed cb
print(text[8::-1]) #8에서부터 처음까지 거꾸로 한개씩 출력 -> gfed cba
print(text[::-1]) #끝에서부터 처음까지 거꾸로 한개씩 출력 -> kjih gfed cba
'''

#1. 출력 지정 : format(a,b,c,,,) -> {}안에 format('')안에 들어간 값이 들어감
'''
text = 'abcde {} {}'
print(text.format('ABC',123)) #abcde ABC 123
'''

#2. 대체하기 : replace(a,b) -> a를 b로 바꿈
'''
text = 'abcde ABC ABC'
print(text.replace('ABC','Kk')) #abcde KBC KBC
'''

#3. 자르기 : split(a)
'''
text = 'abcde A/B/C A.B.C'
a,b,c = text.split('/') # split값 기준으로 잘라줌 -> split('.')일경우 / a = abcde A/B/C A / b = B / c = C
print(a) #abcde A
print(b) #B
print(c) #C A.B.C
'''

#4. 합치기 : a.join() -> text값 사이로 / 들어감
'''
text = 'abcde'
print('/'.join(text)) #a/b/c/d/e
'''

#5. 개수 확인하기 : count(a) -> count안에 값 개수 확인
'''
text = 'abcde ABC ABC'
print(text.count('a')) #1
print(text.count('A')) #2
print(text.count('B')) #2
'''

#6. 제거하기 : strip(a) / lstrip(a) / rstrip(a)
'''
text = '***abcde***'
print(text.strip('*')) #양쪽 별 제거
print(text.lstrip('*')) #왼쪽 별 제거
print(text.rstrip('*')) #오른쪽 별 제거
'''

#7. 인덱스 찾기 : find(a) / rfind(a) / index(a) / rindex(a)
text = 'ABC ABC'
print(text.find('A')) #0 -> 없는값 찾을때 -1리턴
print(text.rfind('A')) #4 -> 없는값 찾을때 -1리턴
print(text.index('A')) #0 -> 없는값은 오류
print(text.rindex('A')) #4 -> 없는값은 오류
