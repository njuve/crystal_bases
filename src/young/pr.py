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
    return
