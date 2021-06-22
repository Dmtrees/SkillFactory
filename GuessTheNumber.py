from typing import Any, Union
import numpy as np   # Импорт библиотеки numpy


def game_core(number):    # Функция, которая возвращает кол-во попыток, в зависимости от загадонного числа
    low_number = 1    # Первое значение интервала, в котором угадывается число
    high_number = 101    # Последнее значение интервала, в котором угадывается число
    count = 0    # Счетчик попыток
    while True:
        predict = (low_number + high_number) // 2
        count += 1
        if number > predict:
            low_number = predict + 1
        elif number < predict:
            high_number = predict - 1
        elif number == predict:
            break
    return count


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score: Union[int, Any] = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


number = np.random.randint(1, 101)
print(score_game(game_core))
