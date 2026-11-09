import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo


def insert(data):

    nice_tz = ZoneInfo("Europe/Paris")

    day = datetime.now(nice_tz).date().isoformat()

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (data['user_id'],))
    cur.execute("INSERT INTO class (user_id, class_type, counter_messages, date) VALUES (?, ?, ?, ?)",
                (data['user_id'], data['source'], data['message_counter'], day))
    conn.commit()
    conn.close()

def read(user_id):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT class_type,counter_messages, date "
                "FROM class"
                " WHERE user_id = ?", (user_id,))
    res = cur.fetchall()
    conn.close()
    return res


