from typing import List, Tuple


# reads text file into list of fresh id ranges and a list of ids in inventory
def read_input(file_name: str = 'input.txt') -> Tuple[List[List[int]], List[int]]:
    fresh, inventory = [], []
    with open(file_name) as file:
        line_break = False
        for line in file:
            line = line.strip()
            if line:
                if line_break:
                    inventory.append(int(line))
                else:
                    fresh_range = line.split('-')
                    fresh.append([int(x) for x in fresh_range])
            else:
                line_break = True

    return (fresh, inventory)


# sort and reduce ranges to minimum required
def optimize_ranges(ranges: List[List[int]]) -> List[List[int]]:
    # sort by minimum value
    ranges = sorted(ranges)

    i = 0
    j = len(ranges) - 1
    # 
    while i < j:
        # check if the current range overlaps with the next
        if ranges[i][1] >= ranges[i+1][0]:
            # merge the overlapping ranges
            # range[i][0] < range[i+1][0] bc the list is sorted
            ranges[i][1] = max(ranges[i][1], ranges[i+1][1])
            del ranges[i+1]
            j -= 1
        else:
            i += 1

    return ranges


# check if an id is within one of the given ranges
def id_in_ranges(id: int, ranges: List[List[int]]) -> bool:
    for r in ranges:
        if id <= r[1]:
            if id >= r[0]:
                # only need to be inside of one range
                return True
            # a valid id < r[0] would have been picked up in a previous range
            return False
    return False


# count the number of valid ids in given ranges
# only works if the ranges are optimized first!
def count_ids_in_ranges(ranges: List[List[int]]) -> int:
    sum = 0

    for r in ranges:
        sum += r[1] - r[0] + 1

    return sum
        

if __name__ == "__main__":
    fresh, inventory = read_input('example.txt')
    fresh = optimize_ranges(fresh)

    assert id_in_ranges(1, fresh) == False
    assert id_in_ranges(5, fresh) == True
    assert id_in_ranges(8, fresh) == False
    assert id_in_ranges(11, fresh) == True
    assert id_in_ranges(17, fresh) == True
    assert id_in_ranges(32, fresh) == False
    
    for i in range(len(fresh)-1):
        assert fresh[i][1] < fresh[i+1][0]

    assert count_ids_in_ranges(fresh) == 14