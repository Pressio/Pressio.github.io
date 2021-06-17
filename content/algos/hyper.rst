Supported hyper-reduction algorithms 
#######################################

:breadcrumb: {filename}/algos.rst Algorithms
:summary: Algos
:authors: Eric Parish, Patrick Blonigan

.. role:: math-info(math)
    :class: m-default



What is hyper-reduction
========================
When applied to systems that display non-polynomial nonlinearities in the state, or are non-affine in their parametric dependence, pROMs do not directly result in computational savings as evaluating the velocity/residual requires operations that scale with the dimension of the full-order model. Hyper-reduction techniques alleviate this issue. At their core, **hyper-reduction techniques are sampling-based methods that query the full-order model for only a subset of the velocity or residual vectors**. This process enables ROMs whose cost does not scale with the dimensionality of the full-order model. 

At the core of hyper-reduction implementations is the **sample mesh**, a disjoint collection of nodes or elements at which the velocity or residual vector are computed. The sample mesh is used in conjunction with what we refer to as the **stencil mesh**, which contains all nodes or elements needed to compute the velocity or residual vector on the sample mesh. For example, consider the case when the state in neighboring elements is needed to compute the residual or velocity contribution for a given element in the sample mesh. One sample and stencil mesh for a two dimensional rectangle is shown below. The sample mesh elements are dark blue and the corresponding stencil mesh is comprised of the light blue elements: 

.. figure:: {static}/img/sample_stencil_mesh.pdf

The sample mesh serves two purposes:

  1. Limit computations of the velocity of residual vectors to a given subset of nodes or elements.
  2. Minimize the memory needed to store the ROM basis and other ROM operators. 

These are both crucial for enabling the ROM to be run on smaller, less powerful computers than the corresponding full order model. 

How does Pressio support hyper-reduction?
==========================================
Hyperreduction is composed of two aspects. First, hyper-reduction places a burden on the application to only compute the velocity/residual on the sample mesh. As this burden is on the application, Pressio is unable to provide this functionality to a code. The second aspect of hyper-reduction is a modification to the underlying pROM problem. Pressio has support for this aspect of hyper-reduction, as it is application agnostic. Specifically, Pressio supports hyper-reduction in the following ways:

  1. Pressio assumes the velocity/residual is returned at the sample points
  2. Pressio assumes that the basis is provided at the stencil points
  3. Pressio keeps track of the bookkeeping between the sample and stencil points
  4. Pressio modifies the projection process as required by the hyper-reduction method of interest.

**We emphasize that if the target application cannot return the residual/velocity at only the sample points, Pressio will not be able to provide the code with real hyper-reduction.**

*In the above, the stencil points refer to the union of the sample points with all additional points that are required to compute the velocity/residual at the sample points*.

What type of hyper-reduction does Pressio support?
=====================================================
**Pressio supports**
  1. Collocation-based hyper-reduction
  2. Weighted hyper-reduction techniques such as Gappy POD, Discrete Empirical Interpolation, etc., via an abstract projection operator
  3. Masked hyper-reduction. Masked hyper-reduction mimics real hyper-reduction, but doesn't result in computational savings

For a quick-start guide on how to set up hyper-reduction in Pressio, see our syntax synopsis for C++ (needs to be added) and `Python <https://pressio.github.io/pressio4py/html/md_pages_synopsis_galerkin.html>`__, as well as our `C++ tutorial <https://pressio.github.io/pressio-tutorials/html/md_pages_swe_main.html>`__.


