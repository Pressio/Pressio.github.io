Fundamental Design
##################

:breadcrumb: {filename}/overview.rst Overview
:summary: Design Idea

.. role:: math-info(math)
    :class: m-default

.. container::

	Pressio is applicable to any system expressible as:

	.. math::
	    :class: m-success

		\frac{d \boldsymbol{y}}{dt} =
		\boldsymbol{f}(\boldsymbol{y},t; \boldsymbol{\mu}),
		\quad \boldsymbol{y}(0;\boldsymbol{\mu}) = \boldsymbol{y}(\boldsymbol{\mu}),

	where :math-info:`\boldsymbol{y}` denotes the state, :math-info:`\boldsymbol{y}^0`
	denotes the initial state, :math-info:`\boldsymbol{\mu} \in {\cal D}
	\subseteq \mathbb{R}^{n_{\mu}}` denotes the system parameters,
	:math-info:`\boldsymbol{f}` denotes the velocity that may be linear or nonlinear
        in its first argument,
	and :math-info:`t\in[0,T]` denotes time with :math-info:`T>0` denoting the final time.
	We note that the model form above is highly expressive, as it may be derived
	from the spatial discretization of a PDE problem or from naturally
	discrete systems (e.g., molecular-dynamics problems).


.. block-primary:: Design Idea

	We leverage this simple, expressive mathematical framework
	as a pivotal design choice to enable a minimal application
	programming interface (API) that is natural to dynamical systems.


.. figure:: {static}/img/schem.svg
