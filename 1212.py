import colorama
import inspect
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print("Модуль COLORAMA\n")

print("Тип модуля colorama:")
print(type(colorama))
print()

print("Атрибути та методи модуля colorama:")
print(dir(colorama))
print()

print("Коротка довідка про модуль colorama:")
help(colorama)

print("\nІНТРОСПЕКЦІЯ КЛАСІВ:\n")

print("Атрибути класу Fore:")
print(dir(Fore))
print()

print("Атрибути класу Back:")
print(dir(Back))
print()

print("Атрибути класу Style:")
print(dir(Style))
print()

print("\nПриклад:\n")

print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Back.BLUE + "Текст з синім фоном")
print(Style.BRIGHT + "Кастом текст")
print(Style.RESET_ALL + "Звичайний текст")

print("\nВИСНОВОК      ")
print("Colorama дозволяє працювати з шрифтом у консолі.")
print("За допомогою інтроспекції були досліджені модуль та основні класи:")
print("Fore–колір тексту, Back–колір фону, Style–стиль тексту.")
