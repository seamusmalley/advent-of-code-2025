from typing import List
from utils import read_input, max_joltage

def sum_max_joltage(banks: List[List[int]], num_batteries: int) -> int:
    sum = 0
    for bank in banks:
        sum += max_joltage(bank, num_batteries)

    return sum


if __name__ == "__main__":
    input = read_input()
    print(f'Part 1: {sum_max_joltage(input, 2)}')
    print(f'Part 2: {sum_max_joltage(input, 12)}')