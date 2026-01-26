import sqlite3

DB_NAME = "AnimalKingdom.db"

def main():
    # 1) Підключення/створення БД
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # 2) Створення таблиці
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            animal_type TEXT NOT NULL
        )
    """)

    # Щоб при повторному запуску не дублювати записи (для зручності навчання)
    cur.execute("DELETE FROM Animals")

    # 3) Вставка 5 звірів
    animals = [
        ("Лев", "Ссавець"),
        ("Крокодил", "Плазун"),
        ("Орел", "Птах"),
        ("Морська черепаха", "Плазун"),
        ("Мавпа", "Ссавець"),
    ]
    cur.executemany("INSERT INTO Animals (name, animal_type) VALUES (?, ?)", animals)

    # 4) Зміна "Орел" -> "Сокіл"
    cur.execute("UPDATE Animals SET name = ? WHERE name = ?", ("Сокіл", "Орел"))

    conn.commit()

    # 5) Вибір всіх звірів типу "Ссавець"
    print('Звірі типу "Ссавець":')
    cur.execute('SELECT id, name, animal_type FROM Animals WHERE animal_type = ?', ("Ссавець",))
    for row in cur.fetchall():
        print(row)

    # 6) Вивід всіх записів
    print("\nУсі записи про звірів:")
    cur.execute("SELECT id, name, animal_type FROM Animals ORDER BY id")
    for row in cur.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    main()
