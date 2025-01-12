# db update하기 !

import sqlite3
from libs.db.dba import getConn

def update_a():
    conn = getConn() #커넥션가져오기
    cur = conn.cursor() #쿼리문 실행위해 커서가져오기
    up_sql = 'update test set name=? where name = ?'
    cur.execute(up_sql,('홍일점', '홍길동'))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    update_a()