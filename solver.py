from typing import List, Tuple

import numpy as np


def small_square_axis(idx: int) -> Tuple[int, int]:
    start = idx // 3 * 3
    end = start + 3
    return start, end


def small_square(board: np.array, x: int, y: int) -> np.array:
    x_start, x_end = small_square_axis(x)
    y_start, y_end = small_square_axis(y)
    return board[x_start: x_end, y_start: y_end]


def answer_space(board: np.array, x: int, y: int) -> List[int]:
    assert board[x, y] == 0
    return list(set(range(1, 10)) - set(board[x, :]) - set(board.T[y, :]) - set(list(small_square(board, x, y).flat)))


def trial(board: np.array) -> bool:
    holes = np.argwhere(board == 0)
    if holes.size == 0:
        return True

    x, y = holes[0]
    possible_answers = answer_space(board, x, y)
    if not possible_answers:
        return False

    for v in possible_answers:
        board[x, y] = v
        result = trial(board)
        if result:
            return True
    board[x, y] = 0
    return False


def setup_board(values: List[Tuple[int, int, int]]) -> np.array:
    x, y, z = zip(*values)
    board = np.zeros(shape=(9, 9), dtype='int8')
    board[x, y] = z
    return board


def main() -> None:
    test_values = [
        (0, 0, 5),
        (0, 1, 3),
        (0, 4, 7),
        (1, 0, 6),
        (1, 3, 1),
        (1, 4, 9),
        (1, 5, 5),
        (2, 1, 9),
        (2, 2, 8),
        (2, 7, 6),
        (3, 0, 8),
        (3, 4, 6),
        (3, 8, 3),
        (4, 0, 4),
        (4, 3, 8),
        (4, 5, 3),
        (4, 8, 1),
        (5, 0, 7),
        (5, 4, 2),
        (5, 8, 6),
        (6, 1, 6),
        (6, 6, 2),
        (6, 7, 8),
        (7, 3, 4),
        (7, 4, 1),
        (7, 5, 9),
        (7, 8, 5),
        (8, 4, 8),
        (8, 7, 7),
        (8, 8, 9)
    ]
    board = setup_board(test_values)
    print('Question', board, sep='\n')
    trial(board)
    print('Answer', board, sep='\n')


if __name__ == '__main__':
    main()
