Hypersonic Aerodynamics
#######################

:breadcrumb: {filename}/hypaero.rst Hypersonic Aerodynamics
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
Navier-Stokes and Reynolds-Averaged Navier--Stokes (RANS) equations. The
following section contains results obtained using Pressio and the Sandia
Aerodynamics and Reentry Code (SPARC) [Howard et al. 2017][1]. 

Blottner Sphere
===============

The Blottner Sphere is a commonly used verification case for hypersonic flow CFD codes [Blottner 1990][2]. A schematic of the problem is
shown below. 

.. figure:: {static}/img/blottner_sphere/blottner_schematic.png
    :scale: 100 %
    :alt: Blottner Sphere Schematic

    Blottner sphere schematic. Infinity subscript indicates a freestream quantity. 


The main feature is the bow shockwave just
upstream of the sphere, which can be difficult to capture accurately due to the shock
strength and a numerical phenomena know as the carbuncle problem. 
Non-dimensional quantities characterizing the problem are the Mach number, Ma = 5.0, and the Reynolds Number, Re=1,887,500. Despite the large Reynolds number, this
problem is run without a turbulence model, and the boundary layer is
assumed to be laminar.

The full order model (FOM) is based on a spatial discretization using a structured mesh with 4,192,304 cells
shown below

.. figure:: {static}/img/blottner_sphere/mesh.png
    :scale: 40 %
    :alt: Blottner Sphere Mesh

    Blottner sphere full model mesh 

We focus on the pseudo-transient behavior of the system from a uniform Mach 5.0 flow to steady state.
The pseudo time stepping is performed using the (implicit) backward Euler scheme with
fixed time step of :math:`2.5\times 10^{-6}` seconds, yielding 64 time instances.
During the pseudo-transient phase, the bow shock
upstream of the sphere moves and deforms until it reaches a steady state.

The ROM results below are for a reconstructive case in which the ROM is run at the same inpute parameters, in this case flow conditions, as the FOM. The ROM is run using a basis comprised of the leading 8 POD modes computed from all FOM snapshots. The time integration scheme and step size were identical to that used for the FOM. Hyper-reduction is achieved using a sample mesh composed of 1,678 randomly selected cells 
in which the residual is sampled, along with neighboring
cells and neighbors of neighbors, yielding 41,414 cells in total,
equivalent to roughly 1% of the full mesh. It is shown below:

.. figure:: {static}/img/blottner_sphere/sample_mesh.png
    :scale: 40 %
    :alt: Blottner Sphere Sample Mesh

    Blottner sphere sample mesh

Using this sample mesh resulted in a maximum state error of around than 0.5%, as well as errors of no more than 0.4% in wall heat flux and skin friction. The following pictures show the Mach number and wall heat flux computed using the FOM and ROM, respectively. ROM results are shown on the sample mesh, and reconstructed on the full mesh, respectively. 

.. image-grid:: 

    {static}/img/blottner_sphere/mach-heat-3d-fom.png FOM solution
    {static}/img/blottner_sphere/mach-heat-3d-hrom.png ROM solution on the sample mesh
    {static}/img/blottner_sphere/mach-heat-3d-mrom.png ROM solution reconstructed on full mesh

HIFiRE-1
========

TODO


References
==========

- [1]: Micah Howard, Andrew Bradley, Steven W. Bova, James Overfelt, Ross Wagnild, Derek Dinzl, Mark Hoemmen and Alicia Klinvex. "Towards Performance Portability in a Compressible CFD Code," AIAA 2017-4407. 23rd AIAA Computational Fluid Dynamics Conference. June 2017.
- [2]: F. G. Blottner, "Accurate Navier-Stokes Results for the Hypersonic Flow over a Spherical Nosetip", Journal of Spacecraft, Vol. 27, No. 2, March-April 1990, DOI: 10.2514/3.26115

