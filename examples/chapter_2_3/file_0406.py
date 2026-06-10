# Перебирать символы из строки

s: str = "Welcome"

for item in s:
    print(item.lower())
# print(s)


i: int = 0
# print(len(s))
length: int = len(s)

while i < length:
    # while i < len(s):
    print(s[i].lower())

    i = i + 1  # инкрементировать

# –––

# сумма всех чисел в диапазоне
start: int = 1
end: int = 10

total_sum: int = 0
for i in range(start, end + 1):
    total_sum = total_sum + i
print(total_sum)

# произведение всех чисел в диапазоне
start: int = 1
end: int = 10

total_prod: int = 1
for i in range(start, end + 1):
    total_prod = total_prod * i
print(total_prod)

# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120

# ---

# сумма всех чисел в диапазоне
start: int = 1
end: int = 10

total_sum: int = 0
j: int = start
while j < end:
    total_sum = total_sum + j

    j = j + 1

print(total_sum)
print(f"start = {start}, end = {end}, j = {j}")

start: int = 1
end: int = 10

total_sum: int = 0
while start < end:
    total_sum = total_sum + start

    start = start + 1

print(total_sum)
print(f"start = {start}, end = {end}")

# произведение всех чисел в диапазоне
start: int = 1
end: int = 10

total_prod: int = 1
while start < end:
    total_prod = total_prod * start

    start = start + 1
    # start += 1

print(total_prod)

# найдите произведение всех цифр пятизначного числа

n: int = int(input())  # 12345, 67492, 34054

total_prod: int = 1
while n > 0:
    m = n % 10
    total_prod = total_prod * m

    n = n // 10

print(total_prod)
