LSPG ROM
###################

:breadcrumb: {filename}/algos.rst Algorithms
:summary: LSPG ROM

.. role:: math-info(math)
    :class: m-default

.. container::

   The LSPG ROM is ...
   todo( put some references)

   To formulate the problem, consider a dynamical system of the form

   .. math::
      :class: m-default

	 \frac{d \boldsymbol{x}}{dt} =
      \boldsymbol{f}(\boldsymbol{x},t; \boldsymbol{\mu}),
	 \quad \boldsymbol{x}(0;\boldsymbol{\mu}) = \boldsymbol{x}(\boldsymbol{\mu}),

   where :math-info:`\boldsymbol{x}: [0, T] \times {\cal D} \rightarrow  \mathbb{R}^N`

   \todo missing the approximation of the state


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
