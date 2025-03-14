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