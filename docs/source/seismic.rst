Seismic Shear Waves
===================

This work focuses on projection-based reduced-order models (ROMs) of linear time-invariant (LTI) dynamical systems. 
For such systems, current practice relies on ROM formulations expressing the state as a rank-1 tensor (i.e., a vector), 
leading to computational kernels that are memory bandwidth bound and, therefore, ill-suited for scalable performance on modern architectures. This weakness can be particularly limiting when tackling many-query studies, where one needs to run a large number of simulations. 
This work introduces a reformulation, called rank-2 Galerkin, of the Galerkin ROM for LTI dynamical systems which converts the nature of the ROM problem from memory bandwidth to compute bound. We present the details of the formulation and its implementation, and demonstrate its utility through numerical experiments using, as a test case, the simulation of elastic seismic shear waves in an axisymmetric domain. We quantify and analyze performance and scaling results for varying numbers of threads and problem sizes. Finally, we present an end-to-end demonstration of using the rank-2 Galerkin ROM for a Monte Carlo sampling study. We show that the rank-2 Galerkin ROM is one order of magnitude more efficient than the rank-1 Galerkin ROM (the current practice) and about 970 times more efficient than the full-order model, while maintaining accuracy in both the mean and statistics of the field.

The code for shear wave simulation code developed for this work is `available here <https://github.com/Pressio/SHAW>`__.

References
----------

- F. Rizzi, E.J.Parish, P.J.Blonigan, J.Tencer, A compute-bound formulation of Galerkin model reduction for linear time-invariant dynamical systems, CMAME, Volume 384, 1 October 2021
