"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток
    """

    count = 0
    mn,mx = 1,100

    while True:
        count += 1
        md = int((mn+mx)/2)
        
        if md > number:
            mx = md        
        elif md < number:
            mn = md

        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
                   
    return count

random_predict()