path = input("Введіть шлях до файлу: ")

try:
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не знайдено.")
