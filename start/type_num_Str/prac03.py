# 숫자열 다루기

#문자1.split(문자2) : 문자2를 기준으로 문자1을 자른다.
#input입력값은 str형식임
'''
text = input('날짜 입력 yyyy.mm.dd')
y,m,d = text.split('.') #text 입력값을 '.'기준으로 자름
print(text, y, m, d) #text : 2024.12.16 / y : 2024 / m : 12 / d : 16
'''
#---------------------------------------------------------------------------------------------
#위에 값을 하나씩 int(y), int(m), int(d) 로 바꾸면 힘듬 = map사용
# map(함수, 집합형태-iterable객체)
'''
a,b,c = map(int,['1','2','3'])
print(a,b,c, a+b+c) #int형태로 변환 -> 1,2,3,6 출력

a,b,c = map(int,input('날짜입력 : yyyy.mm.dd').split('.'))
print(a,b,c, a+b+c)
'''

#위 함수 풀이
'''
text = input('아무숫자 입력 : a b c')
text = text.split(' ')
a,b,c = map(int,text)
print(a,b,c, a+b+c)
'''

#---------------------------------------------------------------------------------------------
#숫자 출력하기
x=3
y=5
'''
#숫자와 문자 함께 출력하기 (1) 콤마 & 형변환
print(x,'과',y,'의 합은',x+y,'이다')
#print(x+'과'+y+'의 합은'+x+y+'이다') 오류나옴 -> int와 str은 더할수없음

#숫자와 문자 함께 출력하기 (2) end='
print(x, end='')
print('과', end='')
print(y, end='')
print('의 합은', end='')
print(x+y, end='')
print('이다.')

#숫자와 문자 함께 출력하기 (3) format()
방법2개 -> .format() or f"{}"
print('{}과 {}의 합은 {}이다.'.format(x,y,x+y))
print(f"{x}과 {y}의 합은 {x+y}이다.")
'''
#---------------------------------------------------------------------------------------------

#반올림 : round(a), round(a,b) -> a는 대상, b는 소수점 자릿수
print(round(3.33)) #3
print(round(3.66)) #4
print(round(3.66, 1)) #3.7

#절대값 : abs(a) -> 양수는 양수, 음수는 양수로 출력
print(abs(3)) #3
print(abs(-3)) #3

#제곱 : pow(a,b) -> a는 대상, b는 제곱수
print(pow(3,2)) #9
print(3**2) #9

#나눗셈 : divmod(a,b) -> a를 b로 나눈후 몫, 나머지 출력 
x,y = divmod(7,2)
print(x) #3 -> 몫 <=> 7 // 2 몫 출력하는거 동일
print(y) #1 -> 나머지 <=> 7 % 2 나머지 출력이랑 동일

#최대값 : max(a,b,c,d...) -> list형태도 가능
print(max([1,3,5,7])) #7

#최소값 : min(a,b,c,d...) -> tuple형태도 가능
print(min(1,3,5,7)) #1

#합 : sum(집합 형태 : iterable) -> list형태나 tuple형태로 넣어야 함수실행됨
print(sum([1,3,5,7])) #16