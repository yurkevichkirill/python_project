import math

start = int(input("Введите начало диапазона "))
end = int(input("Введите конец диапазона "))

print("Начало:", start)
print("Конец:", end)

for el in range(start, end):
    isRight = True

    if(el < 2):
        continue

    for i in range(2, int(math.sqrt(el)) + 1):
        if el % i == 0:
            isRight = False
            break
    if isRight:
        print(el)