import time

sec: float = 0
while True:
    print(f"{sec} seconds")

    sec += 0.25
    time.sleep(0.25)

    if sec >= 10:
        print(f"{sec} seconds left")
        break

# ---

fruits: list[str] = ["apple", "banana", "cherry", "grape", "mango"]
target: str = "cherry"

for fruit in fruits:
    if fruit == target:
        print(f"{fruit} fruit found")
        break

# ---

fruits: list[str] = ["apple", "banana", "cherry", "grape", "mango"]

dontlike: str = "grape"
for fruit in fruits:
    if fruit == dontlike:
        continue

    print(f"I like {fruit}")

print(f"---------")

dontlike: str = "grape"
for fruit in fruits:
    if fruit != dontlike:
        print(f"I like {fruit}")

# ---

nums: list[int] = [10, 3, 5, -5, 73, 24, 675, 69]
target: int = 66
flag: bool = False
for num in nums:
    if target == num:
        flag = True
        print("found")
        break

if not flag:
    print("not found")

target: int = 3
flag: bool = False
for num in nums:
    if target == num:
        flag = True
        print("found")
        break
else:
    print("not found")

# ---

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue  # Пропустить часть кода на этой итерации
    print(number)

for number in numbers:
    if number % 2 != 0:
        print(number)
