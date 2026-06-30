# Задача P


# n: int = int(input())
#
#
# if n == n[::-1]:
#     print("YES")
# else:
#     print("NO")


# s = "hello"
#
# print(s[::-1])


# ---

# n = 123
#
# last_digit = 3
# middle = 2
# first = 1
#
# reversed_num = 0
# reversed_num = reversed_num * 10 + last_digit  # 3
# reversed_num = reversed_num * 10 + middle      # 32
# reversed_num = reversed_num * 10 + first       # 321

# ---

n: int = int(input())

temp_n: int = n
reversed_num: int = 0
while temp_n > 0:
    last_digit = temp_n % 10

    # reversed_num *= 10 + last_digit
    reversed_num = reversed_num * 10 + last_digit

    temp_n //= 10

print(n)
print(reversed_num)

# TODO: Как разработать версию программы для любых целых чисел?

# -12321

number: int = int((int(input()) ** 2) ** 0.5) # сначала возводим в степень 2, чтобы избавиться от знака "минус", затем извлекаем корень.

temp_number = number
revers_number: int = 0

while number != 0:
    last_digit = number % 10
    revers_number = revers_number * 10 + last_digit
    number = number // 10

if revers_number == temp_number:
    print('YES')

else:
    print('NO')
