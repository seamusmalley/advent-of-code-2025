from typing import List, Tuple

def read_input(file_name: str = 'input.txt') -> List[List[int]]:
    input = []
    with open(file_name) as file:
        for line in file:
            bank = []
            for char in line:
                if char in '0123456789':
                    bank.append(int(char))
            input.append(bank)

    return input


def max_joltage(battery_bank: List[int], num_batteries: int) -> int:
    i = 0
    max_joltage = ''
    for j in range(num_batteries):
        start = i + j
        end = (j - num_batteries + 1) if (j - num_batteries + 1) < 0 else len(battery_bank)

        val, k = find_max_digit(battery_bank[start:end])

        i += k
        max_joltage += str(val)
    return int(max_joltage)


def find_max_digit(lst: List[int]) -> Tuple[int]:
    max_val, max_val_loc = 0, len(lst) + 1

    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_val_loc = i

    return (max_val, max_val_loc)


if __name__ == "__main__":
    assert max_joltage([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], 2) == 98
    assert max_joltage([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], 2) == 89
    assert max_joltage([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], 2) == 78
    assert max_joltage([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1], 2) == 92

    assert max_joltage([9,8,7,6,5,4,3,2,1,1,1,1,1,1,1], 12) == 987654321111
    assert max_joltage([8,1,1,1,1,1,1,1,1,1,1,1,1,1,9], 12) == 811111111119
    assert max_joltage([2,3,4,2,3,4,2,3,4,2,3,4,2,7,8], 12) == 434234234278
    assert max_joltage([8,1,8,1,8,1,9,1,1,1,1,2,1,1,1], 12) == 888911112111