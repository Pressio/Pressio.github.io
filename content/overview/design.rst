Fundamental Design
##################

:breadcrumb: {filename}/overview.rst Overview
:summary: Design Idea

.. role:: math-info(math)
    :class: m-default

Scope of Pressio
=================
.. container::

	Pressio is applicable to any system expressible in a continuous-time form as 

	.. math::
	    :class: m-success

		\frac{d \boldsymbol{y}}{dt} =
		\boldsymbol{f}(\boldsymbol{y},t; \ldots),

  or in time-discrete form as

	.. math::
	    :class: m-success

		\boldsymbol R(\mathbf{y}, \mathbf{y}_{n-1} , \ldots, t_n, t_{n-1},\ldots) = \boldsymbol 0.

	In the time-continuous case, :math-info:`\boldsymbol{y}(t,\cdots) \in \mathbb{R}^N` denotes the state and 
	:math-info:`\boldsymbol{f}` denotes the velocity that may be linear or nonlinear in its first argument. In the time-discrete case, :math-info:`\mathbf{y} \in \mathbb{R}^N` denotes the state at the current time instance, :math-info:`\mathbf{y}_{n-i} \in \mathbb{R}^N` denotes the state at the ith previous time instance, and :math-info:`\boldsymbol R` denotes the time-discrete residual arrising, for example, from a linear mulstistep method. We note that the model form above is highly expressive, as it may be derived from the spatial discretization of a PDE problem or from naturall discrete systems (e.g., molecular-dynamics problems).


.. container:: 

  .. block-primary:: Design Idea

	  We leverage this simple, expressive mathematical framework
	  as a pivotal design choice to enable a minimal application
	  programming interface (API) that is natural to dynamical systems: you choose the formulation more convenient to you, and interface your application to Pressio by creating a corresponding adapter class to expose the operators needed for the chosen formulation. In general, you don't need to support both: there are advantages and disadvantages for both, and sometimes the choice is dictated directly by your native application (for example, in some cases it might be easier to directly expose the residual). A schematic depicting this design idea is given below. 

.. figure:: {static}/img/schem.svg
