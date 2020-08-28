---
title: Interpolation and Projection
layout: handbook
---

We now take a closer look at what happens in the initialisation of this GridFunction.
Denote the global basis functions of the space by $\psi\_j$, for $j=1,\dots,N$.
The computation of the grid function consists of two steps:

+ Compute the projection coefficients
  $p\_j=\int\_{\Gamma}\overline{\psi\_j(\mathbf{y})}f(\mathbf{y})\mathrm{d}\mathbf{y}$,
  where $f$ is the analytic function to be converted into a grid function and $\Gamma$
  is the surface defined by the grid.
+ Compute the basis coefficients $c\_j$ from $Mc=p$, where $M$ is the mass matrix defined by
  $M\_{ij}=\int\_{\Gamma}\overline{\psi\_i(\mathbf{y})}\psi\_j(\mathbf{y})\mathrm{d}\mathbf{y}$.

This is an orthogonal $\mathcal{L}^2(\Gamma)$-projection onto the basis $\{\psi\_1,...,\psi\_N\}$.
