import random

# Создаем словарь с знаменитостями и их годами рождения
celebrities = {
    "Альберт Эйнштейн": 1879,
    "Исаак Ньютон": 1643,
    "Мария Кюри": 1867,
    "Уильям Шекспир": 1564,
    "Леонардо да Винчи": 1452
}

# Перемешиваем список знаменитостей
celebrity_names = list(celebrities.keys())
random.shuffle(celebrity_names)

# Инициализируем переменные для подсчета результатов
correct_answers = 0
wrong_answers = 0

# Начинаем игру
play_again = "да"
while play_again.lower() == "да":
    for celebrity in celebrity_names:
        # Задаем вопрос
        user_input = input(f"Когда родился {celebrity}? ")

        # Проверяем ответ и увеличиваем счетчики
        if int(user_input) == celebrities[celebrity]:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Неправильно!")
            wrong_answers += 1

    # Выводим результаты
    total_questions = correct_answers + wrong_answers
    percent_correct = (correct_answers / total_questions) * 100
    percent_wrong = (wrong_answers / total_questions) * 100

    print(f"\nКоличество правильных ответов: {correct_answers}")
    print(f"Количество неправильных ответов: {wrong_answers}")
    print(f"Процент правильных ответов: {percent_correct}%")
    print(f"Процент неправильных ответов: {percent_wrong}%")

    # Спрашиваем пользователя, хочет ли он начать игру заново
    play_again = input("\nХотите начать игру заново? (да/нет) ")

print("Спасибо за игру! До свидания!")
