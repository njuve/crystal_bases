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
    return JeuDeTaquin.jeu_de_taquin(tab)


class JeuDeTaquin:
    tab: list = field(init=True, repr=True, compare=False)

    def find_null_box(self):
        return

    def backmove(self):
        return

    def forwordmove(self):
        return

    def jeu_de_taquin(self):
        return

