#json다루기 (파일생성 & 읽기기)
#json파일 생성하기

import json

li = [
    {'name' : '홍길동', 'kor' : 77, 'eng' : 90, 'mat' : 70}, 
    {'name' : '김철수', 'kor' : 87, 'eng' : 82, 'mat' : 84}, 
    {'name' : '이영희', 'kor' : 90, 'eng' : 85, 'mat' : 74}
    ]

# dump => 던지다 
# with open(경로) as 변수명: => f.close()안해도됨
with open('c:/test/abc.json', 'w') as f:
    json.dump(li, f, ensure_ascii=False) #json을 던져라(li를 f로, 아스키코드 false (한글보존)



#json 읽기
import json

with open('c:/test/abc.json', 'r') as f:
    info = json.load(f)
print(info) #json파일 한번에 출력됨됨

#데이터 뽑아쓰기
#for 키, 값 in 딕셔너리.items():
#     반복할 코드

for i in info:
    print(i) #{'name': '홍길동', 'kor': 77, 'eng': 90, 'mat': 70}
    for k, v in i.items(): #key, value값 뽑을때 사용
        print(k, v) #name 홍길동, kor 77, eng, 90, mat 70
    print('-'*30)