from typing import List
from utils import (
    JunctionBox,
    Circuit,
    read_input
)


def build_circuits(boxes: List[JunctionBox], connections: int, num_largest_circuits: int = 3) -> int:
    circuits = []
    for box in boxes:
        circuit = Circuit()
        circuit.add(box)
        circuits.append(circuit)

    print(circuits)
    return 0


if __name__ == "__main__":
    example_input = read_input('example.txt')
    assert build_circuits(example_input, 10) == 40