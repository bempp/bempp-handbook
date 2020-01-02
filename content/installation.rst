************
Installation
************

Requirements
============

Bempp-cl can be installed on any Windows, Mac, or Linux system with
Python 3.7. The following dependencies are required:

- numpy
- scipy
- numba
- pyopencl
- meshio
- plotly

OpenCL
======

Bempp-cl uses OpenCL kernels to launch computations.
`OpenCL <https://www.khronos.org/opencl/>`_ is a standard for accessing
various types of compute devices, including CPUs and GPUs. Bempp-cl uses
OpenCL to compile C99 kernels during runtime for the underlying compute device.
This requires a runtime environment to be installed. Runtime environments are
available from Apple (CPU, GPU), Nvidia (GPU),
`AMD (GPU) <https://rocm.github.io/install.html`>_, 
`Intel (CPU/GPU) <https://software.intel.com/en-us/articles/opencl-drivers>`_ and
through the open-source `Pocl Project (CPU) <http://portablecl.org/>`_. In the
following a few important remarks about OpenCL runtime environments.

- Most GPU devices are much faster in single precision and we do not
  advise using Bempp in double precision on such devices.
- If Pocl is used we require at least version 1.3. The package in the
  current Ubuntu 18.04 LTS release is older and does not yet support Bempp-cl.
- The Apple CPU runtime environment is not compatible with Bempp-cl.

We provide quick installation instructions with Pocl, but also test regularly
with AMD and Nvidia runtime environments. This quick installation creates a
working installation based on the Pocl ICD (Installable Client Driver). For the
activation of other ICDs (e.g. from AMD or Nvidia) see further below.

Quick-Installation
==================

The quick installation gets you up and running on a CPU based system. It works
on Mac OS, Linux and the Windows Subsystem for Linux. The only Requirements
is a working `conda` installation.

First, if not already done, enable the conda-forge channel.

.. code-block:: shell

    conda config --add channels conda-forge
    conda config --set channel_priority strict

Next, create a new environment for Bempp and change into it.
::

    conda create -n bempp python=3.7
    conda activate bempp

We are using Python 3.7 by default, as there is currently still a bug
with Numba and Python 3.8 that effects Bempp-cl. On older versions of
`conda` it may be necessary to use `source activate` instead of
`conda activate`.

We can now install all necessary dependencies.
::

    conda install numpy, scipy, numba, pyopencl, plotly, meshio, pocl

It is also advisable to have the `Gmsh binary <https://gmsh.info>`_ somewhere
in the system path as it is used to discretise on the fly some of the example
shapes that come with the library. Gmsh can be installed directly from the
website on Windows and Mac systems or through the package manager on most
Linux distributions.

Finally, we can install Bempp-cl using `pip`.
::

    pip install Bempp-cl

Using other compute devices
===========================

Any compute device that provides a valid ICD can
in principle be used with Bempp. However, if Bempp is installed within a conda
environment these may not be seen by the installation. A simple workaround is
as follows. First, find out where your conda environment is installed,
using e.g. the command `which python` when the environment is active.
The output of the command may be something like
::

    /home/user/miniconda3/envs/bempp/bin/python

But this depends on whether Anaconda Python or Miniconda is installed and
where the base installation resides. The directory in which conda installs
ICDs is
::

    /home/user/miniconda3/envs/bempp/etc/OpenCL/vendors

This directory already contains a file called `pocl.icd` which has been
installed through the `pocl` conda package. To use other ICD drivers
copy them over from the system directory `/etc/OpenCL/vendors`
into the above directory of your conda environment.
