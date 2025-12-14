from typing import List
from utils import Problem, read_input,  read_cephalopod_input

# Part 1
def do_math_homework(problems: List[Problem]) -> int:
    answer_sum = 0
    for problem in problems:
        answer_sum += problem.solve()
    return answer_sum


if __name__ == "__main__":
    example = read_input('example.txt')
    assert do_math_homework(example) == 4277556

    input = read_input()
    print(f'Part 1: {do_math_homework(input)}')
    
    ceph_input = read_cephalopod_input()
    print(f'Part 2: {do_math_homework(ceph_input)}')