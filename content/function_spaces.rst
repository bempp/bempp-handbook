***************
Function Spaces
***************

Function spaces form a central part of Bempp. They store information about
bases on elements and the mappings of local to global degrees of
freedom (dofs).

Local vs global dofs
====================

A function space associates with each element i in the grid a local basis
of functions :math:`S_i^{loc} := \{\Phi_{i, 1}^{loc}, \dots, \Phi_{i, n_i}^{loc}\}`,
where the support of each local basis function :math:`\Phi_{i, j}^{loc}` is
restricted to element i.

A global basis function is a weighted sum of all local
basis functions of the form

.. math::

   \Phi_{\ell} = \sum_{i}\sum_{j}\delta_{i, j}^{\ell}c_{i, j}\Phi_{i, j}^{loc}

The coefficients :math:`c_{i, j}` are the local multipliers and are
independent of the global basis functions. The
values :math:`\delta_{i, j}^{\ell}` take the value 1 if the local
basis function contributes to the global basis function or zero
otherwise.

Let's make an example. The usual finite element hat functions
are defined as continuous, elementwise linear functions such that

.. math::

    \Phi_{\ell}(p_k) = \begin{cases}0, & k = \ell\\
                                    1, &\text{otherwise}
                               \end{cases}.

Here, :math:`p_k` is the kth vertex in the grid. The local basis
functions :math:`\Phi_{i, j}^{loc}`, :math:`j=1, \dots, 3` on element i
are defined as linear functions which are 1 on the jth vertex of the
element and 0 on the other two vertices.

The local multipliers :math:`c_{i, j}` are all 1, and the indices
:math:`\delta_{i, j}^{\ell}` are 1 for all local basis functions whose
nonzero vertex is identical to the global vertex :math:`p_{\ell}`.

Defining a function space
=========================

To define a function space we require a grid object. We can then use
the `function_space` method to intitialise a new space. To define
a space of piecewise constant functions we use the command
::

    spce = bempp.api.function_space(grid, "DP", 0)

The parameter `DP` is short for Discontinuous Polynomial. The number 0 is
the degree of the polynomial space. To define a space of continuous, piecewise
linear functions use
::

    space = bempp.api.function_space(grid, "P", 1)

Bempp-cl only supports function spaces up to degree 1. This is an important
difference to earlier versions that also supported higher order spaces.

