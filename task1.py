#Напишите программу, которая принимает на вход вещественное число и показывает сумму 
#его цифр(отсекаем минус, считаем все в плюс).

#Пример:

#67,82 -> 23
#0,56 -> 11

n = float(input('Введите число '))


a = n/10 
b = n%10
c = n*10%10
d = n*100%10
print(a+b+c+d)
#что-то я запуталась.. округлить не получилось