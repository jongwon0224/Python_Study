# class사용 -> init에서 변수 초기화
# 변수에 클래스 대입

class Person: #첫글자는 대문자, 매개변수로 객체값 대입
    def __init__(self, name, age): #self는 클래스안에있는 자기자신의 객체를 지칭
        self.name = name
        self.age = age
    def display(self): # 클래스안에 메소드생성성
        print(self.name, self.age)

# 객체를 변수에 대입 = 생성자 매개변수 줌
p1 = Person('홍길동', 25)
print(p1.name, p1.age)
p1.display() #메소드 호출

p2 = Person('김철수', 27)
print(p2.name, p2.age)
p2.display() #메소드 호출

