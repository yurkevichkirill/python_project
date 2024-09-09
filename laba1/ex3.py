import sys

n = int(input("Введите натуральное число n "))
print(n)

if(n<1):
    print("Данное число не является натуральным")
    sys.exit()
cube_list = []
print("Введите n целых чисел")
for i in range(n):
    num = int(input())
    cube_list.append(num ** 3)
sum = 0
product = 1
for el in cube_list:
    sum += el
    product *= el
print("Сумма элементов списка:", sum)
print("Произведение элементов списка:", product)

for el in reversed(cube_list):
    print(el)
