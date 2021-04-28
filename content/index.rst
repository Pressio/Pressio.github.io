Pressio
#############

:save_as: index.html
:cover: {static}/img/top1.jpg
:url:
:description: Projection-based model reduction for dynamical systems.
:summary: Model reduction for ...
:hide_navbar_brand: True
:landing:
    .. container:: m-row

        .. container:: m-col-l-6 m-push-l-1 m-col-m-7 m-nopadb

            .. raw:: html

                <h1 style="text-transform:capitalize">Pressio</h1>

    .. container:: m-row

        .. container:: m-col-l-6 m-push-l-1

            **Open-source project aimed at enabling leading-edge projection-based
            reduced order models (pROMs) for dynamical systems
            in science and engineering.**


    .. container:: m-row

        .. container:: m-col-l-6 m-push-l-1

            Projection-based model reduction refers to a class of surrogate models that reduce the number of degrees of freedom in the high-fidelity model through a projection process. This projection step applied to the governing equations often enables one to make stronger performance guarantees (e.g., of structure preservation, of accuracy via adaptivity) than other surrogates like data-fits and perform more accurate a posteriori error analysis (e.g., via a posteriori error bounds or error models).

	    Want to learn more about pROMs? Explore the `steps typically involved in pROMs <{filename}/overview/proms.rst>`_.


        .. container:: m-col-l-2 m-push-l-2 m-col-m-4 m-col-s-6 m-push-s-3 m-col-t-8 m-push-t-2

            .. figure:: {static}/img/plogo.png


    .. container:: m-row

        .. container:: m-col-l-9 m-push-l-1

            .. raw:: html

                <p class="m-text m-default m-big"><i>Pressio aims to mitigate the
                implementation burden of projection-based model reduction
                in large-scale applications without compromising performance.</i></p>


    ..
       .. container:: m-row

	   .. container:: m-col-l-9 m-push-l-1

	       Want to learn more about pROMs? Explore the `steps typically involved
	       in pROMs <{filename}/overview/proms.rst>`_.


    .. raw:: html

        <br>

    .. container:: m-row m-container-inflate

        .. container:: m-col-m-6 m-text-center

            .. block-primary:: Core C++ library

                Do you have a C++ application and want to know how to use *pressio* from C++?
                Follow this link to the userguide and documentation.

                .. button-primary:: https://pressio.github.io/pressio/html/index.html
                    :class: m-fullwidth

                    Take me there


        .. container:: m-col-m-6 m-text-center

            .. block-primary:: Python bindings library

                Do you have a Python application and would like to use Pressio
                *without* touching C++? We have Python bindings for that!
                This is the link for you.

                .. button-primary:: https://pressio.github.io/pressio4py/html/index.html
                    :class: m-fullwidth

                    Take me there




    .. container:: m-row m-text-center

        .. container:: m-push-l-3 m-col-m-6 m-text-center

            .. block-flat:: Tutorials/Demos

		Want to skip directly to the tutorials/demos?

		.. button-default:: https://pressio.github.io/pressio-tutorials/html/index.html
		    :class: m-fullwidth

                    c++ tutorials

		.. button-default:: https://pressio.github.io/pressio4py/html/md_pages_demos_demo1.html
		    :class: m-fullwidth

                    pressio4py demos
