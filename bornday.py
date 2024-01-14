correct_year = 1799

user_year = int(input("Введите год рождения А.С. Пушкина: "))

if user_year != correct_year:
    print("Неверный год рождения")
else:
    user_day = int(input("Введите день рождения А.С. Пушкина: "))
    correct_day = 6 # Предполагаемый день рождения А.С. Пушкина

    if user_day == correct_day:
        print("Верно")
    else:
        print("Неверный день рождения")