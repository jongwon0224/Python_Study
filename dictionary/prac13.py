# 딕셔너리 -> 자바스크립트 객체 -> {key : value}

#딕셔너리 만들기
'''
dic = {}
dic = dict()
'''

# 딕셔너리 특징
dic = {'kor' : 80, 'eng' : 90, 'mat' : 77}

dic['sport'] = 50 # 키값 추가 + 밸류값 추가

'''
print(dic['sport']) # 50
print(dic['kor']) #80
print(dic['eng']) #90
print(dic['mat']) #77
print(dic[0]) # 오류
'''
'''
del dic['mat'] #키 + 밸류 삭제
print(dic)
'''
'''
dic.clear() #전체삭제
print(dic)

print('eng' in dic) #false

print(len(dic)) #3

print(dic.keys()) #dict_keys(['kor', 'eng', 'sport'])

a = set(dic)
print(a)

a = list(dic.keys()) #list형태로 변환
b = tuple(dic.keys()) #튜플형태로 변환
print(a, b)


print(dic.values()) #dict_values([80, 90, 50])
print(dic.items()) #dict_items([('kor', 80), ('eng', 90), ('sport', 50)])

print(dic)
# list(dic) 키값만 가져와서 리스트로 바꿈
list(dic.values()) #value값을 따로 변환해야됨
'''

#딕셔너리로 타입 변환 (2개씩 있으면 가능 -> 3개는 불가)

li = ['ab','cd','ef'] #2개씩 리스트형태일 경우 -> 딕셔너리로 변환 가능
print(dict(li)) # {'a': 'b', 'c': 'd', 'e': 'f'}

li = [['a',1],['b',2],['c',3]] # 배열로 2개씩 묶여있을 경우도 딕셔너리로 변환 가능
print(dict(li)) # {'a': 1, 'b': 2, 'c': 3}
