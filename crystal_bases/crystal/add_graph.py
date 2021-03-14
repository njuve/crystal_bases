import networkx as nx
from typing import Any, Union
from crystal_bases.crystal.crystal_graph import CrystalGraph, crystal_graph
from crystal_bases.young.tableau import Tableau, tableau
from crystal_bases.young.pr import pr


def add_graph(crystal_graph: CrystalGraph, operator: Any) -> nx.DiGraph:
    """add graph to a crystal graph

    Args:
        crystal_graph: CrystalGraph
        operator: Any

    Returns:
        nx.DiGraph: [description]

    Examples:
        >>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
        >>> B = crystal_graph(tab = tab, n = 3)
        >>> add_graph(crystal_graph = B, operator = pr(n=3))
    """
    return AddGraph().add_graph(crystal_graph=crystal_graph, operator=operator)


class AddGraph:
    def add_edge(self, G: nx.DiGraph, operator: Any, tab: Tableau) -> Any:
        if operator(tab) is not None:
            op_tab = operator(tab)
            G.add_edge(tab)
            return self.add_edge(G, operator, op_tab)
        else:
            return G

    def add_graph(self, crystal_graph: CrystalGraph, operator: Any) -> nx.DiGraph:
        return self.add_edge(
            G=crystal_graph.G, operator=operator, tab=crystal_graph.tab
        )
