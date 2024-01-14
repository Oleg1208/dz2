correct_year = 1799

while True:
    user_year = int(input("Введите год рождения А.С. Пушкина: "))

    if user_year == correct_year:
        print("Верно")
        break
    else:
        print("Неверный год рождения")