---
title: The Bempp Handbook
---

Bempp is a platform for the assembly of boundary integral operators in Python.
It offers the following features:

+ Assembly of all the standard integral kernels for Laplace, Helmholtz,
  modified Helmholtz, and electromagnetic problems.
+ Support for AVX2 and AVX-512 Vectorisation on CPU platforms.
+ GPU assembly on Intel, AMD, and Nvidia GPU platforms.
+ A comprehensive operator algebra that makes it easy to formulate complex
  product operator formulations.
+ Import and export in a number of standard formats, including Gmsh and VTK.

There are two versions of Bempp available, a legacy version, which is
Bempp 3.3.4, and a new development version Bempp-cl 0.1.0.
The latter version is essentially feature complete for the dense assembly
of operators, provides advanced support for AVX2 and AVX-512 instruction sets,
and supports GPUs. The advantage of the legacy version is the mature H-Matrix
arithmetic that allows the solution of very large problems. Currently, Bempp-cl
only supports the dense assembly of operators and is therefore restricted to
problems in the dimension of a few ten thousand (or around 100,000 using a
specific dense evaluator mode on GPUs).
Support for large-scale problems is one of the main working areas for Bempp-cl.
This handbook focuses completely on Bempp-cl.

Contents
========
+ Grids
    + [Working with grids](grids.md)
+ Function spaces
    + [Function spaces](function_spaces.md)
