import sqlite3

def create_database():

    conn = sqlite3.connect("database/visitors.db")

    cursor = conn.cursor()

    cursor.execute('''

    CREATE TABLE IF NOT EXISTS visitors(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    phone TEXT,

    purpose TEXT,

    photo TEXT,

    checkin_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    ''')

    conn.commit()

    conn.close()


def add_visitor(name, phone, purpose, photo):

    conn = sqlite3.connect("database/visitors.db")

    cursor = conn.cursor()

    cursor.execute(

        "INSERT INTO visitors(name,phone,purpose,photo) VALUES(?,?,?,?)",

        (name, phone, purpose, photo)

    )

    conn.commit()

    conn.close()
