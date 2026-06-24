# Loops - Циклы

## Традиционные циклы в программирование

- `while` - пока, до тех пор
- `for` (условие) (нет в Python)
- Java, JS

```java
for (int i = 0; i < 10; i++) {

 }
```

- `do while` (нет в Python)

## Итератор

```
# for элемент из последовательности:
```

```python
sequence: str = "Hello"
for item in sequence:
    print(item.upper())
```

## Клюевые слова, которые часто используются в циклах:

- `break` - бросать, прервать
- `continue` - продолжить
- `pass` (только в Python) - синтаксическое дополнение кода, чтобы не было ошибок
- `else` (только в Python) - иначе, тогда

```python
name = "Alice"

if name.lower() == "alex":
    pass
else:
    print("Это не Алекс")


def main():
    ...
```

## Оператор присваивание

```python
name = "Alice"
print(name)
```

с этим опетаором не получится присовить и вывести результат.

```python
# print(name="Alice")
```

## Моржовый оператор

```python
# name := "Alice"
```

```python
print(name := "Alice")
```

```python
name = input()
while name != "alex":
    print("Укажите корректное имя")
    name = input()
```

```python
while (name := input()) != "alex":
    print("Укажите корректное имя")
```

---

# 04.06.2026

- инкрементировать - увеличить
- декрементировать - уменшить

```python
n: int = 789

# шаг 1
last_digit: int = n % 10  # 9
n = n // 10  # 78

# шаг 2
last_digit: int = n % 10  # 8
n = n // 10  # 7

# шаг 3
last_digit: int = n % 10  # 7
n = n // 10  # 0

print(n)
```

Условие для `while`: Когда `n` будет равна нулю.

```python
n: int = 789

while n != 0:
    last_digit: int = n % 10
    n = n // 10
```

---

## Операторы циклов

[Исходный код](file_1106.py)

---

## Какие алгоритмы мы уже знаем

- Линеный поиск

```python
fruits: list[str] = ["apple", "banana", "cherry", "grape", "mango"]
target: str = "cherry"

for fruit in fruits:
    if fruit == target:
        print(f"{fruit} fruit found")
        break
```

- Бинарный поиск

```python
# например уже реализованная программа "Угадай число"
low: int = 1
high: int = 1000
more: str = 'Больше'
fewer: str = 'Меньше'
target: str = 'Угадал!'

while True:
    guess = (low + high) // 2
    print(guess)
    reply: str = input()

    if reply == target:
        break

    if reply == fewer:
        high = guess - 1
    elif reply == more:
        low = guess + 1     
```
