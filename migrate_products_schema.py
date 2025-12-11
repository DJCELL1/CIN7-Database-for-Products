import sqlite3

con = sqlite3.connect("products.db")
cur = con.cursor()

# Add new columns if they don't exist
columns_to_add = [
    ("styleCode", "TEXT"),
    ("stockControl", "TEXT"),
    ("supplierCode", "TEXT"),
    ("supplierName", "TEXT"),
    ("supplierId", "INTEGER")
]

for col, typ in columns_to_add:
    try:
        cur.execute(f"ALTER TABLE products ADD COLUMN {col} {typ};")
        print(f"Added column {col}")
    except:
        print(f"Column {col} already exists, uso.")

con.commit()
con.close()

print("Schema upgrade complete, sole!")
