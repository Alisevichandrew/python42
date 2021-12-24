# def print_name(name='world'):
#     print(f'Hello, {name}')


# Создать собственный модуль, который будет содержать несколько функций:
# Проверка числа на четность

# Вывод делителей числа

# Является ли число простым

# (предусмотреть ввод отрицательного числа)



def is_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 10 -> [1,2,5,10]
# 7 -> [1, 7]
# 1 -> [1]
def delimeters(n): #функция делителей числа
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result 

def is_prime(n): 
   count_of_delimetrs = len(delimeters(n))
   if count_of_delimetrs == 2:
       return True
    else:
        return False 
