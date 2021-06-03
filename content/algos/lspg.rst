LSPG ROM
########

:breadcrumb: {filename}/algos.rst Algorithms
:summary: LSPG ROM
:authors: Eric Parish

.. role:: math-info(math)
    :class: m-default

.. container::

   Least-squares Petrov--Galerkin (LSPG) projection is a popular alternative to Galerkin projection. Unlike Galerkin projection, which relies on residual orthogonality, LSPG relies on residual minimization. In general, LSPG projection yields more robust ROMs than Galerkin projection for nonsymmetric systems. Additionally, as LSPG is defined from residual minimization principles, aspects such as hyper-reduction and physical contraints can be more easily integrated into the ROM framework.
   To formulate the problem, consider a dynamical system of the form

   .. math::
      :class: m-default

      \frac{d \boldsymbol{y}}{dt} =
      \boldsymbol{f}(\boldsymbol{y},t; \boldsymbol{\mu}),
      \quad \boldsymbol{y}(0;\boldsymbol{\mu}) = \boldsymbol{y}(\boldsymbol{\mu}),

   where :math-info:`\boldsymbol{y}: \mathbb{R}^N`,
   :math-info:`t` is time, and :math-info:`\mu` are parameters.
   We refer to this system as the full-order model (FOM).

   The key assumption is to approximate the FOM state, :math-info:`y`, as:

   .. math::
      :class: m-default

	      \boldsymbol{y} = g(\boldsymbol{\hat{y}})

   where :math-info:`\boldsymbol{\hat{y}}` is the reduced state (or generalized coordinates),
   and :math-info:`g(.)` represents a linear or nonlinear mapping.


.. container::

   LSPG projection corresponds to minimizing the (weighted)
   :math-info:`\ell^2`-norm of the *time-discrete* residual over the trial manifold.
   Hence, the starting point for this approach is the residual
   ODE formulation discretized in time with an arbitrary time-discretization method.

   LSPG projection is derived by substituting the approximate state
   in the time-discrete residual and minimizing its (weighted) @f$\ell^2@f$-norm,
   which yields a sequence of residual-minimization problems

   .. math::
      :class: m-success

	      \hat{x}^n(\mu)  =
	      \underset{\xi \in R^{p}}{arg min}
	      \left\|
	      A r^{n}\left(x_{ref}(\mu)+g(\xi);\mu)\right)
	      \right\|_2^2,\quad
	      n=1,\ldots,N_t

  todo( describe what kind of problems Galerkin is good for and those it is not good for)
  todo(put figure that shows how big the operators are)
