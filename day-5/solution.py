from typing import List
from utils import read_input, optimize_ranges, id_in_ranges, count_ids_in_ranges


# Part 1
# given a list of fresh id ranges and a list of inventory, count the number of fresh ids
def count_fresh_ingredients(fresh_id_ranges: List[List[int]], inventory: List[int]) -> int:
    # sort and reduce ranges
    fresh_id_ranges = optimize_ranges(fresh_id_ranges)

    count = 0
    for id in inventory:
        # increment count if the id is in any of the ranges
        count += id_in_ranges(id, fresh_id_ranges)

    return count

# Part 2
# given a list of fresh id ranges, count the number of 
def count_fresh_ids(fresh_id_ranges: List[List[int]]) -> int:
    fresh_id_ranges = optimize_ranges(fresh_id_ranges)

    return count_ids_in_ranges(fresh_id_ranges)


if __name__ == "__main__":
    example_fresh, example_inventory = read_input('example.txt')
    assert count_fresh_ingredients(example_fresh, example_inventory) == 3
    assert count_fresh_ids(example_fresh) == 14

    fresh_ids, inventory = read_input()
    print(f'Part 1: {count_fresh_ingredients(fresh_ids, inventory)}')
    print(f'Part 2: {count_fresh_ids(fresh_ids)}')