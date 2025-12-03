from typing import List, Tuple

# convert combination lock input into list of integers
# e.g. L68 -> -68, R48 -> +48
def read_input(file_name: str = 'input.txt') -> List[int]:
    steps = []
    with open(file_name, 'r') as file:
        for line in file:
            val = int(line[1:])
            if line[0] == 'L':
                val = -val
            steps.append(val)
    return steps

# fake modulo that handles negative numbers the way I want for this problem
def evil_modulo(a: int, n: int) -> int:
    if a >= 0:
        return a % n
    
    a = abs(a)
    return -(a % n)


def test_evil_modulo():
    assert evil_modulo(59, 100) == 59
    assert evil_modulo(3948, 100) == 48
    assert evil_modulo(-123, 100) == -23
    assert evil_modulo(-4, 100) == -4

if __name__ == "__main__":
    test_evil_modulo()