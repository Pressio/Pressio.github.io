Pressio
#######

:save_as: index.html
:url:
:cover: {static}/img/top1.jpg
:description: Projection-based model reduction for dynamical systems.
:summary: Model reduction for ...
:hide_navbar_brand: True
:landing:
    .. container:: m-row

        .. container:: m-col-l-6 m-push-l-0 m-col-m-7 m-nopadb

            .. raw:: html

                <h1 style="text-transform:capitalize">Pressio</h1>


    .. container:: m-row

        .. container:: m-col-l-9 m-push-l-0

                *Pressio is an open-source project aimed at alleviating the intrusive nature of* `projection-based reduced-order models (pROMs) <{filename}/overview/proms.rst>`_ *for large-scale codes. The core of the Pressio project is a header-only C++ library that leverages generic programming to interface with shared or distributed memory applications using arbitrary data-types and diverse programming models. Pressio provides several functionalities and solvers for performing model reduction, such as Galerkin and least-squares Petrov–Galerkin projections.*

		The name comes from the Latin *compressionem*: pressing together, squeezing.

        .. container:: m-col-l-2 m-push-l-1 m-col-m-4 m-col-s-6 m-push-s-3 m-col-t-8 m-push-t-2

	   .. figure:: {static}/img/plogo.png


    .. container:: m-row

        .. container:: m-col-l-15 m-push-l-0

          **Features of the Pressio C++ library include:**
            * Numerous model reduction routines, including Galerkin, least-squares, and windowed least-squares projections
            * Support for arbitrary datatypes via generic programming and custom operations
            * Built-in support to use Eigen, Kokkos, and Trilinos (with more in progress)
	    * Several time integration schemes

        .. container:: m-col-l-15 m-push-l-0

          **The Pressio ecosystem also offers:**
            * `pressio4py <https://pypi.org/project/pressio4py/>`_: Python bindings enabling Pressio's C++ library to be used in pure-Python applications.
            * `pressio-tools <https://github.com/Pressio/pressio-tools>`_: A library to compute large-scale SVD, QR, and sample meshes.
            * `pressio-demoapps <https://github.com/Pressio/pressio-demoapps>`_: A suite of 1d, 2d, and 3d demo applications for testing pROMs and hyper-reduction.


    .. container:: m-row m-container-inflate

        .. container:: m-col-m-4 m-text-center

            .. block-primary:: Core C++ library

                Do you have a C++ application and want to know how to use *pressio* from C++?
                Follow this link to the userguide and documentation.

                .. button-primary:: https://pressio.github.io/pressio/html/index.html
                    :class: m-fullwidth

                    Take me there


        .. container:: m-col-m-4 m-text-center

            .. block-primary:: Python bindings library

                Do you have a Python application and would like to use Pressio
                *without* touching C++? We have Python bindings for that!

                .. button-primary:: https://pressio.github.io/pressio4py/html/index.html
                    :class: m-fullwidth

                    Take me there


        .. container:: m-col-m-4 m-text-center

            .. block-flat:: Skip directly to:

                .. button-default:: https://pressio.github.io/pressio-tutorials/html/index.html
                    :class: m-fullwidth

                    c++ tutorials

                .. button-default:: https://pressio.github.io/pressio4py/html/md_pages_demos_demo1.html
                    :class: m-fullwidth

                    pressio4py demos
