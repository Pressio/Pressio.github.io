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

Here is another example for a three dimensional mesh:

.. figure:: {static}/img/3dsm.png

The sample mesh serves two purposes:

  1. Limit computations of the velocity of residual vectors to a given subset of nodes or elements.
  2. Minimize the memory needed to store the ROM basis and other ROM operators. 

These are both crucial for enabling the ROM to be run on smaller, less powerful computers than the corresponding full order model. 

A number of techniques have been proposed to determine which elements/nodes should be included in the sample mesh. Some popular approaches include the empirical interpolation method (EIM), discrete empirical interpolation (DEIM), and Gauss-Newton with approximate tensors (GNAT); references for these methods are included below. This is an area of active research so more options are becoming available. 

How does Pressio support hyper-reduction?
==========================================
Hyperreduction is composed of two aspects. First, hyper-reduction places a burden on the application to only compute the velocity/residual on the sample mesh. As this burden is on the application, Pressio is unable to provide this functionality to a code. The second aspect of hyper-reduction is a modification to the underlying pROM problem. Pressio has support for this aspect of hyper-reduction, as it is application agnostic. Specifically, Pressio supports hyper-reduction in the following ways:

  1. Pressio assumes the velocity/residual is returned at the sample nodes/elements
  2. Pressio assumes that the basis is provided at the stencil nodes/elements
  3. Pressio keeps track of the bookkeeping between the sample and stencil nodes/elements
  4. Pressio modifies the projection process as required by the hyper-reduction method of interest.

**We emphasize that if the target application cannot return the residual/velocity at only the sample nodes/elements, Pressio will not be able to provide the code with real hyper-reduction.**

Although Pressio itself does not contain any sampling methods, some of these are supported in the `pressio-tools repository <https://github.com/Pressio/pressio-tools>`__.

What type of hyper-reduction does Pressio support?
=====================================================
**Pressio supports**
  1. Collocation-based hyper-reduction
  2. Weighted hyper-reduction techniques such as Gappy POD, Discrete Empirical Interpolation, etc., via an abstract projection operator
  3. Masked hyper-reduction. Masked hyper-reduction mimics real hyper-reduction, but doesn't result in computational savings

For a quick-start guide on how to set up hyper-reduction in Pressio, see our syntax synopsis for C++ (needs to be added) and `Python <https://pressio.github.io/pressio4py/html/md_pages_synopsis_galerkin.html>`__, as well as our `C++ tutorial <https://pressio.github.io/pressio-tutorials/html/md_pages_swe_main.html>`__.

To learn more about hyper-reduction:
=====================================

A selection of papers on sampling techniques:

Maxime Barrault, Yvon Maday, Ngoc Cuong Nguyen, Anthony T. Patera, *An ‘empirical interpolation’ method: application to efficient reduced-basis discretization of partial differential equations*, Comptes Rendus Mathematique, Volume 339, Issue 9,
2004, Pages 667-672, ISSN 1631-073X, https://doi.org/10.1016/j.crma.2004.08.006.

Saifon Chaturantabut and Danny C. Sorensen, *Nonlinear Model Reduction via Discrete Empirical Interpolation*, SIAM Journal on Scientific Computing, Volume 32, Issue 5, Pages 2737-2764, https://doi.org/10.1137/090766498.

Zlatko Drmač and Serkan Gugercin, *A New Selection Operator for the Discrete Empirical Interpolation Method---Improved A Priori Error Bound and Extensions*, SIAM Journal on Scientific Computing, Volume 38, Issue 2, Pages A631-A648, https://doi.org/10.1137/15M1019271.

Kevin Carlberg, Charbel Farhat, Julien Cortial, David Amsallem, *The GNAT method for nonlinear model reduction: Effective implementation and application to computational fluid dynamics and turbulent flows*, Journal of Computational Physics, Volume 242, 2013, Pages 623-647, ISSN 0021-9991, https://doi.org/10.1016/j.jcp.2013.02.028.

