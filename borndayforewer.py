correct_year = 1799
correct_day = 6

while True:
    user_year = int(input("Введите год рождения А.С. Пушкина: "))

    if user_year == correct_year:
        while True:
            user_day = int(input("Введите день рождения А.С. Пушкина: "))

            if user_day == correct_day:
                print("Верно")
                exit()  # Выход из программы
            else:
                print("Неверный день рождения")
        break
    else:
        print("Неверный год рождения")