Sample mesh and hyper-reduction
###############################

:breadcrumb: {filename}/algos.rst Algorithms
:summary: Algos
:authors: Eric Parish, Patrick Blonigan

.. role:: math-info(math)
    :class: m-default


The purpose of this page is to explain what hyper-reduction is, 
how it works, and what Pressio offers in this regard.
Since these concepts are not trivial, we tried our best to explain them 
clearly, but any feedback on how to improve them is welcome! 
Open an `issue on Github <https://github.com/Pressio/Pressio.github.io/issues>`_ 
to provide feedback.


A low-dimensional manifold is not (always) enough!
==================================================

The `key idea of pROMs <{filename}/overview/proms.rst>`_ is to 
approximate the full-order model (FOM) system with a low-dimensional one. 
However, when applied to systems that display non-polynomial nonlinearities 
in the state, or are non-affine in their parametric dependence, 
pROMs do not directly result in computational savings because the 
computational cost of evaluating the FOM velocity/residual operator (which ROMs 
need to manipulate) scales with the dimension of the full-order model. 
Hyper-reduction techniques aim to alleviate this issue. 

.. note-success:: 

    Hyper-reduction techniques are sampling-based methods that 
    try to approximate the FOM operators by querying 
    the full-order model for only a subset of elements of the velocity or residual vectors. 
    This, combined with the low-dimensional system approximation mentioned above, 
    enables ROMs to be computationally efficient.

.. This process enables ROMs whose cost does not scale with the dimensionality of the full-order model.

At the core of hyper-reduction implementations there are two main concepts: 

  1. **sample mesh**: a disjoint collection of nodes or elements at which the velocity (or residual) operator is computed. More details on how to select these nodes are discussed below.

  2. **stencil mesh**: the set of all nodes or elements needed to compute the velocity or residual on the sample mesh. 


The sample mesh serves two main purposes:

    1. Reduce the cost of computing the velocity or residual operators by only focusing on a given subset of nodes or elements.

    2. Minimize the memory footprint of storing the ROM basis and other ROM operators.

    These are both crucial to enable the ROM to be run on smaller, less powerful computers than the corresponding full order model.


A picture is worth a thousand words
===================================

The idea of sample and stencil mesh is better explained using figures.
Consider a 2D domain and let's assume you are using a 2nd-order finite-difference scheme 
to discretize the derivatives in your governing equations, using for example 
the `five-point stencil <https://en.wikipedia.org/wiki/Five-point_stencil>`__, 
as show in the left figure below. In this full-mesh scenario, 
you evaluate your operators at every cell in the domain, 
where any given cell needs the nearest-neighboring elements 
along each axis as shown in the left figure just below.

Now, assume that you are only interested in evaluating the operators at a subset of nodes.
(For the time being, assume that the choice of nodes is given, more details on this below).
The right figure below shows a sample and stencil mesh for an example selection of cells. 
The *sample mesh is color-coded cyan*, while the other unfilled cells 
complete the stencil mesh. It is clear that, for a given sample mesh, 
the stencil mesh is determined by the choice of stencil and numerical schemes.
Obviously, this is not restricted to a specific stencil size: if you need 
a larger or custom stencil, you end up with a difference stencil mesh.

.. figure:: {static}/img/2dsm.png
  :scale: 40 %


Here is another example for a three dimensional mesh:

.. figure:: {static}/img/3dsm.png
  :scale: 40 %

|

.. block-warning:: Key question

    How does one select the sample mesh nodes?


A number of techniques have been proposed to determine which elements/nodes should be included in the sample mesh. Some popular approaches include the empirical interpolation method (EIM), discrete empirical interpolation (DEIM), and Gauss-Newton with approximate tensors (GNAT); references for these methods are included below. This is an area of active research so more options are becoming available. 

.. note-success:: 

    The Pressio ecosystem offers such sampling techniques (some are already implemented 
    while some are not yet supported) in the `pressio-tools repository <https://github.com/Pressio/pressio-tools>`__.


How does Pressio support hyper-reduction?
==========================================

Hyperreduction is composed of two aspects. First, hyper-reduction places a burden on the application to only compute the velocity/residual on the sample mesh. As this burden is on the application, Pressio is unable to provide this functionality to a code. The second aspect of hyper-reduction is a modification to the underlying pROM problem. Pressio has support for this aspect of hyper-reduction, as it is application agnostic. Specifically, Pressio supports hyper-reduction in the following ways:

1. Pressio assumes the velocity/residual is returned at the sample nodes/elements
2. Pressio assumes that the basis is provided at the stencil nodes/elements
3. Pressio keeps track of the bookkeeping between the sample and stencil nodes/elements
4. Pressio modifies the projection process as required by the hyper-reduction method of interest.

**We emphasize that if the target application cannot return the residual/velocity at only the sample nodes/elements, Pressio will not be able to provide the code with real hyper-reduction.**

|


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

* Maxime Barrault, Yvon Maday, Ngoc Cuong Nguyen, Anthony T. Patera, 
  *An ‘empirical interpolation’ method: application to efficient reduced-basis discretization of partial differential equations*, Comptes Rendus Mathematique, Volume 339, Issue 9, 2004, Pages 667-672, ISSN 1631-073X, https://doi.org/10.1016/j.crma.2004.08.006.

* Saifon Chaturantabut and Danny C. Sorensen, 
  *Nonlinear Model Reduction via Discrete Empirical Interpolation*, SIAM Journal on Scientific Computing, Volume 32, Issue 5, Pages 2737-2764, https://doi.org/10.1137/090766498.

* Zlatko Drmač and Serkan Gugercin, 
  *A New Selection Operator for the Discrete Empirical Interpolation Method---Improved A Priori Error Bound and Extensions*, SIAM Journal on Scientific Computing, Volume 38, Issue 2, Pages A631-A648, https://doi.org/10.1137/15M1019271.

* Kevin Carlberg, Charbel Farhat, Julien Cortial, David Amsallem, 
  *The GNAT method for nonlinear model reduction: Effective implementation and application to computational fluid dynamics and turbulent flows*, Journal of Computational Physics, Volume 242, 2013, Pages 623-647, ISSN 0021-9991, https://doi.org/10.1016/j.jcp.2013.02.028.
