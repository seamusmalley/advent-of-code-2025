from typing import List
from math import sqrt


class JunctionBox:
    x: int
    y: int
    z: int

    def __init__(self, x: str, y: str, z: str):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __repr__(self):
        return f'({self.x},{self.y},{self.z})'

    def distance_to(self, box: JunctionBox):
        dif_x = self.x - box.x
        dif_y = self.y - box.y
        dif_z = self.z - box.z

        return sqrt(dif_x**2 + dif_y**2 + dif_z**2)
    

class Circuit:
    size: int
    boxes: List[JunctionBox]

    def __init__(self):
        self.size = 0
        self.boxes = []

    def __repr__(self):
        return str(self.boxes)

    def add(self, box: JunctionBox):
        self.size += 1
        self.boxes.append(box)

    def join(self, circuit: JunctionBox):
        self.size += circuit.size
        self.boxes.extend(circuit.boxes)
        

def read_input(file_name: str = 'input.txt') -> List[JunctionBox]:
    boxes = []
    with open(file_name, 'r') as file:
        for line in file:
            coords = line.replace('\n', '').split(',')
            boxes.append(JunctionBox(coords[0], coords[1], coords[2]))

    return boxes


if __name__ == "__main__":
    example = read_input('example.txt')
    circuit = Circuit()
    for box in example:
        circuit.add(box)

    print(circuit)