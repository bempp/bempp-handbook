---
title: Installation
---

### Requirements

Bempp-cl can be installed on any Windows, Mac, or Linux system with
Python 3.7. The following dependencies are required:

+ numpy
+ scipy
+ numba
+ pyopencl
+ meshio
+ plotly

#### OpenCL

Bempp-cl uses OpenCL kernels to launch computations.
[OpenCL](https://www.khronos.org/opencl/) is a standard for accessing
various types of compute devices, including CPUs and GPUs. Bempp-cl uses
OpenCL to compile C99 kernels during runtime for the underlying compute device.
This requires a runtime environment to be installed. Runtime environments are
available from Apple (CPU, GPU), Nvidia (GPU),
[AMD (GPU)](https://rocm.github.io/install.html), 
[Intel (CPU/GPU)](https://software.intel.com/en-us/articles/opencl-drivers) and
through the open-source [Pocl Project (CPU)](http://portablecl.org/). In the
following a few important remarks about OpenCL runtime environments.

+ Most GPU devices are much faster in single precision and we do not
  advise using Bempp in double precision on such devices.
+ If Pocl is used we require at least version 1.3. The package in the
  current Ubuntu 18.04 LTS release is older and does not yet support Bempp-cl.
+ The Apple CPU runtime environment is not compatible with Bempp-cl.

We provide quick installation instructions with Pocl, but also test regularly
with AMD and Nvidia runtime environments. This quick installation creates a
working installation based on the Pocl ICD (Installable Client Driver). For the
activation of other ICDs (e.g. from AMD or Nvidia) see further below.

### Quick-Installation

The quick installation gets you up and running on a CPU based system. It works
on Mac OS, Linux and the Windows Subsystem for Linux. The only requirement
is a working `conda` installation.

First, if not already done, enable the conda-forge channel.

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Next, create a new environment for Bempp and change into it.

```bash
conda create -n bempp python=3.7
conda activate bempp
```

We are using Python 3.7 by default, as there is currently still a bug
with Numba and Python 3.8 that effects Bempp-cl. On older versions of
`conda` it may be necessary to use `source activate` instead of
`conda activate`.

We can now install Bempp-cl with

```bash
conda install bempp-cl
```

This installs Bempp-cl with a minimal set of dependencies that are
required to run the software. However, we strongly recommend to also
install Gmsh, Matplotlib, and Jupyter. This can be done via

```bash
conda install gmsh matplotlib jupyter
```

### Using other compute devices
Any compute device that provides a valid ICD can
in principle be used with Bempp. However, if Bempp is installed within a conda
environment these may not be seen by the installation. The reason is that conda
expects files in different locations than may be provided by the system. The
following two solutions have been tested on Linux based systems.

#### Set the ICD location via environment variable

Typically, GPU vendors install ICDs in `/etc/OpenCL/vendors`. You can
set this as default search path for ICD files with the command
::

    export OPENCL_VENDOR_PATH=/etc/OpenCL/vendors

The drawback is that as long as this variable is set the Pocl driver
provided through conda is not visible any more.

#### Copy ICD files into the correct location

An alternative to setting an environment variable is to copy the system
ICD files into a location that conda knows.

First, find out where your conda environment is installed,
using e.g. the command `which python` when the environment is active.
The output of the command may be something like

```/home/user/miniconda3/envs/bempp/bin/python```

But this depends on whether Anaconda Python or Miniconda is installed and
where the base installation resides. The directory in which conda installs
ICDs is

```/home/user/miniconda3/envs/bempp/etc/OpenCL/vendors```

This directory already contains a file called `pocl.icd` which has been
installed through the `pocl` conda package. To use other ICD drivers
copy them over from the system directory `/etc/OpenCL/vendors`
into the above directory of your conda environment.
