# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

s = ""
n = int(input("Введите число в десятичной системе счисления: "))
while n != 0:
   s = str(n%2) + s
   n //=2
print(f'Число в двоичной системе после преобразования: {s}')