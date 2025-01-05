# class접근제한자 -> 변수에 __사용 (self._-eng)
'''
class Sj:
    def __init__(self):
        self.kor = 90
        self.__eng = 77
        self.math = 88
    def getScore(self):
        print(self.__eng)
s1 = Sj()
print(s1.kor)
# print(s1.eng) 접근제한 걸려서 오류나옴

s1.getScore() # 메소드내 __eng하면 됨됨
'''

# setter getter 사용해서 클래스내 값 입/출력함 == JAVA와 같음
class Sj:
    def __init__(self):
        self.__eng = 77

    def getEng(self):
        return self.__eng
    def setEng(self, eng):
        self.__eng = eng

s1 = Sj()
s1.setEng(100)
print(s1.getEng())