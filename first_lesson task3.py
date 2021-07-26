#s = 'abcd' + 'efgh'
#print(s)
# сложение строк

#или 
 
#s1 = 'abcd'
#s2 = 'efgh'
#s = s1 + s2
#print(s) 

#или

#чтобы посчитать длину строки, нужно

#s1 = 'abcd'
#s2 = 'efgh'
#s = s1 * 5 + s2
#print(len(s)) 
#len count only from variable, for example - 'S'

# or

#s1 = str(1234) 
#1234 this is the string value
#s2 = 'efgh'
#s = s1 * 5 + s2
#print(s) 

# or 

#s1 = str(1234) 
#1234 this is the string value
#s2 = 'efgh'
#s = s1 * 5 + s2
#print(s)
#print(s[10]) #we take 10-s value. 
#In resault, we've got value '3' couse count
#begin from '0' and then '1234 e.t.c.

#value from '10' till '15'
#s1 = str(1234) 
#1234 this is the string value
#s2 = 'efgh'
#s = s1 * 5 + s2
#print(s)
#print(s[10:15]) #resault from '10' till '15' 
#10-s value include, 15-s value does not include 

#overturn string
#s1 = str(1234) 
#1234 this is the string value
#s2 = 'efgh'
#s = s1 * 5 + s2
#print(s)
#print(s[::-1]) #from ':' - start, to ":" - finish 
#with step '-1'
#10-s value include, 15-s value does not include 


#we take every 3-d element
#s1 = str(1234) 
#1234 this is the string value
#s2 = 'efgh'
#s = s1 * 5 + s2
#print(s)
#print(s[1:10:3]) #from '1' - start, to "10" - finish 
#every 3-d element '3'
#1-st value include, 10-s value does not include 


#we input string
#s = input() 
#print(len(s))
#we take string overturn and print '3' time (раза)
#print(s[::-1] * 3)
#we print value from 1-st and last sumbols
#print(s[1:-1])

#у нас есть строка
#и мы хотим, чтобы каждый раз выводилось новое имя
#name = 'World'
#temp = f'Hello, {name}'
#вверху указана так называемая 'f' строка
#в нее можно вводить переменные, которые объявили раньше
#эти переменные могут быть преобразованы в 'str'
#print(temp)

#а можно и вводить слова
#name = input()
#temp = f'Hello, {name}'
#вверху указана так называемая 'f' строка
#в нее можно вводить переменные, которые объявили раньше
#эти переменные могут быть преобразованы в 'str'
#print(temp)

#также можно подставить другой тип данных
#name = 12345
#temp = f'Hello, {name}'
#вверху указана так называемая 'f' строка
#'f' строка может использоваться в программе 
#только один раз, а потом "умирает"
#в нее можно вводить переменные, которые объявили раньше
#эти переменные могут быть преобразованы в 'str'
#print(temp)

#или у нас есть шаблон, и мы в этот шаблон 
#подставляем 'name', который вводим
name = 12345
temp = 'Hello, {name}' #это шаблон
#где вместо {name} подставляется '12345'

print(temp.format(name=name))


