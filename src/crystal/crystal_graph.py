from dataclasses import dataclass, field
from typing import Union, List
import src.young.tableau as tableau
from crystal_structure import f, e, phi, epsilon
import matplotlib.pyplot as plt
import networkx as nx


@dataclass(frozen=True)
class CrystalGraph:
    G: nx.DiGraph = field(init=False, repr=True, compare=False, default=nx.DiGraph())
    tab: tableau.Tableau = field(init=True, repr=True, compare=False)
    n: int = field(init=True, repr=True, compare=False)

    def __eq__(self, other):
        edge_match = nx.algorithms.isomorphism.numerical_edge_match("i", 1)
        return nx.is_isomorphic(G1=self.G, G2=other.G, edge_match=edge_match)

    def __post_init__(self):
        self.create_graph(tab=self.tab, n=self.n)
        self._set_node_position()

    def _lower_graph(self, tab: tableau.Tableau, n: int) -> None:
        self.G.add_node(tab)
        for i in range(1, n):
            if phi(i)(tab) > 0:
                T = f(i)(tab)
                self.G.add_edge(tab, T, i=i)
                self._lower_graph(T, n)

    def _raiging_graph(self, tab: tableau.Tableau, n: int) -> None:
        self.G.add_node(tab)
        for i in range(1, n):
            if epsilon(i)(tab) > 0:
                T = e(i)(tab)
                self.G.add_edge(T, tab, i=i)
                self._raiging_graph(T, n)

    def create_graph(self, tab: tableau.Tableau, n: int) -> None:
        self._lower_graph(tab=tab, n=n)
        self._raiging_graph(tab=tab, n=n)

    def _set_node_position(self) -> None:
        pos = nx.spring_layout(self.G, k=0.3, seed=1)
        for node in self.G.nodes():
            self.G.nodes[node]["pos"] = pos[node]

    def _get_subgraph_by_attribute(self, attribute, val) -> nx.DiGraph:
        subgraph = self.G.edge_subgraph(
            [
                (start, end)
                for start, end, data in self.G.edges(data=True)
                if data[attribute] == val
            ]
        )
        return subgraph

    def view(self) -> List[Union[plt.Figure, plt.axis]]:
        fig, ax = plt.subplots(figsize=(16, 9))

        edge_label_colors = ["#566978", "#FF5F5A", "#41C773", "#FFC87C", "#06C2B9"]

        for i in range(1, self.n):
            subgraph = self._get_subgraph_by_attribute(attribute="i", val=i)
            nx.draw_networkx_edge_labels(
                subgraph,
                pos=nx.get_node_attributes(subgraph, "pos"),
                edge_labels=nx.get_edge_attributes(subgraph, "i"),
                font_size=30,
                font_color=edge_label_colors[len(edge_label_colors) - i],
                font_weight="bold",
                alpha=0.8,
                ax=ax,
            )

        nx.draw(
            self.G,
            pos=nx.get_node_attributes(self.G, "pos"),
            edge_color="#566978",
            node_color="#06C2B9",
            node_size=500,
            width=3,
            alpha=0.7,
            ax=ax,
        )

        ax.set_title(
            rf"n = {self.n}, shape = {self.tab.shape()}, weight = {self.tab.weight()}",
            fontdict=dict(
                size=25,
                color="#566978",
                weight="bold",
            ),
        )

        return [fig, ax]


def crystal_graph(tab: tableau.Tableau, n: int) -> CrystalGraph:
    """crystal graph

    Args:
        tab: tableau.Tableau

    Returns:
        CrystalGraph:

    Examples:
        >>> tab = tableau.tableau(boxes=[[1, 1], [2, 2]], orientation='row')
        >>> crystal_graph(tab = tab, n = 3) == crystal_graph(tab = tab, n = 3)
        True
    """
    return CrystalGraph(tab=tab, n=n)
