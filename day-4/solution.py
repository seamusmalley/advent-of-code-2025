from typing import List
from utils import read_input, num_neighbors

def find_num_accessible_rolls(board: List[List[int]], max_adj_rolls: int) -> int:
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] and (num_neighbors(board, i, j) < max_adj_rolls):
                count += 1
    return count


def move_rolls(board: List[List[int]], max_adj_rolls: int) -> int:
    rolls_moved = 0
    rolls_to_move = True

    while rolls_to_move:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] and num_neighbors(board, i, j) < max_adj_rolls:
                    count += 1
                    board[i][j] = 0
        if count == 0:
            rolls_to_move = False
        else:
            rolls_moved += count

    return rolls_moved


if __name__ == "__main__":
    test_input = read_input('example.txt')
    assert find_num_accessible_rolls(test_input, 4) == 13
    assert move_rolls(test_input, 4) == 43

    input = read_input()
    print(f'Part 1: {find_num_accessible_rolls(input, 4)}')
    print(f'Part 2: {move_rolls(input, 4)}')