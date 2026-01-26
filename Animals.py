import sqlite3

DB_NAME = "AnimalKingdom.db"

def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            animal_type TEXT NOT NULL
        )
    """)
    cur.execute("DELETE FROM Animals")
    animals = [
        ("Лев", "Ссавець"),
        ("Крокодил", "Плазун"),
        ("Орел", "Птах"),
        ("Морська черепаха", "Плазун"),
        ("Мавпа", "Ссавець"),
    ]
    cur.executemany("INSERT INTO Animals (name, animal_type) VALUES (?, ?)", animals)

    cur.execute("UPDATE Animals SET name = ? WHERE name = ?", ("Сокіл", "Орел"))
    conn.commit()

    print('Звірі типу "Ссавець":')
    cur.execute("SELECT id, name, animal_type FROM Animals WHERE animal_type = ?", ("Ссавець",))
    for row in cur.fetchall():
        print(row)

    print("\nУсі записи про звірів:")
    cur.execute("SELECT id, name, animal_type FROM Animals ORDER BY id")
    for row in cur.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    main()

