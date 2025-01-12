# db에서 delete하기

import sqlite3
from libs.db.dba import getConn

def del_a(num):
    conn = getConn()
    cur = conn.cursor()
    cur.execute('delete from test where eng <= ?', (num,))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    del_a(85)