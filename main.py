import numpy as np
import random


def random_state(width, height):
    board = [[random.random() for i in range(width)]] * height


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(random_state(5, 5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
