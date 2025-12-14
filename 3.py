class Task:
    def __init__(self, title, desc, deadline):
        self.title, self.desc, self.deadline = title, desc, deadline
        self.done = False

    def __str__(self):
        s = "✅" if self.done else "❌"
        return f"{s} {self.title} (до {self.deadline}) — {self.desc}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, desc, deadline):
        self.tasks.append(Task(title, desc, deadline))

    def delete(self, n):
        if 1 <= n <= len(self.tasks):
            self.tasks.pop(n - 1); return True
        return False

    def done(self, n):
        if 1 <= n <= len(self.tasks):
            self.tasks[n - 1].done = True; return True
        return False

    def show(self, only_not_done=False):
        if not self.tasks:
            print("Список порожній."); return
        for i, t in enumerate(self.tasks, 1):
            if not (only_not_done and t.done):
                print(f"{i}. {t}")


m = TaskManager()
while True:
    print("\n1 Додати  2 Видалити  3 Виконано  4 Всі  5 Невиконані  0 Вихід")
    c = input(">").strip()

    if c == "1":
        m.add(input("Назва: "), input("Опис: "), input("Дедлайн: "))
    elif c == "2":
        print("OK" if m.delete(int(input("Номер: "))) else "Немає такого")
    elif c == "3":
        print("OK" if m.done(int(input("Номер: "))) else "Немає такого")
    elif c == "4":
        m.show()
    elif c == "5":
        m.show(True)
    elif c == "0":
        break
    else:
        print("Невірна команда")
