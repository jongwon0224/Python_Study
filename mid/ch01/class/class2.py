# class에서 input값 받기
class  Person:
    def __init__(self):
        self.name = input('이름입력 :')
        self.age = int(input('나이입력 :'))
    def getInfo(self):
        print(self.name + ':' + str(self.age))

# 리스트만들어서 입력값 for문 사용해서 리스트값으로 넣기
li = []
for i in range(3):
    li.append(Person())

# 리스트 요소값 출력
for i in li:
    i.getInfo()