from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def create_connection():
    conn = sqlite3.connect('ai_memory.db')
    return conn

def create_table():
    conn = create_connection()
    sql_create_experiences_table = """ CREATE TABLE IF NOT EXISTS experiences (
                                        id integer PRIMARY KEY,
                                        timestamp text NOT NULL,
                                        experience text NOT NULL
                                    ); """
    conn.execute(sql_create_experiences_table)
    conn.close()

@app.route('/add_experience', methods=['POST'])
def add_experience():
    try:
        experience = request.json['experience']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = create_connection()
        sql = ''' INSERT INTO experiences(timestamp, experience)
                  VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (timestamp, experience))
        conn.commit()
        conn.close()
        return jsonify({"message": "Experience added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_experiences', methods=['GET'])
def get_experiences():
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM experiences")
        rows = cur.fetchall()
        conn.close()
        experiences = []
        for row in rows:
            experiences.append({"id": row[0], "timestamp": row[1], "experience": row[2]})
        return jsonify(experiences), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000)