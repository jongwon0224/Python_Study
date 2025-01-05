# list & 제어문 활용하기
'''
li = []

#for문으로 리스트 값 추가
for i in range(5) :
    li.append(int(input('숫자입력:'))) # 입력값 리스트에 넣기

print(li)

#for문으로 리스트 값 출력
for i in range(len(li)) : # 리스트 개수만큼 돌리기
    print(li[i])


for i in li :
    print(i)



#if문 추가
for i in range(len(li)) : # 3 5 6 7 8입력 -> 3 6 8출력
    if i%2 == 0:
        print(li[i])  # 인덱스가 짝수인 경우

print()

for i in li : # 3 5 6 7 8입력 -> 6 8출력
    if i % 2 == 0: 
        print(i) # 요소가 짝수인 경우
'''

#리스트 분리하기
li = list(input('문자입력:')) # aaa bbb ccc 입력시 -> ['a', 'a', 'a', ' ', 'b', 'b', 'b', ' ', 'c', 'c', 'c']
#li = input('문자입력').split() # aaa bbb ccc 입력시 -> ['aaa', 'bbb', 'ccc']



up = []
down = []

for i in li :
    if i.isupper() : # 대문자일 경우 up리스트에 추가
        up.append(i)
    elif i.islower() : # 소문자일 경우 down리스트에 추가
        down.append(i)

print(up)
print(down)
