import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ ایجاد اتصال به پایگاه داده SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def select_all_experiences(conn):
    """ بازیابی تمام تجربیات از جدول """
    cur = conn.cursor()
    cur.execute("SELECT * FROM experiences")
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

def main():
    database = "ai_memory.db"

    # ایجاد اتصال به پایگاه داده
    conn = create_connection(database)

    with conn:
        print("تجربیات ذخیره شده:")
        select_all_experiences(conn)

if __name__ == '__main__':
    main()