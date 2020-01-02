Working with grids
==================

This tutorial demonstrates basic features of dealing with grids in Bempp.
Simple grids can be easily created using built-in commands.
More complicated grids can be imported in the Gmsh format.

In order for the commands in this tutorial to work, Gmsh must be
installed and the command `gmsh` must be available in the path.

Creating basic grid objects
---------------------------

Let us create our first grid, a simple sphere. We first import bempp.
We will also import Numpy as it will be needed later.
::

    import bempp.api
    import numpy as np

The following command creates the sphere grid.
::

    grid = bempp.api.shapes.regular_sphere(3)


