import sqlite3

def create_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS codes (
            hashcode TEXT,
            name TEXT PRIMARY KEY,
            code TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_code(db_file, snippet_id, name, code):
    create_database(db_file)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO codes (hashcode, name, code)
        VALUES (?, ?, ?)
    """, (snippet_id, name, code))
    conn.commit()
    conn.close()

def get_code(db_file, snippet_id):
    create_database(db_file)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT code FROM codes WHERE hashcode = ?", (snippet_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return None

def get_all_data_as_dataframe(db_file):
    import pandas as pd
    create_database(db_file)
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("SELECT * FROM codes", conn)
    conn.close()
    return df if not df.empty else None
