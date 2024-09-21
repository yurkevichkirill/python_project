print("hello world")
a = [1, 'Kirill', 2.4, True]
print(a)
info = {"name": "Kirill", "height": 185, "weight": 85, "love": "Veronika"}
print(info["love"])
print(2**3)
print(f"{35/6:.2f}")
print(36//6)
print(35%6)

# num1 = int(input("Введите первое число "))
# num2 = int(input("Введите второе число "))
# if num1 > num2:
#     print("Число", num1, "больше числа", num2)
# elif num1 < num2:
#     print("Число", num2, "больше числа", num1)
# else:
#     print("Числа равны")

# i = 6
# while i <= 10:
#     print(i)
#     if(i == 5):
#         break
#     i += 1
# else:
#     print('Цикл окончен, i =', i)
# print("Конец")

print("%7s %-10s %-10s" %('param1', 'param2', 'param3'))

print('{}'.format(['el_1', 'el_2', 'el_3', 'el_4']))
print("{:>30} {:>20} {:>20}".format('my_param_1', 'my_param_2',
'my_param_3'))

string = "abrakadbra"
str_reverse = string[::-1]
print(str_reverse)







