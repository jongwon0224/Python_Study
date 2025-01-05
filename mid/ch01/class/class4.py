# class 상속
class Person:
    def __init__(self):
        self.name = '황'
        self.age = 27
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def getInfo(self):
        print(self.name + ':' + str(self.age))

# 상속받는법 => class명(부모클래스)
class Korean (Person):
    def __init__(self): # super + 생성자 생성
        super().__init__()
        self.lang = '한국어'
    def getInfo(self): # 메소드 오버라이딩
        print(f'언어 : {self.lang}')

# 상속받는법 => class명(부모클래스)
class American (Person):
    def __init__(self):
        super().__init__()
        self.lang = '영어'
    def getInfo(self):
        super().getInfo() # 부모 메소드 출력
        print(f'언어 : {self.lang}') # 자식 메소드 출력

p1 = Person()
# p1.getInfo() #황 27

k1 = Korean()
k1.getInfo() #언어 : 한국어

a1 = American()
a1.getInfo() #황 27 언어 : 영어