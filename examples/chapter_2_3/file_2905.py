# Цикл while
count: int = 0
name: str = "Alex"
# То что в теле может сработать только один раз
if (name == "Alice") and (count < 10):
    print("Яндекс")

count: int = 0
# То что в теле может сработать только один или более раз
while (name == "Alice") and (count < 10):
    print("Yandex")

    count += 1

# ---

# Цикл (итератор) for

# for i in range(10):
# когда переменная цикла не используется,
# то переменную называют _ (подчеркивание)
for _ in range(10):
    print("Привет, Мир!")

i: int = 0
while i < 10:
    print("Привет, Мир!")

    i += 1  # i = i + 1

if name == "Alice":
    for _ in range(10):
        print("Yandex")

# ---

sequence: str = "Hello"

for item in sequence:
    print(item.upper())

j: int = 0  # индекс первого символа
length: int = len(sequence)  # 5

while j < length:
    print(sequence[j].upper())
    j += 1

# ---

# markdown разметка
