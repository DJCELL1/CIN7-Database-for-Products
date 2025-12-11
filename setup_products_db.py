import sqlite3

def setup_db():
    con = sqlite3.connect("products.db")
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            code TEXT UNIQUE,
            name TEXT,
            description TEXT,
            supplier TEXT,
            status TEXT,
            lastModified TEXT
        )
    """)

    con.commit()
    con.close()

if __name__ == "__main__":
    setup_db()
    print("products.db ready to roll, uso.")
