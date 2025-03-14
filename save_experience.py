import sqlite3
from sqlite3 import Error
from datetime import datetime

def create_connection(db_file):
    """ ایجاد اتصال به پایگاه داده SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def save_experience(conn, experience):
    """ ذخیره تجربه در جدول """
    sql = ''' INSERT INTO experiences(timestamp, experience)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, experience)
    conn.commit()
    return cur.lastrowid

def main():
    database = "ai_memory.db"

    # ایجاد اتصال به پایگاه داده
    conn = create_connection(database)

    with conn:
        # ذخیره تجربه
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        experience = "این یک تجربه نمونه است."
        experience_data = (timestamp, experience)
        experience_id = save_experience(conn, experience_data)

if __name__ == '__main__':
    main()