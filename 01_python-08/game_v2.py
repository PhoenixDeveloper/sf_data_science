"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(min_number: int, max_number: int, number: int = 1) -> int:
    """Guessing function

    Args:
        min_number (int): Beginning of the list of generated numbers
        max_number (int): Ending of the list of generated numbers
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: predict number
    """
    
    if min_number > max_number:
        raise ValueError("min_number must be less max_number")
    
    if min_number == max_number:
        return min_number
    
    count = 0
    seek_range = range(min_number, max_number)

    while True:
        count += 1
        predict_number = seek_range[0]
        
        if number in range(seek_range[0], seek_range[int(len(seek_range) / 2)]):
            seek_range = range(seek_range[0], seek_range[int(len(seek_range) / 2)])
        else:
            predict_number = seek_range[-1]
            seek_range = range(seek_range[int(len(seek_range) / 2)], seek_range[-1] + 1)
            
        if number == predict_number:
            break  # выход из цикла если угадали

    return count


def score_game(random_predict, count_iteration: int = 1000) -> int:
    """Analysis function

    Args:
        random_predict (_type_): Guessing function
        count_iteration (int, optional): Number of iterations of the guess function. Defaults to 1000.

    Returns:
        int: Average number of attempts
    """
    count_ls = []
    min_number = 1
    max_number = 101
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(min_number, max_number, size=(count_iteration))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(min_number, max_number, number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
