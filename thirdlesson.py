#shop = {
#    'mmilk' : 2,
#    'butter' : 5,
#    'muka' : 7,
#    'apple' : 10,
#}

#a = input()

#print(shop.get(a, -1))
# completed 

#print('abcd')
#print('string')

# n = 0

# def get_determinant(a, b, c):
#    d = a**2 - 4 * b *c
#    return d **0.5
# def my_new_func(name='world'):
#     n
#     return f'Hello {name}'    

# result = my_new_func('Yan')
# print(result)

# def fibonaschi_function(a):
#     a = [(i-1) + (i-2)]
#     for i in range(a):
#         return
#         print(a)

#вывести все фрукты, которые начинаются с 'a'
# fruits = ['apple','banana', 'mango']

# new_list = [x for x in fruits if 'a' == x[0]]  

# print(new_list)

#or another version

#вывести все фрукты, которые начинаются с 'a'
# fruits = ['apple','banana', 'mango']
# new_list = []
# for x in fruits:
#     if x[0] == 'a':
#         new_list.append(x)
# print(new_list)
# new_list = [x for x in fruits if 'a' == x[0]]
# print(new_list)

#мы также можем сделать

# fruits = ['apple','banana', 'mango']
# new_list = []
# for x in fruits:
#     if x[0] == 'a':
#         new_list.append(x)
# print(new_list)
# new_list = [x[1:-1] for x in fruits if 'a' == x[0]]
# print(new_list)

#есть числа от 1 до 10. Нам нужно сгенерировать квадраты этих чисел

# n = 12
# d = {}
# for x in range(1, n+1):
#     d.update({x: x**2})

# print(d)

#Это можно сократить
# n = 12
# d = {}
# for x in range(1, n+1):
#     d.update({x: x**2})

# d = {x: x**2 for x in range(1, n+1)}

# print(d)


#можно добавить условие if, где нет квадратов чисел 3, 7, 5
# n = 12
# d = {}
# for x in range(1, n+1):
#     d.update({x: x**2})

# d = {x: x**2 for x in range(1, n+1) if x not in (3, 7, 5)}

# print(d)

# #реализация функции

# def my_new_func():
#     print('Hello world') 
# my_new_func() #это вызывает функцию

#теперь в функцию передадим имя

def my_new_func(name):
    print(f'Hello {name}') #делаем принт при помощи f строки
my_new_func(name='Yan') #это вызывает функцию




