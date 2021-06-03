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
    1. Its ease of implementation,
    2. Its compatability with both explicit and implicit time schemes,
    3. Its computational efficiency.

  \ 

  **Disadvantages of the Galerkin ROM include**
    1. A lack of robustness for non-symmetric systems
    2. A lack of robustness when equipped with hyperreduction techniques

  \

  Want to learn more about the Galerkin ROM and implement it in Pressio? See our `Python <https://pressio.github.io/pressio4py/html/md_pages_tutorials_tutorial3.html>`__ and `C++ <https://pressio.github.io/pressio-tutorials/html/md_pages_rom_tutorial2.html>`__ tutorials on the Galerkin ROM!

|

Overview of the least-squares Petrov--Galerkin ROM
==================================================
  Least-squares Petrov--Galerkin (LSPG) projection is a popular alternative to Galerkin projection. Unlike Galerkin projection, which relies on residual orthogonality, LSPG relies on residual minimization. Specifically, LSPG operates by sequentially computing solutions that minimize the time-discrete residual within a low-dimensional trial subspace at each time step. In general, LSPG projection yields more robust ROMs than Galerkin projection for nonsymmetric systems. Additionally, as LSPG is defined from residual minimization principles, aspects such as hyper-reduction and physical contraints can be more easily integrated into the ROM framework.

  **Advantages of the LSPG ROM include**
    1. Robustness for non-symmetric and nonlinear systems
    2. Robustness when eqipped with hyper-reduction techniques
    3. Its ability to be equipped with physical constraints

  \

  **Disadvantages of the LSPG ROM include**
    1. LSPG ROMs are inherently implicit, and are generally more computationally expensive than the Galerkin ROM.
    2. LSPG ROMs display a significant dependence on the time step. This dependence is difficult to quantify.
    3. LSPG ROMs are more diffusive than Galerkin ROMs.

  \

  Want to learn more about the LSPG ROM and implement it in Pressio? See our `Python <https://pressio.github.io/pressio4py/html/md_pages_demos_demo2.html>`__ and `C++ <https://pressio.github.io/pressio-tutorials/html/md_pages_swe_lspg.html>`__ tutorials using LSPG!


|

Overview of the windowed least-squares ROM
==========================================
  Windowed least-squares (WLS) is an extension of LSPG. Similar to LSPG, WLS operates by computing solutions that minimize the residual over *time windows* (each time window can comprise many time steps). WLS more robust than both LSPG and Galerkin ROMs, particularly when applied to non-symmetric systems.

  **Advantages of WLS include**
    1. WLS is equipped with the same advantages of LSPG with an increased robustness
    2. WLS decopules the residual minimization statement from the time step, and displays reduced sensitivity to the time step as compared to LSPG.

  \

  **Disadvantages of WLS include**
    1. In general, WLS is more expensive than both Galerkin and LSPG projection.
    2. WLS solutions are more diffusive than both Galerkin and LSPG.

  \

  Want to learn more about WLS? We are currently working on adding tutorials for WLS, but you can see our `reference publication <https://www.sciencedirect.com/science/article/pii/S0021999120307130>`__.

