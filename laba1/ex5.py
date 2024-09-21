jewelry_dict = {
    "necklace": ["silver", 30, 60],
    "earrings": ["gold", 115, 18],
    "ring": ["gold", 230, 77],
    "brooch": ["zircon", 16, 200],
    "chain": ["silver", 45, 55]
}
cart = []

while True:
    print("1 Просмотр описания")
    print("2 Просмотр цены")
    print("3 Просмотр количества")
    print("4 Всю информацию")
    print("5 Покупка")
    print("6 До свидания")

    try:
        choice = int(input("Введите номер опции: "))
    except ValueError:
        print("Ошибка: введите целое число.")
        continue

    if choice == 1:
        for el in jewelry_dict:
            print(el, '-', jewelry_dict[el][0])
    elif choice == 2:
        for el in jewelry_dict:
            print(el, ' - $', jewelry_dict[el][1], sep='')
    elif choice == 3:
        for el in jewelry_dict:
            print(el, '-', jewelry_dict[el][2])
    elif choice == 4:
        for el in jewelry_dict:
            print(el, '-', jewelry_dict[el])
    elif choice == 5:
        while True:
            print("Введите название изделия")
            name = input()
            if name in jewelry_dict:
                try:
                    print("Введите количество")
                    quantity = int(input())
                    if quantity <= 0:
                        print("Ошибка: количество должно быть положительным числом.")
                        continue
                except ValueError:
                    print("Ошибка: введите целое число.")
                    continue

                if quantity > jewelry_dict[name][2]:
                    print(f"Такого количества нет в наличии ({jewelry_dict[name][2]})")
                else:
                    jewelry_dict[name][2] -= quantity
                    cart.append((name, quantity))
                    print("Изделие", name, "в количестве", quantity, "штук было успешно куплено!")

                    while(True):
                        print("Желаете вернуться в меню (0) или совершить еще покупку (1)?")
                        try: buy_more = int(input())
                        except:
                            print("Ошибка: введите 0 или 1.")
                            continue
                        if buy_more == 1 or buy_more == 0:
                            break
                        else: print("Ошибка: введите 0 или 1.")

                    if buy_more == 0:
                        break
            else:
                print("Изделие не найдено")
    elif choice == 6:
        print("Ваш чек:")
        fullPrice = 0;
        for item, qty in cart:
            print(f"{item} - {qty} шт. - ${qty * jewelry_dict[item][1]}")
            fullPrice += (jewelry_dict[item][1] * qty)
        print(f"Итого: ${fullPrice}")
        break
    else:
        print("Ошибка: выбрана неверная опция.")
