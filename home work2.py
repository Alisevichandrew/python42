# Определяем переменную str
str = "Uncle Styopa helped the girl cross the road"

# Выполняем операцию с переменной str
result = str.replace("Uncle Styopa", "Andrew")
 
# Выводим результат на экран
print(result)

#далее, выполняем аналогичные операции по замене
str1 = "Styopa took the cat from the tree"
result = str1.replace("Styopa",  "Andrew")
print(result)

str2 = "Uncle took Tanya's ball out of the river"
result = str2.replace("Uncle",  "Andrew")
print(result)

s = "It will rain for a week"
print(s.replace("It will rain for a week", "the next string withoun changes:"))
print(s)

str3 = "Uncle Styopa is now the official person of KOKO pizza. With the promo code 'Styopa' you can get a discount on training"
result = str3.replace('Uncle', 'Andrew') 
result = str3.replace("Styopa",  "Andrew", 2)
print(result)

#enter finish result
#end of program

