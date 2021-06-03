Supported hyper-reduction algorithms 
#######################################

:breadcrumb: {filename}/algos.rst Algorithms
:summary: Algos
:authors: Eric Parish

.. role:: math-info(math)
    :class: m-default



What is hyper-reduction
========================
When applied to systems that display non-polynomial nonlinearities in the state, or are non-affine in their parametric dependence, pROMs don't directly result in computational savings as evaluating the velocity/residual requires operations that scale with the dimension of the full-order model. Hyper-reduction techniques alleviate this issue. At their core, **hyper-reduction techniques are sampling-based methods that query the full-order model for only a subset of the velocity or residual**. This process enables ROMs that do not scale with the dimensionality of the full-order model. 



How does Pressio support hyper-reduction?
==========================================
Hyper-reduction requires modifications to the full-order model (e.g., telling it where to sample the residual), and is thus an intrusive process. Pressio supports hyper-reduction in the following ways:
  1. Pressio assumes the velocity is returned at the sample points
  2. Pressio assumes that the basis is provided at the stencil points
  3. Pressio keeps track of the bookkeeping between the sample and stencil points

We emphasize that if the target application cannot return the residual/velocity at only the sample points, Pressio will not be able to provide the code with real hyper-reduction.

*In the above, the stencil points refer to the union of the sample points with all additional points that are required to compute the velocity/residual at the sample points*.

What type of hyper-reduction does Pressio support?
=====================================================
**Pressio supports**
  1. Collocation-based hyper-reduction
  2. Weighted hyper-reduction techniques such as Gappy POD, Discrete Empirical Interpolation, etc., via an abstract projection operator
  3. Masked hyper-reduction. Masked hyper-reduction mimics real hyper-reduction, but doesn't result in computational savings

For a quick-start guide on how to set up hyper-reduction in Pressio, see our syntax synopsis for C++ (needs to be added) and `Python <https://pressio.github.io/pressio4py/html/md_pages_synopsis_galerkin.html>`__, as well as our `C++ tutorial <https://pressio.github.io/pressio-tutorials/html/md_pages_swe_main.html>`__.


