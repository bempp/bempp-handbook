---
title: Sparse Boundary Operators
layout: handbook
---
Discretising the identity operator leads to a matrix $M=(m\_{ij})$, defined by
[[m\_{ij}=\int\_\Gamma\phi\_j\cdot\overline{\psi\_i},]]
where $\phi\_j$ and $\psi\_i$ are the basis functions of the domain and dual spaces respectively.
As this integral will only be non-zero when the basis functions overlap, the resulting
matrix will be sparse.

The identity operator can be created in Bempp using:
```python
ident = bempp.api.operators.boundary.sparse(domain, range_, dual)
```

A `SparseDiscreteBoundaryOperator` can be obtained using:
```python
mat = ident.weak_form()
```
This matrix is commonly called the mass matrix between the domain and dual spaces.

If desiried, a SciPy CSR matrix can be obtained from this discrete boundary operator with:
```python
mat.A
```
