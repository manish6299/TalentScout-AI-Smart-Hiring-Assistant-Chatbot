import sqlite3

DB_NAME = "candidates.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            experience TEXT,
            position TEXT,
            location TEXT,
            tech_stack TEXT,
            sentiment TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_candidate_to_db(data: dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO candidates 
        (name, email, phone, experience, position, location, tech_stack, sentiment)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("name"),
        data.get("email"),
        data.get("phone"),
        data.get("experience"),
        data.get("position"),
        data.get("location"),
        data.get("tech_stack"),
        data.get("sentiment", "neutral")
    ))

    conn.commit()
    conn.close()
