import json
import sqlite3
from textblob import TextBlob
import os

# Emotion Detection
def get_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity < -0.3:
        return "sad"
    elif polarity > 0.4:
        return "happy"
    else:
        return "normal"

# Short-term memory
def load_memory():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as f:
            return json.load(f)
    else:
        return {"short_term": []}

def save_memory(memory):
    with open("memory.json", "w") as f:
        json.dump(memory, f)

# SQLite Long-term memory
def init_db():
    conn = sqlite3.connect("priyanka.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT,
            reply_text TEXT,
            emotion TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn, cursor

def save_long_term(user_text, reply_text, emotion):
    conn, cursor = init_db()
    cursor.execute("INSERT INTO memory (user_text, reply_text, emotion) VALUES (?, ?, ?)",
                   (user_text, reply_text, emotion))
    conn.commit()
    conn.close()
