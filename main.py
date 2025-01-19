import numpy as np
import random


def random_state(width, height):
    board = [[random.random() for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            board[i][j] = 1 if board[i][j] > 0.5 else 0
    return board


def render(board):
    alive = '█'
    dead = ' '

    height = len(board)
    width = len(board[0])
    return width, height


if __name__ == '__main__':
    print(random_state(6, 4))
    print(f"Dims: {render(random_state(6, 4))}")
