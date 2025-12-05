from typing import List
from utils import validate, read_input, strict_validate

# sum the invalid ids, strict flag is for enhanced requirements of Part 2
def sum_invalid_ids(id_ranges: List[List[str]], strict: bool = False) -> int:
    sum = 0

    for id_range in id_ranges:
        start = int(id_range[0])
        end = int(id_range[1])

        for id in range(start, end + 1):
            if strict:
                sum += strict_validate(id)
            else:
                sum += validate(id)

    return sum


if __name__ == "__main__":
    id_ranges = read_input()
    print(f'Part 1: {sum_invalid_ids(id_ranges)}')
    print(f'Part 2: {sum_invalid_ids(id_ranges, strict=True)}')