class Prystrii:
    def on(self):
        print("Пристрій увімкнено")

    def off(self):
        print("Пристрій вимкнено")


class Phone(Prystrii):
    pass


class Laptop(Prystrii):
    pass


class TV(Prystrii):
    pass


phone = Phone()
laptop = Laptop()
tv = TV()

phone.on()
laptop.on()
tv.on()

tv.off()
