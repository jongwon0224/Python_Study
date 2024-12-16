# 자료형이란 => 데이터의 종류
'''
자료형 결정 x => 파이썬 내부에서 자동으로 적용 (자바스크립트처럼)
자료형 확인 => type()함수로 알수있음
'''
a,b = 1,2

print(a + b) # 3
print(a - b) # -1
print(a * b) # 2
print(a / b) # 0.5
print(a // b) # 0 -> a를 b로 나눈 몫
print(a % b) # 1 -> 나머지
print(a ** b) # 1 -> a의 b 제곱

print(4/2) # 2.0 -> float타입으로 출력됨 (Java처럼 4+2.0같이 강제 형변환도 되는듯)
#---------------------------------------------------------------------------------------------

# 논리형 true or false
# x or y
# x and y
# not x = x가 참이면 거짓, 거짓이면 참
x, y= 10, -10
print(x > 0 or y > 0) #true
print(x > 0 and y > 0) #false
print(not x > 0) #false

#문자열형
a = 5
b = '5'
c = 5.0

print(a+a) #5+5 = 10
print(b+b) #55 Str
print(a*b) #55555 Str(5)*5

'''
#오류사항
print(a+b) #int + str은 오류 -> 문자열과 숫자열은 못더함
print(b*c) #str * float은 오류 -> 실수는 문자열에 곱하기 불가, 정수는 가능
'''
#---------------------------------------------------------------------------------------------
#군집 자료형 종류
# list = 데이터를 순차적으로 저장 -> 열거형 
# tuple = 값을 변경할 수 없는 열거형 집합
# set = 순서가 없고 중복이 허용되지 않는 집합
# dictionary = 키와 값의 쌍으로 구성된 집합

#자료형 변환 방법 : 원하는 자료형 함수에 값을 넣으면 됨 (javaScript랑 비슷)
# Str(10) => 10을 문자형으로 변환
# int('10') => 문자 10을 int로 변환
# int(12.5) => float를 int로 변환
# list('hello') => 문자hello를 리스트로 변환

a = input('숫자를 입력하세요') #7입력시 문자열 7로 입력됨
print(a+a) # 77 출력

#int로 변환
a = int(input('숫자를 입력하세요'))
print(a+a) #14

#float로 변환
a = float(input('숫자를 입력하세요'))
print(a+a) #14.0

#list로 변환
a = list(input('숫자를 입력하세요'))
print(a+a) #['7','7']