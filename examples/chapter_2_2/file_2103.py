# if
# elif - N
# else

# ---

# if
# else

# ---

# if
# elif - N

# ---

# if

# ---

# if
# if
# if
# if

a: int = 5
b: int = 10

if a > b:
    print("Первое")
elif b > a:
    print("Второе")
else:
    print("Числа равны")

if a > b:
    print("Первое")
else:
    print("Второе")

# ---

x: int = 10

if x > 2:
    print("Число больше 2")
if x % 2 != 0:
    print("Число нечетное")
if x % 5 == 0:
    print("Число кратно 5")

# ---

day: str = "вторник"

if (day == "понедельник") or (day == "вторник"):
    print("Рабочий день")
elif day == "вторник":
    print("Рабочий день")
# ...
elif day == "пятница":
    print("Рабочий день")
elif day == "суббота":
    print("Выходной день")
elif day == "воскресенье":
    print("Выходной день")
else:
    print("Неизвестный день")

# ---

match day:
    case "понедельник" | "вторник" | "среда":
        print("Рабочий день")
    case "пятница":
        print("Рабочий день")
    case "воскресенье":
        print("Выходной день")
    case _:
        print("Неизвестный день")
