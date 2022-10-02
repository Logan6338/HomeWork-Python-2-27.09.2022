# 3) Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55


start = False
while start == False:
    n = int(input('Введите положительное число '))
    if n >= 1:
        start = True
    else:
        print('Неправильное число!! ')
result = 0
for i in range (1, n+1):
    result += (1+1/i)**i
print(result)