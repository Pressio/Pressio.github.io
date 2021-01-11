Galerkin ROM
###################

:breadcrumb: {filename}/algos.rst Algorithms
:summary: Galerkin method

.. role:: math-info(math)
    :class: m-default

.. container::

   The Galerkin ROM is one of the most important techniques  for model reduction.
   todo( put some references)

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

	      \boldsymbol{y} = \boldsymbol{\phi} \boldsymbol{\hat{y}}

   where :math-info:`\boldsymbol{\hat{y}}` is the reduced state (or generalized coordinates),
   and :math-info:`\boldsymbol{\phi}` represents a linear mapping.


.. container::

   Galerkin projection can be derived by
   minimizing the *time-continuous* residual over the trial manifold.
   The resulting model can be obtained by substituting the approximate state
   and the corresponding velocity :math-info:`f(\tilde{y})` into the time-continuous
   residual and minimizing its (weighted) :math-info:`\ell^2`-norm,
   which yields:

   .. math::
      :class: m-success

	      \dot{\hat{\mathbf{y}}}(t;\mathbf{\mu}) =
	      \Big( \mathbf{A} \mathbf{\phi} \Big)^+
	      \mathbf{A} \mathbf{f}
	      \Big(\mathbf{y}_{ref}(\mathbf{\mu})
	      + \mathbf{\phi}\hat{\mathbf{y}} \Big)


  where the superscript + denotes the Moore-Pentrose pseudoinverse
  and :math-info:`\hat{\mathbf{y}}(0;\mathbf{\mu})=\hat{\mathbf{y}}^0(\mathbf{\mu})`
  is the reduced initial condition. The matrix :math-info:`\mathbf{A} \in R^{z \times N}`
  with :math-info:`z \leq N` denotes a weighting matrix that can enable hyper-reduction.

  todo( describe what kind of problems Galerkin is good for and those it is not good for)
  todo(put figure that shows how big the operators are)

   ..
      a sequence of residual-minimization problems
      .. math:: :class: m-default
      \dot{\hat{\mathbf{y}}}(t; \mathbf{\mu})  =
      \underset{\mathbf{\xi} \in R^{p}}{arg min}
      \left\|
      \mathbf{A} \left( \mathbf{J}(\hat{\mathbf{y}}(t;\mathbf{\mu}))\mathbf{\xi}
      - \mathbf{f}\left(\mathbf{y}_{ref}(\mathbf{\mu})
      + \mathbf{\phi}\hat{\mathbf{y}}(t;\mathbf{\mu}
      \right) \right)
      \right\|_2^2
      which can be equivalently written as
