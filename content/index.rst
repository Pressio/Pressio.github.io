Pressio
#######

:save_as: index.html
:url:
:cover: {static}/img/top3.jpg
:description: Model reduction for dynamical systems.
:summary: Model reduction for ...
:hide_navbar_brand: True
:landing:
    .. container:: m-row

        .. container:: m-col-l-6 m-push-l-0 m-col-m-7 m-nopadb

            .. raw:: html

                <h1 style="text-transform:capitalize">Pressio</h1>


    .. container:: m-row

        .. container:: m-col-l-11 m-push-l-0

	  Simulating parameterized systems of equations is ubiquitous in science and engineering.
	  It is often the case that solving such systems with high level of accuracy is
	  a computationally intensive process.
	  For many-query analyses such as uncertainty quantification and optimization,
	  reduced models are required to make the analysis tractable.
	  Model reduction is a broad and active field.
	  Several techniques exist, but there is no such thing as "one method to rule them all".


        .. container:: m-col-l-7 m-push-l-1

                Pressio aims to advance model reduction for science and engineering,
		and our current focus is on mitigating the intrusive nature of `projection-based
		reduced-order models (pROMs) <{filename}/proms/description.rst>`_ for large-scale codes,
		and making this available to the community to foster research of new ideas
		and as well as more broad testing.
		The design of Pressio pivots on a `minimally intrusive interface <{filename}/interface/design.rst>`_
		with external applications.
		The core of the project is a header-only C++ library that leverages generic
		programming to support shared or distributed memory applications using
		arbitrary data-types and diverse programming models.

        .. container:: m-col-l-2 m-push-l-1 m-col-m-4 m-col-s-6 m-push-s-4 m-col-t-8 m-push-t-2

	   .. figure:: {static}/img/plogo.png


    .. container:: m-row

        .. container:: m-col-l-11 m-push-l-0

          **Our philosophy**
	     We believe in model reduction techniques that use data but
	     are grounded in physical laws.
	     Projection-based model reduction falls in this category due its basis in
	     mathematically derived projection processes and adherence of physical laws
	     This technique has shown large potential, but its main drawback is an intrusive nature.
	     This has been, historically, one of the key barriers (if not the main one)
	     precluding this technique to impact more broadly science and engineering.
	     As a consequence, this has also limited the range of
	     applications and the capabilities tested.
	     We believe this barrier can be broken, thus opening up large
	     opportunities to explore and mature this field.
	     This is especially true if this advancement is done by
	     leveraging ideas from other fields.
	     This is our "why" and motivates this project.


    .. container:: m-row

        .. container:: m-col-l-15 m-push-l-0

          **Features of the Pressio C++ library include:**
	    * A minimally-intrusive interface that can be useful for a variety of purposes
            * Numerous model reduction routines, including Galerkin, least-squares, and windowed least-squares projections
            * Support for arbitrary datatypes via generic programming and custom operations
            * Built-in support to use Eigen, Kokkos, and Trilinos (with more in progress)
	    * Several time integration schemes and nonlinear solvers

        .. container:: m-col-l-15 m-push-l-0

          **The Pressio ecosystem also offers:**
            * `pressio4py <https://pressio.github.io/pressio4py/html/index.html>`_: Python bindings enabling Pressio's C++ library to be used in pure-Python applications.
            * `pressio-tools <https://github.com/Pressio/pressio-tools>`_: A library to compute large-scale SVD, QR, and sample meshes.
            * `pressio-demoapps <https://github.com/Pressio/pressio-demoapps>`_: A suite of 1d, 2d, and 3d demo applications for testing ROMs and hyper-reduction.


    .. container:: m-row m-container-inflate

        .. container:: m-col-m-6 m-text-center

            .. block-primary:: Core C++ library

                Do you have a C++ application and want to know how to use *pressio* from C++?
                Follow this link to the userguide and documentation.

                .. button-primary:: https://pressio.github.io/pressio/html/index.html
                    :class: m-fullwidth

                    Documentation Website

                .. button-default:: https://pressio.github.io/pressio-tutorials/html/index.html
                    :class: m-fullwidth

                    Tutorials/Demos


        .. container:: m-col-m-6 m-text-center

            .. block-primary:: Python bindings library

                Do you have a Python application and would like to use Pressio
                *without* touching C++? We have Python bindings for that!

                .. button-primary:: https://pressio.github.io/pressio4py/html/index.html
                    :class: m-fullwidth

                    Documentation Website

                .. button-default:: https://pressio.github.io/pressio4py/html/md_pages_demos_demo1.html
                    :class: m-fullwidth

                    Tutorials/Demos


	..
	   .. container:: m-col-m-4 m-text-center

	       .. block-flat:: Skip directly to:

		   .. button-default:: https://pressio.github.io/pressio-tutorials/html/index.html
		       :class: m-fullwidth

		       c++ tutorials

		   .. button-default:: https://pressio.github.io/pressio4py/html/md_pages_demos_demo1.html
		       :class: m-fullwidth

		       pressio4py demos



..
   Pressio provides several functionalities and solvers for performing model reduction,
   such as Galerkin and least-squares Petrov–Galerkin projections.*
   <h5>(from the Latin *compressionem*: pressing together, squeezing)</h5>
