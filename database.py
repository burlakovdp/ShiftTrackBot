import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo


def insert(data):

    NICE_TZ = ZoneInfo("Europe/Paris")
    
    day = datetime.now(NICE_TZ).date().isoformat()
    
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    print(data['user_id'])
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (data['user_id'],))
    cur.execute("INSERT INTO class (user_id, class_type, counter_messages, date) VALUES (?, ?, ?, ?)", (data['user_id'], data['source'], data['message_counter'], day))
    conn.commit()
    conn.close()