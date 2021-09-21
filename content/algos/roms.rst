Supported ROM algorithms
########################

:breadcrumb: {filename}/algos.rst Algorithms
:summary: Galerkin method
:authors: Eric Parish

.. role:: math-info(math)
    :class: m-default


**Pressio currently supports Galerkin projection, least-squares Petrov--Galerkin projection, and windowed least-squares projection model reduction schemes.** For a quick-start guide on how to use these ROMs in Pressio, see our syntax synopsis for C++ (needs to be added) and `Python <https://pressio.github.io/pressio4py/html/md_pages_synopsis_galerkin.html>`__.

|

Overview of the Galerkin ROM
============================

The Galerkin ROM is one of the most widely used techniques in model reduction. **Galerkin projection is most appropriate for symmetric systems**, in which case the resulting ROM can be equipped with rigorous error bounds. For systems characterized by non-symmetric, nonlinear operators, Galerkin projection can yield inaccurate, or even unstable, dynamics. Nonetheless, Galerkin projection is widely used, and has been applied successfully to numerous linear and nonlinear systems.


**Advantages of the Galerkin ROM include**
  1. Ease of implementation
  2. Compatability with both explicit and implicit time schemes
  3. Computational efficiency

\

**Disadvantages of the Galerkin ROM include**
  1. Lack of robustness for non-symmetric systems
  2. Lack of robustness when equipped with hyperreduction techniques

\

**Related tutorials and demos**
  1. `Galerkin ROM with explicit time stepping in C++ <https://pressio.github.io/pressio-tutorials/html/md_pages_rom_galerkin_default_explicit.html>`__
  2. `Galerkin ROM with implicit time stepping in C++ <https://pressio.github.io/pressio-tutorials/html/md_pages_rom_galerkin_default_implicit.html>`__
  3. `Galerkin ROM with explicit time stepping in pressio4py <https://pressio.github.io/pressio4py/html/md_pages_tutorials_tutorial3.html>`__
  4. `Galerkin ROM with masked collocation in pressio4py <https://pressio.github.io/pressio4py/html/md_pages_demos_demo4.html>`__

\

|

Overview of the least-squares Petrov--Galerkin ROM
==================================================

Least-squares Petrov--Galerkin (LSPG) projection is a popular alternative to Galerkin projection. Unlike Galerkin projection, which relies on residual orthogonality, LSPG relies on residual minimization. Specifically, LSPG operates by sequentially computing solutions that minimize the time-discrete residual within a low-dimensional trial subspace at each time step. In general, LSPG projection yields more robust ROMs than Galerkin projection for nonsymmetric systems. Additionally, as LSPG is defined from residual minimization principles, aspects such as hyper-reduction and physical contraints can be more easily integrated into the ROM framework.

**Advantages of the LSPG ROM include**
  1. Robustness for non-symmetric and nonlinear systems
  2. Robustness when eqipped with hyper-reduction techniques
  3. Ability to be equipped with physical constraints

\

**Disadvantages of the LSPG ROM include**
  1. Inherently implicit
  2. Generally more computationally expensive than the Galerkin ROM
  3. Display a significant dependence on the time step, with this dependence difficult to quantify
  4. More diffusive than Galerkin ROMs

\

**Related tutorials and demos**
  1. `LSPG ROM for the 1D advection diffusion equation in pressio4py <https://pressio.github.io/pressio4py/html/md_pages_demos_demo2.html>`_
  2. `LSPG ROM on a kernel PCA nonlinear manifold for the 1D advection diffusion equation in pressio4py <https://pressio.github.io/pressio4py/html/md_pages_demos_demo3.html>`__
  3. `LSPG ROM on a multilayer perceptron nonlinear manifold for the 1D advection diffusion in pressio4py <https://pressio.github.io/pressio4py/html/md_pages_demos_demo6.html>`__
  4. `Compare masked LSPG to masked Galerkin <https://pressio.github.io/pressio4py/html/md_pages_demos_demo5.html>`__

\

|

Overview of the windowed least-squares ROM
==========================================

Windowed least-squares (WLS) is an extension of LSPG. Similar to LSPG, WLS operates by computing solutions that minimize the residual over *time windows* (each time window can comprise many time steps). WLS more robust than both LSPG and Galerkin ROMs, particularly when applied to non-symmetric systems.

**Advantages of WLS include**
  1. Equipped with the same advantages of LSPG with an increased robustness
  2. Decopules the residual minimization statement from the time step, and displays reduced sensitivity to the time step as compared to LSPG.

\

**Disadvantages of WLS include**
  1. In general, more expensive than both Galerkin and LSPG projection.
  2. More diffusive than both Galerkin and LSPG.

\

Want to learn more about WLS? We are currently working on adding tutorials for WLS, but you can see our `reference publication <https://www.sciencedirect.com/science/article/pii/S0021999120307130>`__.
