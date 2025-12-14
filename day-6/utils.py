from typing import List

# represents an individual math problem in the homework assignment
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


# translate text input into a list of problems
# read values human way (row by row)
def read_input(file_name: str = 'input.txt') -> List[Problem]:
    input = []
    with open(file_name, 'r') as file:
        # convert text into 2d array of strings
        for line in file:
            row = line.replace('\n', '').split()
            input.append(row)

    problems = []
    for i in range(len(input[0])):
        # each column of the grid represents an individual problem
        function = input[-1][i]
        values = [int(input[j][i]) for j in range(len(input)-1)]
        problems.append(Problem(function, values))

    return problems


# translate text input into a list of problems
# read values cephalopod way (column by column)
def read_cephalopod_input(file_name: str = 'input.txt') -> List[Problem]:
    input = []
    with open(file_name, 'r') as file:
        for line in file:
            row = line.replace('\n', '')
            input.append(row)

    problems = []
    i, j = len(input[0])-1, len(input[0])
    while i >= 0:
        # each problem is left-aligned with the function symbol in the last line of the file
        if input[-1][i] != ' ':
            function = input[-1][i]
            values = []
            # each value is a vertical column from the current function to the previous one (moving R->L)
            for x in range(i, j):
                val = ''
                for y in range(len(input)-1):
                    val += input[y][x]
                values.append(int(val.strip()))
            problems.append(Problem(function, values))
            j = i - 1
        i -= 1

    return problems


if __name__ == "__main__":
    input = read_input('example.txt')
    assert input[0].solve() == 33210
    assert input[1].solve() == 490
    assert input[2].solve() == 4243455
    assert input[3].solve() == 401

    input = read_cephalopod_input('example.txt')
    assert input[0].solve() == 1058
    assert input[1].solve() == 3253600
    assert input[2].solve() == 625
    assert input[3].solve() == 8544