#Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

#Пример:

#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

n = int(input("Ввведите число: "))

first_num = 1 
counter = 0
while counter < n:
    counter = counter + 1
step = counter
for i in range(n-1):
    print (first_num, end=", ")
    first_num = first_num*step
print(first_num)