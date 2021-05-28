Supported ROM algorithms
##########################

:breadcrumb: {filename}/algos.rst Algorithms
:summary: Galerkin method

.. role:: math-info(math)
    :class: m-default

**Pressio supports the following ROMs:**
  1. Galerkin ROM
  2. Least-squares Petrov--Galerkin ROM 
  3. Direct windowed least-squares ROMs.

Overview of the Galerkin ROM
==============================
  The Galerkin ROM is one of the most widely used techniques in model reduction. **Galerkin projection is most appropriate for symmetric systems**, in which case the resulting ROM can be equipped with rigorous error bounds. For systems characterized by non-symmetric, nonlinear operators, Galerkin projection can yield inaccurate, or even unstable, dynamics. Nonetheless, Galerkin projection is widely used, and has been applied succesfully to numerous linear and nonlinear systems.

  **Advantages of the Galerkin ROM include** 
    1. Its ease of implementation, 
    2. Its compatability with both explicit and implicit time schemes,
    3. Its computational efficiency.



  **Disadvantages of the Galerkin ROM include** 
    1. A lack of robustness for non-symmetric systems
    2. A lack of robustness when equipped with hyperreduction techniques


Overview of the least-squares Petrov--Galerkin ROM
=====================================================
  Least-squares Petrov--Galerkin (LSPG) projection is a popular alternative to Galerkin projection. Unlike Galerkin projection, which relies on residual orthogonality, LSPG relies on residual minimization. Specifically, LSPG operates by sequentially computing solutions that minimize the time-discrete residual within a low-dimensional trial subspace at each time step. In general, LSPG projection yields more robust ROMs than Galerkin projection for nonsymmetric systems. Additionally, as LSPG is defined from residual minimization principles, aspects such as hyper-reduction and physical contraints can be more easily integrated into the ROM framework.  

  **Advantages of the LSPG ROM include** 
    1. Robustness for non-symmetric and nonlinear systems
    2. Robustness when eqipped with hyper-reduction techniques 
    3. Its ability to be equipped with physical constraints


  **Disadvantages of the LSPG ROM include** 
    1. LSPG ROMs are inherently implicit, and are generally more computationally expensive than the Galerkin ROM.
    2. LSPG ROMs display a significant dependence on the time step. This dependence is difficult to quantify.
    3. LSPG ROMs are more diffusive than Galerkin ROMs.


Overview of the windowed least-squares ROM 
=====================================================
  Windowed least-squares (WLS) is an extension of LSPG. Similar to LSPG, WLS operates by computing solutions that minimize the residual over *time windows* (each time window can comprise many time steps). WLS more robust than both LSPG and Galerkin ROMs, particularly when applied to non-symmetric systems. 

  **Advantages of WLS include**
    1. WLS is equipped with the same advantages of LSPG with an increased robustness
    2. WLS decopules the residual minimization statement from the time step, and displays reduced sensitivity to the time step as compared to LSPG.

  **Disadvantages of WLS include**
    1. In general, WLS is more expensive than both Galerkin and LSPG projection. 
    2. WLS solutions are more diffusive than both Galerkin and LSPG. 



