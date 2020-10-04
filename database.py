import sqlite3 as sql

def init():
    conn = sql.connect('vokabeln.db')
    conn.execute('CREATE TABLE vokabeln (id INTEGER, vokabel TEXT, solution TEXT)')
    conn.close()

def getAllVocabs():
    con = sql.connect("vokabeln.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from vokabeln")
    vocabs = cur.fetchall()
    con.close()
    return(vocabs) 