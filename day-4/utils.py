from typing import List

# convert text file into 2D array of 0s and 1s
def read_input(file_name: str = 'input.txt') -> List[List[int]]:
    with open(file_name) as file:
        input = []
        for line in file:
            row = []
            for x in line:
                if x == '@':
                    row.append(1)
                elif x == '.':
                    row.append(0)
            input.append(row)
        return input
    

# find the number of adjacent rolls of paper
def num_neighbors(board: List[List[int]], x: int, y: int) -> int:
    poss_x, poss_y = [x], [y]

    # a roll can't be its own neighbor
    sum = -board[x][y]

    # loop around current roll, but stay on the board
    for i in range(max(0, x-1), min(x+1, len(board)-1)+1):
        for j in range(max(0, y-1), min(y+1, len(board)-1)+1):
            sum += board[i][j]

    return sum


if __name__ == "__main__":
    # test cases given in problem statement
    example_board = read_input('example.txt')
    assert num_neighbors(example_board, 0, 2) == 3
    assert num_neighbors(example_board, 4, 4) == 8
    assert num_neighbors(example_board, 0, 0) == 2
    assert num_neighbors(example_board, 9, 9) == 2