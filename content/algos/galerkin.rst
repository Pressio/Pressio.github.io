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

	 \frac{d \boldsymbol{x}}{dt} =
      \boldsymbol{f}(\boldsymbol{x},t; \boldsymbol{\mu}),
	 \quad \boldsymbol{x}(0;\boldsymbol{\mu}) = \boldsymbol{x}(\boldsymbol{\mu}),

   where :math-info:`\boldsymbol{x}: [0, T] \times {\cal D} \rightarrow  \mathbb{R}^N`

   \todo missing the approximation of the state


.. container::

   Galerkin projection can be derived by
   minimizing the *time-continuous* residual over the trial manifold.
   The resulting model can be obtained by substituting the approximate state
   and the corresponding velocity :math-info:`f(\tilde{x})` into the time-continuous
   residual and minimizing its (weighted) :math-info:`\ell^2`-norm,
   which yields a sequence of residual-minimization problems

   .. math::
      :class: m-default

	     \dot{\hat{\mathbf{x}}}(t; \mathbf{\mu})  =
	     \underset{\mathbf{\xi} \in R^{p}}{arg min}
	     \left\|
	     \mathbf{A} \left( \mathbf{J}(\hat{\mathbf{x}}(t;\mathbf{\mu}))\mathbf{\xi}
	     - \mathbf{f}\left(\mathbf{x}_{ref}(\mathbf{\mu})
	       + \mathbf{g}(\hat{\mathbf{x}}(t;\mathbf{\mu});\mathbf{\mu}
		 \right) \right)
		 \right\|_2^2


   which can be equivalently written as

   .. math::
      :class: m-success

	      \dot{\hat{\mathbf{x}}}(t;\mathbf{\mu}) =
	      \Big( \mathbf{A} \mathbf{J}(\hat{\mathbf{x}}(t;\mathbf{\mu}) \Big)^+
	      \mathbf{A} \mathbf{f}
	      \Big(\mathbf{x}_{ref}(\mathbf{\mu})
	      + \mathbf{g}(\hat{\mathbf{x}}(t;\mathbf{\mu}); \mathbf{\mu} \Big)


  where the superscript + denotes the Moore-Pentrose pseudoinverse
  and :math-info:`\hat{\mathbf{x}}(0;\mathbf{\mu})=\hat{\mathbf{x}}^0(\mathbf{\mu})`
  is the reduced initial condition. The matrix :math-info:`\mathbf{A} \in R^{z \times N}`
  with :math-info:`z \leq N` denotes a weighting matrix that can enable hyper-reduction.

  todo( describe what kind of problems Galerkin is good for and those it is not good for)
  todo(put figure that shows how big the operators are)
