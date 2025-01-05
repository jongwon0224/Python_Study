# 선형 탐색
# n에 맞는 인덱스값 출력력
'''
li = [1,6,4,2,3,10,8,7,5,9]
n = int(input('1~10까지 입력:'))

for i in range(len(li)):
    if li[i] == n:
        print(i)
        break
'''

# 이진 탐색
li = [1,3,5,6,8,9,13,15,17,19]
n = int(input('1,3,5,6,8,9,13,15,17,19: '))

s_index = 0
e_index = len(li)-1 #9

while s_index <= e_index: # 0 < 9  // 2. # 5 < 9
    m_index = (s_index + e_index) // 2 # 중간인덱스 : 4  // 2. # 7
    
    if n < li[m_index]: 
        e_index = m_index - 1 
    elif n > li[m_index]: #n이 15일 경우 -> 6 (li[m_index])보다 크기때무네
        s_index = m_index +  1 # s인덱스 = 5 (m_index + 1)이 됨됨
    else :
        print(m_index) # li[m_index] == n이여서 출력력
        break
