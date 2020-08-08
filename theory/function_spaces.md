---
title: Function Spaces
layout: handbook
children:
  - theory/sobolev_spaces.md
  - theory/discrete_function_spaces.md
---

### Local vs global dofs

A function space associates with each element i in the grid a local basis
of functions $S_i^{loc} := \{\Phi_{i, 1}^{loc}, \dots, \Phi_{i, n_i}^{loc}\}$,
where the support of each local basis function $\Phi_{i, j}^{loc}$ is
restricted to element i.

A global basis function is a weighted sum of all local
basis functions of the form

$$\Phi_{\ell} = \sum_{i}\sum_{j}\delta_{i, j}^{\ell}c_{i, j}\Phi_{i, j}^{loc}$$

The coefficients $c_{i, j}$ are the local multipliers and are
independent of the global basis functions. The
values $\delta_{i, j}^{\ell}$ take the value 1 if the local
basis function contributes to the global basis function or zero
otherwise.

Let's make an example. The usual finite element hat functions
are defined as continuous, elementwise linear functions such that

$$\Phi_{\ell}(p_k) = \begin{cases}0, & k = \ell\\
                                    1, &\text{otherwise}
                               \end{cases}.$$

Here, $p_k$ is the kth vertex in the grid. The local basis
functions $\Phi_{i, j}^{loc}$, $j=1, \dots, 3$ on element i
are defined as linear functions which are 1 on the jth vertex of the
element and 0 on the other two vertices.

The local multipliers $c_{i, j}$ are all 1, and the indices
$\delta_{i, j}^{\ell}$ are 1 for all local basis functions whose
nonzero vertex is identical to the global vertex $p_{\ell}$.
