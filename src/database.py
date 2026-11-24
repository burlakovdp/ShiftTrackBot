import sqlite3
import pendulum
import os
import dotenv

dotenv.load_dotenv()

DATABASE = os.getenv('DB_PATH')

def insert_data(user_id, shift, message_counter_1, message_counter_2):

    day = pendulum.now("UTC").format("YYYY-MM-DD HH:mm:ss")

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    cur.execute("INSERT INTO class (user_id, shift, counter_amo, counter_tg, date) VALUES (?, ?, ?, ?, ?)",
                (user_id, shift, message_counter_1, message_counter_2, day))
    conn.commit()
    conn.close()

def read_user_language(user_id):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    cur.execute("SELECT language "
                "FROM users"
                " WHERE user_id = ?", ( user_id,))
    res = cur.fetchall()
    conn.close()
    #print(res)
    return res[0][0]

def update_user_language(user_id, language):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    cur.execute("UPDATE users SET language = ? WHERE user_id = ?", (language, user_id))
    conn.commit()
    conn.close()

def read(user_id):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT date, shift, counter_amo, counter_tg "
                "FROM class"
                " WHERE user_id = ?", (user_id,))
    res = cur.fetchall()
    conn.close()
    return res


