from typing import List

class Problem:
    function: str
    values: List[int]

    def __init__(self, function, values):
        self.function = function
        self.values = values
    

    def __repr__(self):
        result = ''
        for value in self.values:
            result += str(value)
            result += self.function
        return result[:-1]


    def solve(self):
        if self.function == '*':
            result = 1
            for value in self.values:
                result *= value
        elif self.function == '+':
            result = 0
            for value in self.values:
                result += value
        else:
            # not supported
            return -1
        return result


def read_input(file_name: str = 'input.txt') -> List[Problem]:
    input = []
    with open(file_name, 'r') as file:
        for line in file:
            row = line.replace('\n', '').split()
            input.append(row)

    problems = []
    for i in range(len(input[0])):
        function = input[-1][i]
        values = [int(input[j][i]) for j in range(len(input)-1)]
        problems.append(Problem(function, values))

    return problems



if __name__ == "__main__":
    input = read_input('example.txt')
    assert input[0].solve() == 33210
    assert input[1].solve() == 490
    assert input[2].solve() == 4243455
    assert input[3].solve() == 401