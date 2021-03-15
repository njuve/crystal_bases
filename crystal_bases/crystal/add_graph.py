import networkx as nx
from typing import Any
from crystal_bases.crystal.crystal_graph import CrystalGraph
from crystal_bases.young.tableau import Tableau


def add_graph(crystal_graph: CrystalGraph, operator: Any) -> nx.DiGraph:
    """add graph stucture to a crystal graph

    Args:
        crystal_graph: CrystalGraph
        operator: Any

    Returns:
        nx.DiGraph: [description]

    Examples:
        >>> from crystal_bases.crystal.crystal_graph import crystal_graph
        >>> from crystal_bases.young.tableau import tableau
        >>> from crystal_bases.young.pr import pr
        >>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
        >>> B = crystal_graph(tab = tab, n = 3)
        >>> G = add_graph(crystal_graph = B, operator = pr(n=3))
        >>> B.G.nodes
        NodeView((Tableau(boxes=[[2, 2], [3, 3]], orientation='row'), Tableau(boxes=[[1, 2], [2, 3]], orientation='row'), Tableau(boxes=[[1, 2], [3, 3]], orientation='row'), Tableau(boxes=[[1, 1], [2, 3]], orientation='row'), Tableau(boxes=[[1, 1], [3, 3]], orientation='row'), Tableau(boxes=[[1, 1], [2, 2]], orientation='row')))
    """
    return AddGraph().add_graph(crystal_graph=crystal_graph, operator=operator)


class AddGraph:
    def add_edge(self, G: nx.DiGraph, operator: Any, tab: Tableau) -> nx.DiGraph:
        op_tab: Tableau = operator(tab)
        G.add_edge(operator, op_tab, i="op1")
        return G

    def add_graph(self, crystal_graph: CrystalGraph, operator: Any) -> nx.DiGraph:
        G = crystal_graph.G.copy()
        for node in crystal_graph.G.nodes:
            G = self.add_edge(G=G, operator=operator, tab=node)
        return G
