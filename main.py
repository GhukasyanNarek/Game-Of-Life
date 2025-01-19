import random
import time

ALIVE = '█'
DEAD = ' '


def dead_state(board_width, board_height):
    return [[0 for _ in range(board_width)] for _ in range(board_height)]


def random_state(board_width, board_height):
    board = [[random.random() for _ in range(board_width)] for _ in range(board_height)]

    for i in range(board_height):
        for j in range(board_width):
            board[i][j] = 1 if board[i][j] > 0.5 else 0
    return board


def render(board):
    rendered_board = ''

    for row in board:
        for cell in row:
            rendered_board += ALIVE if cell == 1 else DEAD
        rendered_board += '\n'

    return rendered_board


def get_height(board):
    return len(board)


def get_width(board):
    return len(board[0])


def is_alive(x, y, board):
    return board[x][y] == 1


def cell_next_state(x, y, board, board_width, board_height):
    alive_neighbors = 0

    for x1 in range(x - 1, x + 2):
        if x1 < 0 or x1 >= board_height:
            continue
        for y1 in range(y - 1, y + 2):
            if y1 < 0 or y1 >= board_width or (x1 == x and y1 == y):
                continue
            if is_alive(x1, y1, board):
                alive_neighbors += 1

    if (alive_neighbors == 3 and not is_alive(x, y, board)) or (2 <= alive_neighbors <= 3 and is_alive(x, y, board)):
        return 1
    else:
        return 0


def get_next_state(board, board_width, board_height):
    next_state = dead_state(board_width, board_height)
    for row in range(board_height):
        for col in range(board_width):
            next_state[row][col] = cell_next_state(row, col, board, board_width, board_height)

    return next_state


def run_forever(init_state, board_width, board_height):
    next_state = init_state
    while True:
        print(render(next_state))
        next_state = get_next_state(next_state, board_width, board_height)
        time.sleep(0.5)


if __name__ == "__main__":
    width, height = 200, 50
    start = random_state(width, height)
    run_forever(start, width, height)
