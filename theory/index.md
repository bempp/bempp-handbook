---
title: A Bempp User's Introduction to Boundary Element Methods
layout: handbook
children:
  - theory/function_spaces.md
  - theory/discrete_function_spaces.md
---

This section is still being written.

The Bempp data structures closely follow the underlying Mathematics.
The basis for each problem is a grid object, which defines the triangulation
of the underlying geometry. Using the grid object one defines a function
space that describes the approximations space. Grid functions describe
concrete objects within a function space, and operators describe mappings
between function spaces. In the following we have more in-depth descriptions
of each of these concepts.
