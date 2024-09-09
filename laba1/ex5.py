jewelry_dict = {
    "necklace": ["silver", "$30", 60],
   "earrings": ["gold", "$115", 18],
   "ring": ["gold", "$230", 77],
   "brooch": ["zircon", "$16", 200],
   "chain": ["silver", "$45", 55]
}

while True:
    print("Выберите опцию меню")
    print("1 Просмотр описания")
    print("2 Просмотр цены")
    print("3 Просмотр количества")
    print("4 Всю информацию")
    print("5 Покупка")
    print("6 До свидания")

    choise = int(input())
    if choise == 1:
        for el in jewelry_dict:
            print(el, '-', jewelry_dict[el][0])
    elif choise == 2:
        for el in jewelry_dict:
            print(el, '-', jewelry_dict[el][1])
    elif choise == 3:
        for el in jewelry_dict:
            print(el, '-', jewelry_dict[el][2])
    elif choise == 4:
        for el in jewelry_dict:
            print(el, '-', jewelry_dict[el])
    elif choise == 5:
        print("Введите название изделия")
        name = input()
        count = 0
        if name in jewelry_dict:
            print("Введите количество")
            quantity = int(input())
            if quantity > jewelry_dict[name][2]:
                print(f"Такого количества нет в наличии ({jewelry_dict[name][2]})")
            else:
                print("Изделие", name, "в количестве", quantity, "штук было успешно куплено!")
        else:
                print("Изделие не найдено")
    elif choise == 6:
        break
