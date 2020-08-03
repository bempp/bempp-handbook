---
title: Working with grids
---

This tutorial demonstrates basic features of dealing with grids in Bempp.
Simple grids can be easily created using built-in commands.
More complicated grids can be imported in the Gmsh format.

In order for the commands in this tutorial to work, Gmsh must be
installed and the command `gmsh` must be available in the path.

Bempp currently only supports grid consisting of flat surface triangles.

### Creating basic grid objects

We first import Bempp.
We will also import Numpy as it will be needed later.

```python
import bempp.api
import numpy as np
```

#### Built-in grids
The following command creates the sphere grid.

```python
grid = bempp.api.shapes.regular_sphere(3)
```

The command `regular_sphere` creates a sphere by refining a
base octahedron. The number of elements in the sphere is given by
$8 * 4^n$, where $n$ is the refinement level.

Another option is to generate a sphere based on a given
element diameter. For example, we can create a unit sphere
with element diameter $h=0.1$ with the command:

```python
grid = bempp.api.shapes.sphere(h=0.1)
```

Full documentation of Bempp's available built-in grids can be found
[here](https://bempp-cl.readthedocs.io/en/latest/docs/bempp/api/shapes/index.html).

#### Importing a grid
To import an existing grid file Bempp provides an `import_grid` command, e.g.

```python
grid = bempp.api.import_grid('my_grid.msh')
```

to import a grid in Gmsh format. Bempp uses the file ending to recognize
a number of grid formats. This works through the external `meshio` library.
The `meshio <https://github.com/nschloe/meshio>`_ website contains details
on supported formats. Frequently used formats with Bempp are `msh` (Gmsh),
`vtk` (Legacy VTK), and `vtu` (VTK Xml Format).

Grids can also be generated from arrays containing vertex coordinates and
connectivity information. For example, to create a grid consisting of two
triangles with vertices $\{(0, 0, 0), (1, 0, 0), (0, 1, 0)\}$ and
$\{(1, 0, 0), (1, 1, 0), (0, 1, 0)\}$ we use the following commands.

```python
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [0, 1, 0],
                     [1, 1, 0]],
                    dtype=np.float64).T
elements = np.array([[0, 1, 2],
                     [1, 3, 2]],
                     dtype=np.uint32).T
grid = bempp.api.Grid(vertices, elements)
```

Note that we have specified the arrays to be transposed. The grid objects
expects the vertices array to be 3&times;$M$, where $M$ is the number
of vertices, and the elements array to be 3&times;$N$, where $N$ is
the number of elements.

The array `vertices` contains the 3D coordinates of all vertices. The array
`elements` contains the connectivity information. In this case the first
triangle consists of the vertices 0, 1, 2, and the second triangle consists
of the vertices 1, 3, 2. Optionally, we can specify a list `domain_indices`
that gives different groups of elements the same id. This can be used
for example to generate different types of boundary data on different parts
of the grid, or to specify function spaces only on parts of the grid. In this
example, both triangles automatically have the identifier 0 since nothing
else was specified. This corresponds to the call

```python
grid = bempp.api.Grid(vertices, elements, domain_indices=[0, 0])
```

### Querying grid information

One can directly query a number of quantities about grids. In the following
we demonstrate some of them.

The number of elements, edges and vertices are given by

```python
grid.number_of_elements
grid.number_of_edges
grid.number_of_vertices
```

To query the maximum and minimum element diameter use the following attributes.

```python
grid.maximum_element_diameter
grid.minimum_element_diameter
```

The vertex indices of the 5th element can be obtained through

```python
grid.elements[:, 5]
```

Hence, to display the vertex coordinates of the 5th element use

```python
grid.vertices[:, grid.elements[:, 5]]
```

The area of the 5th element is shown as

```python
grid.volumes[5]
```

The edge indices associated with the 5th element are given as

```python
grid.element_edges[5]
```

and we can see the definition of the edges in terms of vertex
indices as

```python
grid.edges[:, grid.element_edges[:, 5]]
```

This returns a 2&times;3 array of the vertex coordinates associated
with the three edges of the element. Edges in Bempp are counted such
that the zeroth edge is the one connecting vertex 0 and 1. The first edge
connects vertex 2 and 0, and the third edge connects vertex 1 and 2.

A number of other properties are defined, which are explained in more detail
in the object description for the Grid class.

### Plotting and exporting grids

To export a grid use the `export` command.

```python
bempp.api.export('grid.msh', grid=grid)
```

This commands export the object `grid` as Gmsh file with the
name `grid.msh`.

In order to plot a grid we can simply use the command

```python
grid.plot()
```

By default, this will plot using gmsh (or TODO if you are inside a Jupyter notebook).
The following command can be used to change the plotting backend.

```python
bempp.api.PLOT_BACKEND = 'gmsh'
bempp.api.PLOT_BACKEND = 'paraview'
```

This requires Gmsh or Paraview to be available in the system path.
