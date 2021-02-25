from dataclasses import dataclass, field
from typing import Union, List
import tableau

def jeu_de_taquin(tab: tableau.Tableau) -> tableau.Tableau:
    """jeu de taquin

    Args:
        tableau: tableau.Tableau

    Returns:
        tableau.Tableau:

    Example
    >>> tab = tableau.Tableau(boxes=[[1, 1], [2, None]], orientation='row')
    >>> jeu_de_taquin(tab)
    tableau.Tableau(boxes=[[None, 1], [1, 2]], orientation='row')
    """
    return JeuDeTaquin().jeu_de_taquin(tab)


class JeuDeTaquin:
    def get_null_boxes(self, tab: tableau.Tableau):
        null_boxes = []
        boxes = tab.box()
        for row_num, row in enumerate(boxes):
            for col_num, col in enumerate(row):
                if col == None:
                    null_boxes = null_boxes + [{'row': row_num, 'col': col_num}]

        return null_boxes

    def move(self, tab: tableau.Tableau, direction='back')

    def backmove(self, tab: tableau.Tableau, box_pos: dict):
        boxes = tab.box()
        row_num = box_pos['row']
        col_num = box_pos['col']
        box = boxes[row_num][col_num]
        above = boxes[row_num-1][col_num] if row_num != 0 else 0
        left = boxes[row_num][col_num-1] if col_num != 0 else 0

        if left > above:
            boxes[row_num][col_num], boxes[row_num][col_num-1] = left, box
        else:
            boxes[row_num][col_num], boxes[row_num-1][col_num] = above, box

        return tableau.Tableau(boxes=boxes, orientation='row')

    def forwordmove(self):
        pass

    def jeu_de_taquin(self, tab: tableau.Tableau):
        null_boxes = self.get_null_boxes(tab)
        for null_box in null_boxes:
            tab = self.backmove(tab, null_box)

        return tab

