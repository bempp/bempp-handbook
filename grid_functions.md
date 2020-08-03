---
title: Grid functions
layout: handbook
---

In Bempp, data on a given grid is represented as a grid function object.
A grid function2 consists of a set of basis function coefficients and a corresponding :ref:`function space<function-spaces>`.
In the following we will discuss the different ways of creating a grid function in Bempp.

### Initialising grid functions

#### Initialising with a Python callable
In many applications, such as acoustic scattering problems, we are given an analytic expression for boundary data.
For example, the following code defines a wave travelling with unit wavenumber along the $x$-axis in the positive direction.

```python
import bempp.api
import numpy as np

@bempp.api.complex_callable
def fun(x, normal, domain_index, result):
    result[0] = np.exp(1j * x[0])
```

A Python callable that you want to use to build a grid function should always have four inputs.
The first argument `x` is the coordinates of an evaluation point.
The second argument `normal` is the normal direction at the evaluation point.
The third one is the `domain_index`: this corresponds to the physical id in Gmsh and can be used to assign different boundary data to different parts of the grid.
The last argument `result` is the variable that stores the value of the callable.
It is a Numpy array with as many components as the basis functions of the underlying space have.

In order to discretise this callable, we need to define a suitable [space object](function-spaces.md).
Below we define a space of continuous, piecewise linear functions on a [spherical grid](grids.md).

```python
import bempp.api
grid = bempp.api.shapes.regular_sphere(5)
space = bempp.api.function_space(grid, "DP", 1)
```

The next command now discretises the Python callable by projecting it onto the space.

```python
grid_fun = bempp.api.GridFunction(space, fun=fun)
```

Before we describe in detail what is happening, we want to visualise the grid function.
This can be done with the following command.

``python
grid_fun.plot()
```

By default, the real part of function is plotted. There are more advanced functions to control this behaviour.

We now take a closer look at what happens in the initialisation of this GridFunction.
Denote the global basis functions of the space by $\psi_j$, for $j=1,\dots,N$.
The computation of the grid function consists of two steps:

+ Compute the projection coefficients
  $p_j=\int_{\Gamma}\overline{\psi_j(\mathbf{y})}f(\mathbf{y})\mathrm{d}\mathbf{y}$,
  where $f$ is the analytic function to be converted into a grid function and $\Gamma$
  is the surface defined by the grid.
+ Compute the basis coefficients $c_j$ from $Mc=p$, where $M$ is the mass matrix defined by
  $M_{ij}=\int_{\Gamma}\overline{\psi_i(\mathbf{y})}\psi_j(\mathbf{y})\mathrm{d}\mathbf{y}$.

This is an orthogonal $\mathcal{L}^2(\Gamma)$-projection onto the basis $\{\psi_1,...,\psi_N\}$.

#### Initialising with coefficients or projections
Instead of an analytic expression, we can initialise a grid function from a vector of
coefficients or a vector of projections.
This can be done as follows.

```python
c = np.array([...])  # These are the coefficients
grid_fun = GridFunction(space, coefficients=c)

p = np.array([...])  # These are the projections
grid_fun = GridFunction(space, projections=p, dual_space=dual)
```

The argument `dual_space` gives the space with which the projection coefficients were computed.
The parameter is optional and if it is not given then `space == dual_space` is assumed (i.e. $\mathcal{L}^2(\Gamma)$-projection).
