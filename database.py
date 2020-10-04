import sqlite3

def init():
    import sqlite3
    conn = sqlite3.connect('vokabeln.db')
    conn.execute('CREATE TABLE vokabeln (id INTEGER, vokabel TEXT, solution TEXT)')
    conn.close()