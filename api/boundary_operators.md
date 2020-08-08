---
title: Boundary Operators
layout: handbook
children:
  - api/sparse_boundary_operators.md
  - api/laplace_boundary_operators.md
  - api/helmholtz_boundary_operators.md
  - api/modified_helmholtz_boundary_operators.md
  - api/maxwell_boundary_operators.md
  - api/operator_algebra.md
---

Boundary integral formulations of problems are commonly written using boundary integral operators.
In this section of the Bempp Handbook, we look at how these operators can be defined and
assembled using Bempp.

## Domains, ranges, and duals
When creating an operator in Bempp, three spaces are provided: the domain, the range, and the
dual to the range (given as inputs in that order). The domain and dual spaces are used to
calculate the weak form of the operator. The range is used by the
[operator algebra](operator_algebra.md) to correctly assemble product of operators.
