"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict():
    """Рандомно угадываем число
    Returns:
        int: Число попыток и само число
    """

    count = 0
    mn, mx = 1, 100
    number = np.random.randint(mn, mx+1)  # Загаданное число.\
    # По умолчанию рандомно загадывается компьютером в диапазоне mn-mx.
    if number == mn:
        print(f"Компьютер угадал число за {1} попытку. \
        Это число {number}")
        return 1

    if number == mx:
        print(f"Компьютер угадал число за {1} попытку. \
        Это число {number}")
        return 1

    while True:
        count += 1
        md = int((mn+mx)/2)

        if md > number:
            mx = md
        elif md < number:
            mn = md

        else:
            print(f"Компьютер угадал число за {count} попыток. \
                Это число {number}")
            break  # End of game. Exit from while

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов \
    угадывает наш алгоритм

    Args:
        random_predict (): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    for i in range(1, 101):
        count_ls.append(random_predict())

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
score_game(random_predict)
