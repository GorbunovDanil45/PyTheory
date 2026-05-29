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
