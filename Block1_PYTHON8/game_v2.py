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

random_predict()
