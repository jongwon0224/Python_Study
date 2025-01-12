import sqlite3

def getConn():
    conn = sqlite3.connect('c:/test/abc.db') #db접속
    return conn

def getNewConn(dbpath):
    conn = sqlite3.connect(dbpath)
    return conn