# 선택정렬
'''
li = [8,6,4,1,2,3,5,10,9,7]

for i in range(len(li)):
    print(li)
    m_index = i
    
    for j in range(i, len(li)):
        if li[j] < li[i]:
            i = j
    li[m_index], li[i] = li[i],li[m_index]

print(li)
'''


# 버블정렬

li = [8,6,4,1,2,3,5,10,9,7]
for i in range(len(li)): # i가 0일때 j의 변화
    
    for j in range(len(li)-i-1): # 0~8-i // 1~8 // 2~8 // 3~8 // 4~8 // 5~8 // 6~8 // 7~8 // 8~8
        if li[j] > li[j+1]: # 8 > 6 // 8 > 4 // 8>1 // 8>2 // 8>3 // 8>5 // 8>10 // 10>9 // 10>7
            li[j], li[j+1] = li[j+1], li[j] # 6, 8 // 6,4,8 // 6,4,1,8 // 6,4,1,2,8 // 6,4,1,2,3,8 // 6,4,1,2,3,5,8, 6,4,1,2,3,5,8,10 //6,4,1,2,3,5,8,9,10 // 6,4,1,2,3,5,8,9,7,10 

        print(li)    

print(li)
