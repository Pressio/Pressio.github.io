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

        .. container:: m-col-l-6 m-push-l-1 m-col-m-7 m-nopadb

            .. raw:: html

                <h1 style="text-transform:capitalize">Pressio</h1>


    .. container:: m-row

        .. container:: m-col-l-9 m-push-l-1

                *Pressio is an open-source project aimed at alleviating the intrusive nature of* `projection-based reduced-order models <{filename}/overview/proms.rst>`_ *for large-scale codes. The core of the Pressio project is a header-only C++ library that leverages generic programming to interface with shared or distributed memory applications using arbitrary data-types. Pressio provides numerous functionalities and solvers for performing model reduction, such as Galerkin and least-squares Petrov–Galerkin projections.*

    .. container:: m-row

        .. container:: m-col-l-15 m-push-l-1

          **Features of the Pressio C++ library include**
            1. Numerous model reduction routines, including Galerkin, least-squares, and windowed least-squares projections
            2. Native support for multiple datatypes, including Eigen, Kokkos, and Tpetra
            3. Support for arbitrary datatypes through custom operations

        .. container:: m-col-l-15 m-push-l-1

          **The Pressio ecosystem also offers**
            1. `pressio4py <https://pypi.org/project/pressio4py/>`_: Python bindings enabling Pressio's C++ library to be natively used in Python-only applications.
            2. `pressio-tools <https://github.com/Pressio/pressio-tools>`_: A library for large-scale SVD, QR, and sample meshes.
            3. `pressio-demoapps <https://github.com/Pressio/pressio-demoapps>`_: A suite of 1d, 2d, and 3d demo applications for testing pROMs and hyper-reduction.


    ..
       .. container:: m-row

	   .. container:: m-col-l-9 m-push-l-1

	       Want to learn more about pROMs? Explore `steps typically involved
	       in pROMs <{filename}/overview/proms.rst>`_.


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

            .. block-flat:: Want to skip directly to the tutorials/demos?


                .. button-default:: https://pressio.github.io/pressio-tutorials/html/index.html
                    :class: m-fullwidth

                    c++ tutorials

                .. button-default:: https://pressio.github.io/pressio4py/html/md_pages_demos_demo1.html
                    :class: m-fullwidth

                    pressio4py demos
