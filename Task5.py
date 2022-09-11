# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = int(input('Введите число: '))

def fibonacci(num):
    fibo = []
    n1, n2 = 1, 1
    for i in range(num):
        fibo.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for i in range(num+1):
        fibo.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fibo

print(fibonacci(number))