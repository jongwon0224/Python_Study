#클래스 상속과 다형성

#부모클래스 설계 => display메소드는 pass -> 자식클래스에서 설정할거기 때문
class Point:
    def __init__(self):
        self.x = int(input('x = '))
        self.y = int(input('y = '))
    def display(self):
        pass
#사각형 클래스
class Rect(Point):
    def __init__(self):
        super().__init__()
        self.w = int(input('width = '))
        self.h = int(input('height = '))
    def display(self):
        print('사각형', self.x, self.y, self.w, self.h)
#원 클래스
class Circle(Point):
    def __init__(self):
        super().__init__()
        self.r = int(input('radius = '))
    def display(self):
        print('원',self.x, self.y, self.r)
#메인 메소드
def main():
    li = list()
    while True:
        s=input('1.사각형 2.원 3.조회 4.종료:')
        if s == '1':
            li.append(Rect())
        if s == '2':
            li.append(Circle())
        if s == '3':
            for i in li:
                i.display()
        if s == '4':
            print('프로그램을 종료합니다.')
            break

main()