from typing import List

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
    

def num_neighbors(board: List[List[int]], x: int, y: int) -> int:
    poss_x, poss_y = [x], [y]

    if x > 0:
        poss_x.append(x-1)
    if x < len(board)-1:
        poss_x.append(x+1)
    if y > 0:
        poss_y.append(y-1)
    if y < len(board[x])-1:
        poss_y.append(y+1)

    sum = -board[x][y]
    for i in poss_x:
        for j in poss_y:
            sum += board[i][j]

    return sum


if __name__ == "__main__":
    example_board = read_input('example.txt')
    assert num_neighbors(example_board, 0, 2) == 3
    assert num_neighbors(example_board, 4, 4) == 8
    assert num_neighbors(example_board, 0, 0) == 2
    assert num_neighbors(example_board, 9, 9) == 2