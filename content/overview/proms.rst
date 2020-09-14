What are pROMs
###################

:breadcrumb: {filename}/overview.rst Overview
:summary: Intro to pROMs

.. container::

	Projection-based model reduction refers to a class of surrogate models
	that reduce the number of degrees
	of freedom in the full-order model (FOM) through a projection process.
	This projection step applied to the governing equations often enables one
	to make stronger performance guarantees
	(e.g., of structure preservation, of accuracy via adaptivity) than other
	surrogates like data-fits and perform more accurate *a posteriori*
	error analysis (e.g., via *a posteriori* error bounds or error models).

	Despite these benefits, the practical challenges of
	implementing model-reduction techniques in large-scale codes often
	precludes their adoption in practice; this occurs because standard implementations
	require modifying low-level operations and solvers for each simulation code of interest.
	This implementation strategy is not practical or sustainable
	in many modern settings, because industrial simulation codes often evolve rapidly,
	institutions may employ dozens of simulation codes for different analyses,
	and commercial codes typically do not expose the required low-level
	operators and solvers.

.. container:: m-row

	.. container::

		Projection-based model reduction can be broken into three main steps,
		namely data collection, basis creation, and ROM deployment.

		- data collection: \todo (all)

		- compute basis: \todo (all)

		- create/run the ROM: \todo (all)
