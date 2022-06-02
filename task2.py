#Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

#Пример:

#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

N = int(input("Ввведите число: "))

def factorial(n):
    num = 1
    numbers = []
    for i in range (1, n+1):
        num = num * i
        numbers.append(num)
    return numbers

print(f'набор произведений чисел от 1 до N {factorial(N)}')
