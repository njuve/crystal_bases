from typing import Union, List, Set, Dict
import src.young.tableau as tableau
from highest_weight_crystal import HighestWeightCrystal
from typing import Any


def wt(tab: tableau.Tableau) -> list:
    """weight function

    Args:
        tab: tableau.Tableau [description]

    Returns:
        list: [description]

    Examples:
        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 2]], orientation='row')
        >>> wt(tab)
        [2, 2, 0]
    """
    return Wt().wt(tab=tab)


def f(i: int) -> Any:
    """lowering operator f

    Args:
        i: int

    Returns:
        tableau.Tableau: [description]

    Examples:
        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 2]], orientation='row')
        >>> f(i=1)(tab) # return None

        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 2]], orientation='row')
        >>> f(i=2)(tab).box()
        [[1, 1], [2, 3]]
    """

    def _f(tab: tableau.Tableau) -> Union[tableau.Tableau, None]:
        return F().f(i=i, tab=tab)

    return _f


def e(i: int) -> Any:
    """raiging operator e

    Args:
        i: int

    Returns:
        tableau.Tableau: [description]

    Examples:
        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 3]], orientation='row')
        >>> e(i=1)(tab)

        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 3]], orientation='row')
        >>> e(i=2)(tab).box()
        [[1, 1], [2, 2]]
    """

    def _e(tab: tableau.Tableau) -> Union[str, None]:
        return E().e(i=i, tab=tab)

    return _e


def phi(i: int) -> Any:
    """phi

    Args:
        i: int

    Returns:
        int: [description]

    Examples:
        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 2]], orientation='row')
        >>> phi(i=1)(tab)
        0

        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 2]], orientation='row')
        >>> phi(i=2)(tab)
        2
    """

    def _phi(tab: tableau.Tableau) -> str:
        return Phi().phi(i=i, tab=tab)

    return _phi


def epsilon(i: int) -> Any:
    """phi

    Args:
        i: int

    Returns:
        int: [description]

    Examples:
        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 3]], orientation='row')
        >>> epsilon(i=1)(tab)
        0

        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 3]], orientation='row')
        >>> epsilon(i=2)(tab)
        1
    """

    def _epsilon(tab: tableau.Tableau) -> Union[tableau.Tableau, None]:
        return Epsilon.epsilon(i=i, tab=tab)

    return _epsilon


class Wt:
    def wt(self, tab: tableau.Tableau) -> list:
        return tab.weight()


class F:
    def get_reading(
        self, tab: tableau.Tableau, reading="far_eastern"
    ) -> List[Dict[str, Union[int, None]]]:
        reading = []
        boxes = tab.box()
        for row_num, row in enumerate(boxes):
            for col_num_re, box in enumerate(row[::-1]):
                reading = reading + [
                    {
                        "row": row_num,
                        "col": len(row) - col_num_re - 1,
                        "word": box,
                    }
                ]

        return reading

    def get_signature(
        self, reading: List[Dict[str, Union[int, None]]], i: int
    ) -> List[Dict[str, Union[int, None]]]:
        signature = [
            box
            if (box["word"] == i) or (box["word"] == i + 1)
            else {"row": box["row"], "col": box["col"], "word": None}
            for box in reading
        ]
        return signature

    def signature_rule(
        self, signature: List[Dict[str, Union[int, None]]], i: int
    ) -> Dict[str, Union[Dict[str, Union[int, None]], int, None]]:
        plus: int = 0
        minus: int = 0
        act_point: Dict[str, Union[int, None]] = {"row": None, "col": None}
        for box in signature:
            if box["word"] == i:
                plus = plus + 1
                if plus == 1:
                    act_point = {"row": box["row"], "col": box["col"]}
            if box["word"] == i + 1:
                if plus > 0:
                    plus = plus - 1
                    if plus == 0:
                        act_point = {"row": None, "col": None}
                elif plus == 0:
                    minus = minus + 1
                    act_point = {"row": None, "col": None}

        return {"act_point": act_point, "i": plus, "i+1": minus}

    def f(self, i: int, tab: tableau.Tableau) -> tableau.Tableau:
        reading = self.get_reading(tab=tab, reading="far_eastern")
        signature = self.get_signature(reading=reading, i=i)
        result = self.signature_rule(signature=signature, i=i)
        act_point = result["act_point"]
        if (act_point["row"] is None) & (act_point["col"] is None):
            return None
        else:
            boxes = tab.box()
            boxes[act_point["row"]][act_point["col"]] = i + 1
            return tableau.Tableau(boxes=boxes, orientation="row")


class E:
    def get_reading(
        self, tab: tableau.Tableau, reading="far_eastern"
    ) -> List[Dict[str, Union[int, None]]]:
        reading = []
        boxes = tab.box()
        for row_num, row in enumerate(boxes):
            for col_num_re, box in enumerate(row[::-1]):
                reading = reading + [
                    {
                        "row": row_num,
                        "col": len(row) - col_num_re - 1,
                        "word": box,
                    }
                ]

        return reading

    def get_signature(
        self, reading: List[Dict[str, Union[int, None]]], i: int
    ) -> List[Dict[str, Union[int, None]]]:
        signature = [
            box
            if (box["word"] == i) or (box["word"] == i + 1)
            else {"row": box["row"], "col": box["col"], "word": None}
            for box in reading
        ]
        return signature

    def signature_rule(
        self, signature: List[Dict[str, Union[int, None]]], i: int
    ) -> Dict[str, Union[Dict[str, Union[int, None]], int, None]]:
        plus: int = 0
        minus: int = 0
        act_point: Dict[str, Union[int, None]] = {"row": None, "col": None}
        for box in signature:
            if box["word"] == i:
                plus = plus + 1
            if box["word"] == i + 1:
                if plus > 0:
                    plus = plus - 1
                elif plus == 0:
                    minus = minus + 1
                    act_point = {"row": box["row"], "col": box["col"]}

        return {"act_point": act_point, "i": plus, "i+1": minus}

    def e(self, i: int, tab: tableau.Tableau) -> tableau.Tableau:
        reading = self.get_reading(tab=tab, reading="far_eastern")
        signature = self.get_signature(reading=reading, i=i)
        result = self.signature_rule(signature=signature, i=i)
        act_point = result["act_point"]
        if (act_point["row"] is None) & (act_point["col"] is None):
            return None
        else:
            boxes = tab.box()
            boxes[act_point["row"]][act_point["col"]] = i
            return tableau.Tableau(boxes=boxes, orientation="row")


class Phi:
    def phi(self, i: int, tab: tableau.Tableau) -> tableau.Tableau:
        return


class Epsilon:
    def epsilon(self, i: int, tab: tableau.Tableau) -> tableau.Tableau:
        return