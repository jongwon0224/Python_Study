# SQLite
# sqlite3 모듈 임포트

# 1. table 만들기
# 커넥션 만들기
# 커넥션 함수 가져오기

from libs.db.dba import getConn
#테이블 생성하기
def create_table():
    conn = getConn() #커넥션 가져오기
    cur = conn.cursor() #커서 생성
    cur.execute(''' 
    create table test(
                name text,
                kor int,
                eng int,
                mat int)

''')
    conn.commit() # db 커밋하기
    conn.close()

#이 파일이 메인일 경우에만 true값 나옴
if __name__ == '__main__':
    create_table()

