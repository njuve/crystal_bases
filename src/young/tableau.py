from dataclasses import dataclass, field
from typing import Union, List

def tableau(boxes: List[list], orientation='row') -> Tableau:
    """
    Generate Young tableau.

    Args:
        boxes: list
        orientation: str, optional
            Defaults to 'row'.

    Returns:
        list: [description]

    Examples:
    >>> tableau([[1, 2, 3], [2]]).box()
    [[1, 2, 3], [2]]

    >>> tableau([[1, 2, 3], [2]]).shape()
    [3, 1]

    >>> tableau([[1, 2, 3], [2]]).weight()
    [1, 2, 1]

    """
    return Tableau(boxes = boxes, orientation = orientation)


@dataclass(frozen=True)
class Tableau:
    boxes: List[list] = field(init=True, repr=True, compare=False)
    orientation: str = field(init=True, repr=True, compare=False)

    def shape(self) -> list:
        return [len(row) for row in self.boxes]

    def weight(self) -> list:
        weight = []
        n = len(self.boxes) + 1 # the number of columns + 1
        for i in range(1, n+1):
            count_i = 0
            for row in self.boxes:
                for box in row:
                    if box == i:
                        count_i = count_i + 1
            weight = weight + [count_i]

        return weight

    def box(self) -> List[list]:
        return self.boxes
