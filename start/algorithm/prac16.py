# 함수란 ?
# 프로그램을 짤 때 효율을 높이기 위하여 특정 기능을 미리 만들어놓고 이름을 붙여 사용

# 함수정의 => def 함수명():
def aa(): 
    print('hi') #리턴값 없는 경우


def bb(x):
    for i in range(x): #인자값 1개 반영
        print('hello')


def cc():
    n = int(input('n:')) #인자값없음, 리턴값 있음
    print(n*2)
    return n*2


def dd(x,y): #인자 + 리턴값 있음
    print(x*y)
    return x*y
        

#함수 호출하기

re1 = aa() #hi출력
re2 = bb(3) #hello 3번출력
re3 = cc() #n=5 -> 10출력, 10리턴
re4 = dd(3,5) # 15출력, 15리턴
