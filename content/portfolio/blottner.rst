Blottner Sphere
###############

:summary: pROMs for Hypersonic Aerodynamics

One of our driving use cases for Pressio is for simulations of hypersonic
aerodynamics. Model reduction is necessary because computational models
are widely used in the hypersonic flight regime due to the expense and difficulty 
of flight tests and experiments. The reliance on computational models as well as
the risk tolerances in hypersonic applications requires a greater emphasis on 
trustworthiness of these models. Unfortunately, crucial tasks including 
parameter calibration, uncertainty/error propogation, and (robust) design
optimization require many model evalutations. 

Model reduction with Pressio enables these many query analysis for higher 
fidelity aerodynamic simulations such as finite volume models of the 
Navier-Stokes and Reynolds-Averaged Navier--Stokes (RANS) equations. 
This page presents some results obtained using Pressio and the Sandia
Aerodynamics and Reentry Code (SPARC) `[Howard et al. 2017][1] <https://arc.aiaa.org/doi/abs/10.2514/6.2017-4407>`_.

Description
===========

The Blottner Sphere is a commonly used verification case for hypersonic flow CFD codes `[Blottner 1990][2] <https://arc.aiaa.org/doi/abs/10.2514/3.26115>`_. 
The main feature is the bow shockwave that forms just upstream of the sphere, 
which can be difficult to capture accurately due to the shock strength and a numerical phenomena know as the carbuncle problem. 
Non-dimensional quantities characterizing the problem are the Mach number, Ma = 5.0, 
and the Reynolds Number, Re=1,887,500. 
Despite the large Reynolds number, this problem is run without a turbulence model, 
and the boundary layer is assumed to be laminar.
A schematic of the problem is shown below. 

.. figure:: {static}/img/blottner_sphere/blottner_schematic.png
    :scale: 70 %
    :alt: Blottner Sphere Schematic

    :math:`\rho_{\infty}, V_{\infty}, T_{\infty}` indicate freestream quantities. 

Full order model (FOM)
======================

We focus on the pseudo-transient behavior of the system from a uniform Mach 5.0 flow to steady state.
The pseudo time stepping is performed using the (implicit) backward Euler scheme with
fixed time step of :math:`2.5\times 10^{-6}` seconds, yielding 64 time instances.
During the pseudo-transient phase, the bow shock
upstream of the sphere moves and deforms until it reaches a steady state.
We use a spatial discretization using a structured mesh with 4,192,304 cells shown below.

.. figure:: {static}/img/blottner_sphere/fom_meshflow.png
    :scale: 50 %
    :alt: Blottner Sphere Mesh and steady-state solution.

.. Blottner sphere full model mesh.


LSPG ROM
========


Method
------

We use a Least-Squares Petrov--Galerkin (LSPG) ROM for a reconstructive case in which the ROM is run at the same inpute parameters, in this case flow conditions, as the FOM. The LSPG ROM is solved the same backward Euler time integration scheme and time step size as the FOM. 
The residual is minimized using a Gauss-Newton solver which terminates when the relative residual of the normal equations is reduced by three orders of magnitude. 
The ROM is run using a basis comprised of the leading 8 POD modes computed from all FOM snapshots. 
Further details on the ROM method can be found in `[Rizzi et al. 2020][3] <https://arxiv.org/abs/2003.07798>`_.

TODO Corresponding code functionalities, including solver, ROM, etc. 

Hyper-reduction is achieved using a sample mesh composed of 1,678 randomly selected cells 
in which the residual is sampled, along with neighboring cells and neighbors of neighbors, yielding 41,414 cells in total, 
equivalent to roughly 1% of the full mesh. 
It is shown below:

.. figure:: {static}/img/blottner_sphere/sample_mesh.png
    :scale: 30 %
    :alt: Blottner Sphere Sample Mesh

    Sample mesh used for the ROM.

Results
-------

Using this sample mesh resulted in a ROM with a **speed-up of 100**; that is, around 100 ROM could be run with the computational resources required for a single FOM.  
This substantial cost reduction comes with **almost no loss in accuracy**: a maximum state error of around than 0.5%, as well as errors of no more than 0.4% in wall heat flux and skin friction. The following pictures show the Mach number and wall heat flux computed using the FOM and ROM, respectively. ROM results are shown on the sample mesh, and reconstructed on the full mesh, respectively. 

.. figure:: {static}/img/blottner_sphere/Picture2.png
    :scale: 40 %
    :alt: Blottner Sphere Mesh and steady-state solution.

Additional results can be found in `[Rizzi et al. 2020][3] <https://arxiv.org/abs/2003.07798>`_.

.. block-success:: ROMs are low cost **and** accurate 
    
    .. note-success::

        A hyper-reduced ROM produces results within 1% of the full model results, but only requires around 1% of the computational resources needed for the full model. 

References
==========

- [1]: Micah Howard, Andrew Bradley, Steven W. Bova, James Overfelt, Ross Wagnild, Derek Dinzl, Mark Hoemmen and Alicia Klinvex. "Towards Performance Portability in a Compressible CFD Code," AIAA 2017-4407. 23rd AIAA Computational Fluid Dynamics Conference. June 2017.
- [2]: F. G. Blottner, "Accurate Navier-Stokes Results for the Hypersonic Flow over a Spherical Nosetip", Journal of Spacecraft, Vol. 27, No. 2, March-April 1990, DOI: 10.2514/3.26115
- [3]: F. Rizzi, P. Blonigan, and K. Carlberg. "PRESSIO: ENABLING PROJECTION-BASED MODEL REDUCTION FOR LARGE-SCALE NONLINEAR DYNAMICAL SYSTEMS", arXiv preprint, 2020, arXiv:2003.07798. 
