from typing import List
from utils import read_input, evil_modulo

# Part 1
# given a list of directions, return the number of times the dial is at 0
def count_dial_at_zero(steps: List[int], dial_size: int = 100, dial_start: int = 50) -> int:
    count = 0
    dial = dial_start

    for step in steps:
        dial = (dial + step) % dial_size
        if dial == 0:
            count += 1

    return count


# Part 2
# given a list of directions, return the number of times the dial crosses 0
def count_dial_crosses_zero(steps: List[int], dial_size: int = 100, dial_start: int = 50) -> int:
    count = 0
    dial = dial_start

    for step in steps:
        count += abs(step) // dial_size
        reduced_step = evil_modulo(step, dial_size)

        if ((dial + reduced_step) >= dial_size):
            count += 1
        elif ((dial > 0) and ((dial + reduced_step) <= 0)):
            count += 1

        dial = (dial + step) % dial_size
    
    return count


if __name__ == "__main__":
    steps = read_input()
    print(f'Part 1: {count_dial_at_zero(steps)}')
    print(f'Part 2: {count_dial_crosses_zero(steps)}')
