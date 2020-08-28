---
title: Inf-sup Stability
layout: handbook
---
$\mathcal{V}\_h=\operatorname{span}\\{\phi\_1,...,\phi\_n\\}$
and
$\mathcal{W}\_h=\operatorname{span}\\{\psi\_1,...,\psi\_n\\}$
be two finite dimensional spaces. We define the mass matrix
$M=(m\_{ij})$
between these two spaces by
[[m\_{ij}=\int\_\Gamma \psi\_j\cdot\phi\_i.]]

When forming products of operators, the inverse of this mass matrix will be used. It is therefore
important that the matrix is non-singular. It can be shown that the matrix will be non-singular
if the following inf-sup condition holds:

There exists an $h$-independent constant $c>0$ such that
[[\inf\_{\phi\in\mathcal{V}\_h}\sup\_{\psi\in\mathcal{W}\_h}\frac{\int\_\Gamma \psi\cdot\phi}
{\|\phi\|\|\psi\|}
\geqslant c.]]

This condition does not hold for the mass matrix between RWG and SNC spaces. It does however
hold between RWG and RBC, and between BC and SNC spaces. When solving Maxwell problems, care
must therefore be taken to ensure that all mass matrices involved are stably invertible.
