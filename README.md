# crystal_bases

## Example

### Young Tableau

```python
>>> from young.tableau import tableau
>>> tab = tableau([[1, 2, 3], [2]], orientaton='row')
>>> tab.box()
[[1, 2, 3], [2]]
```

#### jeu de taquin

```python
>>> from young.jeu_de_taquin import jeu_de_taquin
>>> from young.tableau import tableau

>>> tab = tableau(boxes=[[1, 1], [2, None]], orientation='row')
>>> jeu_de_taquin(tab).box()
[[None, 1], [1, 2]]
```

#### promotion operator

```python
>>> from young.pr import pr
>>> from young.tableau import tableau

>>> tab = tableau(boxes=[[1, 1], [2, 3]], orientation='row')
>>> pr(n = 3)(tab).box()
[[1, 2], [2, 3]]
```

## Crystal structure

### wt

```py
>>> from crystal.crystal_structure import wt
>>> from young.tableau import tableau

>>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
>>> wt(tab)
 [2, 2, 0]
```

### f

```py
>>> from crystal.crystal_structure import f
>>> from young.tableau import tableau

>>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
>>> f(i=1)(tab) # return None

>>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
>>> f(i=2)(tab).box()
[[1, 1], [2, 3]]
```

### e

```py
>>> from crystal.crystal_structure import e
>>> from young.tableau import tableau

>>> tab = tableau(boxes=[[1, 1], [2, 3]], orientation='row')
>>> e(i=1)(tab)

>>> tab = tableau(boxes=[[1, 1], [2, 3]], orientation='row')
>>> e(i=2)(tab).box()
 [[1, 1], [2, 2]]
```

### phi

```py
>>> from crystal.crystal_structure import phi
>>> from young.tableau import tableau

>>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
>>> phi(i=1)(tab)
0

>>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
>>> phi(i=2)(tab)
```

### epsilon

```py
>>> from crystal.crystal_structure import epsilon
>>> from young.tableau import tableau

>>> tab = tableau(boxes=[[1, 1], [2, 3]], orientation='row')
>>> epsilon(i=1)(tab)
0

>>> tab = tableau(boxes=[[1, 1], [2, 3]], orientation='row')
>>> epsilon(i=2)(tab)
1
```

## Crystal graph

```python
>>> from crystal.crystal_graph import crystal_graph
>>> from young.tableau import tableau
>>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
>>> B = crystal_graph(tab = tab, n = 3)
>>> list(B.G.nodes)
[Tableau(boxes=[[1, 1], [2, 2]], orientation='row'), Tableau(boxes=[[1, 1], [2, 3]], orientation='row'), Tableau(boxes=[[1, 2], [2, 3]], orientation='row'), Tableau(boxes=[[1, 2], [3, 3]], orientation='row'), Tableau(boxes=[[2, 2], [3, 3]], orientation='row'), Tableau(boxes=[[1, 1], [3, 3]], orientation='row')]

>>> B.view()

```

```python
>>> from crystal.add_crystal import add_crystal
>>> from crystal.crystal_graph import crystal_graph
>>> from young.tableau import tableau
>>> from young.pr import pr
>>> tab = tableau(boxes=[[1, 1], [2, 2]], orientation='row')
>>> B = crystal_graph(tab = tab, n = 3)
>>> G = add_graph(crystal_graph = B, operator = pr(n=3))
>>> list(G.nodes)
[Tableau(boxes=[[1, 1], [2, 2]], orientation='row'), Tableau(boxes=[[1, 1], [2, 3]], orientation='row'), Tableau(boxes=[[1, 2], [2, 3]], orientation='row'), Tableau(boxes=[[1, 2], [3, 3]], orientation='row'), Tableau(boxes=[[2, 2], [3, 3]], orientation='row'), Tableau(boxes=[[1, 1], [3, 3]], orientation='row')]
```
