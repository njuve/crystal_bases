from dataclasses import dataclass, field
from typing import Union, List
import tableau

def pr(tab: tableau.Tableau) -> tableau.Tableau:
    """Schutzenberger's promotion operator

    Args:
        tab: tableau.Tableau

    Returns:
        tableau.Tableau:

    Examples:
    >>> pr(tableau.tableau(boxes=[[1, 1], [2, 2]], orientation='row')).box()
    [[2, 2], [3, 3]]

    >>> pr(tableau.tableau(boxes=[[1, 1], [2, 3]], orientation='row')).box()
    [[1, 2], [2, 3]]

    """
    return Pr().pr(tab)

@dataclass(frozen=True)
class Pr:
    def remove_ns(self, tab:tableau.Tableau) -> tableau.Tableau:
        return

    def add_1s(self, tab:tableau.Tableau) -> tableau.Tableau:
        return

    def fill_nulls(self, tab:tableau.Tableau) -> tableau.Tableau:
        return

    def jue_de_taquin_move(self, tab:tableau.Tableau) -> tableau.Tableau:
        return

    def pr(self, tab: tableau.Tableau) -> tableau.Tableau:
        return
