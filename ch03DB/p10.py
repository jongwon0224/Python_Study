# db에서 select해서 읽어오기

import sqlite3
from libs.db.dba import getConn

# fetchall => 데이터 모두 가져오기
# fetchmany(숫자) => 숫자만큼 가져오기

def select_a():
    conn = getConn() #dba에서 커넥션 모듈 가져오기
    cur = conn.cursor() #커넥션에서 커서 가져오기
    cur.execute('select * from test')
    print('전체 데이터 출력 하기')

    rs = cur.fetchall() #커서를 통해서 모두 가져오기
    for i in rs:
        print(i)

    conn.close()
    

def select_b(num, name):
    conn = getConn()
    cur = conn.cursor()
    cur.execute('select * from test where name = ?', (name,)) #매개변수에 이름 => 튜플형식이여서 (name,)이렇게 받음
    print('홍길동 데이터 가져오기')

    rs = cur.fetchmany(num) #fetchmany = 매개변수 숫자만큼 데이터 가져오기
    for i in rs:
        print(i)


if __name__ == '__main__':
    #select_a()
    select_b(1, '홍길동')