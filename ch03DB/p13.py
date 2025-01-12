# DB다루기 최종본 !! C,R,U,D (create, read, update, delete)
import sqlite3
from libs.db.dba import getNewConn

class Db:
    #클래스변수
    conn = getNewConn('c:/test/phon.db')
    cur = conn.cursor()
    
    #테이블 생성 메소드
    def createTable(self):
        Db.cur.execute('create table tell(name text, no text)')
    
    #데이터 삽입 메소드
    def insert(self):
        #인스턴스 변수
        self.name = input('이름:')
        self.no = input('전화번호:')
        self.sql = 'insert into tell values(?,?)'
        Db.cur.execute(self.sql, (self.name, self.no))

    #데이터 출력 메소드
    def select(self):
        self.sql = 'select * from tell'
        Db.cur.execute(self.sql)
        rs = Db.cur.fetchall()

        print('*********데이터 출력*********')
        for k, v in rs:
            print(k,v)

    #데이터 삭제 메소드
    def delete(self):
        self.name = input('이름:')
        self.sql = 'delete from tell where name = ?'
        Db.cur.execute(self.sql, (self.name,))
        
    #데이터 업데이트 메소드
    def update(self):
        self.name = input('이름:')
        self.no = input('전화번호:')
        self.sql = 'update tell set no=? where name=?'
        Db.cur.execute(self.sql, (self.no, self.name))

def main():
    d = Db()
    while True:
        n = input('a.테이블 생성 1.입력 2.조회 3.삭제 4.수정  0.종료: ')
        if n == 'a':
            d.createTable()
        if n == '1':
            d.insert()
        if n == '2':
            d.select()
        if n == '3':
            d.delete()
        if n == '4':
            d.update()
        if n == '0':
            d.conn.commit()
            d.conn.close()
            print('*****프로그램을 종료합니다*****')
            break

if __name__ == '__main__':
    main()
    