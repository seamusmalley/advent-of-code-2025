from typing import List, Tuple, Dict


# read text input into a list of strings
def read_input(file_name: str = 'input.txt') -> List[str]:
    with open(file_name, 'r') as file:
        input = []
        for line in file:
            input.append(line.replace('\n', ''))

    return input


# given the positions of the beams entering a row, 
# determine the number of splits and the positions of the beams exiting that row
def split_beams(beams: List[int], row: str) -> Tuple[int, List[int]]:
    if not beams:
        return 0, [row.find('S')]
    
    split_count = 0
    beams_out = []
    for index in beams:
        # split the beam
        if row[index] == '^':
            split_count += 1
            if index > 0:
                beams_out.append(index-1)
            if index < len(row)-1:
                beams_out.append(index+1)
        else:
            beams_out.append(index)

    # return deduplicated list
    beams_out = list(set(beams_out))
    return split_count, beams_out


# given the positions of the beam in all timelines entering a row, 
# determine the number of timelines created and the positions of the beams exiting that row in all timelines
# swapped to dict over list for time and memory efficiency
def split_timelines(beam_count_map: Dict[int, int], row: str) -> Tuple[int, Dict[int, int]]:
    if not beam_count_map:
        return 1, {row.find('S'): 1}
    
    timelines_added = 0
    beams_out = {}
    for index in beam_count_map:
        # split the timeline
        if row[index] == '^':
            # each split creates a new timeline for each existing timeline that reaches this split
            timelines_added += beam_count_map[index]
            if index > 0:
                if beams_out.get(index-1):
                    beams_out[index-1] += beam_count_map[index]
                else:
                    beams_out[index-1] = beam_count_map[index]
            if index < len(row)-1:
                if beams_out.get(index+1):
                    beams_out[index+1] += beam_count_map[index]
                else:
                    beams_out[index+1] = beam_count_map[index]
        else:
            if beams_out.get(index):
                beams_out[index] += beam_count_map[index]
            else:
                beams_out[index] = beam_count_map[index]

    return timelines_added, beams_out


if __name__ == "__main__":
    input = read_input('example.txt')