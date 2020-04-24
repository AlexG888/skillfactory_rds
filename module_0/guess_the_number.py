
def score_game(game_core_v3):
    
    """
    Function starts the game 1000
    The guessed number is from 1 to 100
    Returns the average number of required attempts
    
    """
    import numpy as np
    count_ls = []
    np.random.seed(1)  
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core_v3(number))    
    score = int(np.mean(count_ls))
    
    return(print(f"Алгоритм угадывает число в среднем за {score} попыток"))


def game_core_v3(number):
    
    """
    The implementation of the binary search algorithm for the hidden number
    The function takes the requested number and returns the number of attempts

    """
    first = 1 
    last = 100
    count = 0
    
    while first <= last:
        count += 1
        predict = (first + last)//2
        if predict == number:
            return count
        elif predict > number:
            last = predict - 1
        else:
            first = predict + 1

