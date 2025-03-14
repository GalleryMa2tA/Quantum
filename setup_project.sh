#!/bin/bash

# ایجاد پوشه پروژه
mkdir -p ~/ai_project
cd ~/ai_project

# ایجاد فایل database_setup.py
cat <<EOT >> database_setup.py
import sqlite3

def create_connection(db_file):
    """ ایجاد اتصال به پایگاه داده SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ ایجاد جدول در پایگاه داده """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database = "ai_memory.db"

    sql_create_experiences_table = """ CREATE TABLE IF NOT EXISTS experiences (
                                        id integer PRIMARY KEY,
                                        timestamp text NOT NULL,
                                        experience text NOT NULL
                                    ); """

    # ایجاد اتصال به پایگاه داده
    conn = create_connection(database)

    # ایجاد جدول‌ها
    if conn is not None:
        create_table(conn, sql_create_experiences_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
EOT

# ایجاد فایل save_experience.py
cat <<EOT >> save_experience.py
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
EOT

# ایجاد فایل retrieve_experience.py
cat <<EOT >> retrieve_experience.py
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
EOT

echo "تمام فایل‌ها و پوشه‌ها ایجاد شدند."