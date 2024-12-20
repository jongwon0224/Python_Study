#리스트 활용하기
'''
# 문자 입력받아 공백 기준 자르기
li1 = input('문자입력').split() #split괄호안에 빈칸 -> 공백기준으로 잘라라
print(li1) #['dd', 'ff', 'cc']
'''

'''
# 문자입력 받아 전체 자르기
li2 = list(input('문자입력')) #공백도 같이 배열에 넣어줌
print(li2) #['d', 'd', ' ', 'f', 'f', ' ', 'c', 'c']
'''
'''
#숫자 하나씩 입력받기
li3 = []

li3.append(int(input('숫자 입력:')))
li3.append(int(input('숫자 입력:')))
li3.append(int(input('숫자 입력:')))
print(li3) #[5, 7, 9]
'''
'''
#숫자 여러개 입력받기
li4 = list(map(int,input('숫자입력:').split()))

print(li4) #[579]

a = input('숫자입력').split()
b = map(int,a)
c = list(b)
print(c) #[579]
'''

#합, 평균, 최소값, 최대값, 중간값
num = list(map(int, input('숫자입력').split()))

num.sort()

print('합 :', sum(num))
print('평균 :', sum(num) / len(num))
print('최소값 :', num[0])
print('최대값 :', num[len(num)-1])
print('중간값 :', num[len(num) // 2])