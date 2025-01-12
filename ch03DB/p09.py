import sqlite3
from libs.db.dba import getConn

#1번 방법 : 테이블에 데이터 삽입
#정적 쿼리 => 데이터 값이 정해져있음
def insert_b():
    conn = getConn() # dba모듈에서 getConn가져오기기
    cur = conn.cursor() #커서 가져오기
    cur.execute('''
                insert into test values('홍길동', 80, 90, 100)
                ''')
    conn.commit() #커밋해서 저장
    conn.close() # 커넥션 종료

#2번 방법 : 테이블에 데이터 삽입
#동적쿼리 => 데이터가 동적임
# cur.execute(변수명,(튜플형식 데이터))
def insert_c():
    conn = getConn()
    cur = conn.cursor()
    ins_sql = 'insert into test values(?,?,?,?)'
    cur.execute(ins_sql,('황종원', 77, 80, 99)) #튜플 형식으로 매개변수 넣어야됨
    conn.commit()
    conn.close()

#3번 방법 : 다수 데이터 한번에 넣기
#동적 쿼리 => cur.executemany(변수명, 리스트명)
def insert_d():
    conn = getConn()
    cur = conn.cursor()
    ins_sql = 'insert into test values(?,?,?,?)'

    li = [('황철수', 70, 50, 30),('이홍기', 30, 80, 60),('김기원', 60, 70, 60)]
    cur.executemany(ins_sql, li)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    #insert_b()
    #insert_c()
    insert_d()