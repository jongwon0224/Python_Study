# 클래스변수 & 인스턴스 변수

#클래스 변수 => 자바 static변수 같은 개념 => 객체생성할때마다 변수값이 중복이 됨

#자바 => static String var; => 클래스변수
#파이썬 => li = [] (self가 안붙음) => 클래스변수

#차이점 => 자바에서 static변수값이 변하면 사용한 객체에서 모든 값이 변하는 반면 파이썬에서는 사용한 클래스값만 변함..신기 (1,2둘다 사용하고 1만 클래스변수 변경시 -> 1값만 바뀜)
'''
class Person:
    li = []
    def __init__(self,sp):
        Person.li.append(sp)
    
    def display(self):
        print(Person.li)

p1 = Person('우유')
p1.display() # ['우유']
p2 = Person('콜라')
p2.display() # ['우유', '콜라']
p3 = Person('주스')
p3.display() #['우유', '콜라', '주스']
'''
# 인스턴스 변수 => 객체마다 변수값 생김 => 변수값 중복안됨
class Person:
    def __init__(self, sp):
        self.li = []
        self.li.append(sp)
    def display(self):
        print(self.li)

p1 = Person('우유')
p1.display() # ['우유']
p2 = Person('콜라')
p2.display() # ['콜라']
p3 = Person('주스')
p3.display() #['주스']