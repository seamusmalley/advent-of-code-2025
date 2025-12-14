from typing import List
from utils import read_input,  split_beams, split_timelines


# Part 1
# Count the number of times the tachyon beam splits according to a given manifold
def count_beam_splits(input: List[str]) -> int:
    split_count = 0
    beams = []

    for row in input:
        splits, beams = split_beams(beams, row)
        split_count += splits

    return split_count


# Part 2
# Count the number of times the tachyon timeline splits according to the given manifold
def count_timeline_splits(input: List[str]) -> int:
    split_count = 0
    beams = {}

    for row in input:
        splits, beams = split_timelines(beams, row)
        split_count += splits

    return split_count


if __name__ == "__main__":
    example_input = read_input('example.txt')
    assert count_beam_splits(example_input) == 21
    assert count_timeline_splits(example_input) == 40

    input = read_input()
    print(f'Part 1: {count_beam_splits(input)}')
    print(f'Part 2: {count_timeline_splits(input)}')