from typing import List

# parse string input into start/end pairs of the ranges to be evaluated
def read_input(file_name: str = 'input.txt') -> List[List[str]]:
    with open(file_name, 'r') as file:
        for line in file:
            ranges = [range.split('-') for range in line.split(',')]

    return ranges


# determine if an id is valid, return its numeric value if its not
def validate(id: int) -> int:
    id = str(id)
    if len(id) % 2 == 0:
        if id[:len(id)//2] == id[len(id)//2:]:
            return int(id)
    return 0


# part 2 validation
def strict_validate(id: int) -> int:
    id = str(id)

    if len(id) < 2:
        return 0
    
    for i in range(1, (len(id) // 2) + 1):
        sequence = id[:i]

        if sequence * (len(id) // len(sequence)) == id:
            return int(id)

    return 0    


if __name__ ==  "__main__":
    for i in range(11, 23):
        print(strict_validate(i))