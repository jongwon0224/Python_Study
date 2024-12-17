# if문 
'''
if 조건 :
    실행코드

num = int(input('숫자하나입력:'))

if num > 0:
    print(f'{num}은(는) 양수입니다.')
    # print('{}은(는) 양수입니다.'.format(num))
'''

#if ~ else문
'''
num = int(input('숫자하나입력:'))

if num % 2 == 0:
    print(f"{num}은 짝수입니다.")
else :
    print(f"{num}은 홀수입니다.")
'''

# if ~ elif문 (else if)
'''
age = int(input('나이입력:'))

if age <= 7:
    print(f'{age}살 유아입니다.')
elif age <= 19:
    print(f'{age}살 청소년입니다.')
elif age >= 20:
    print(f'{age}살 성인입니다.')
'''

# if ~elif ~ else문 (if ~ else if ~ else)

text = input('알파벳 입력:')

if text.isupper():
    print('대문자')
elif text.islower():
    print('소문자')
else:
    print('대/소문자 구분 불가능')