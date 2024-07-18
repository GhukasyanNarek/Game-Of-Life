import numpy as np
import random


def random_state(width, height):
    board = [[random.random() for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            board[i][j] = 1 if board[i][j] > 0.5 else 0
    return board


def render(board):
    alive = '#'  # alive = '█'
    dead = ' '

    height = len(board)
    width = len(board[0])

    rendered_board = ' ' + '-' * width + '\n'

    for row in board:
        rendered_row = '|'
        for cell in row:
            rendered_row += alive if cell == 1 else dead
        rendered_row += '|\n'
        rendered_board += rendered_row

    rendered_board += ' ' + '-' * width

    return rendered_board


if __name__ == '__main__':
    # print(random_state(30, 30))
    print(f"After Rendering{render(random_state(6, 4))}")
