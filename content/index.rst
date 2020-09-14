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


        .. container:: m-col-l-2 m-push-l-2 m-col-m-4 m-col-s-6 m-push-s-3 m-col-t-8 m-push-t-2

            .. figure:: {static}/img/plogo.png


    .. container:: m-row

        .. container:: m-col-l-9 m-push-l-1

            .. raw:: html

                <p class="m-text m-default m-big"><i>Pressio aims to mitigate the
                implementation burden of projection-based model reduction
                in large-scale applications without compromising performance.</i></p>


    .. container:: m-row

        .. container:: m-col-l-9 m-push-l-1

            Interested in more? Explore the `steps typically involved
	    in pROMs <{filename}/overview/proms.rst>`_ or
	    the `design idea behind Pressio <{filename}/overview/design.rst>`_.


    .. raw:: html

        <br>

    .. container:: m-row m-container-inflate

        .. container:: m-col-m-6 m-text-center

            .. figure: : {static}/img/feature-6.png
                :figclass: m-fullwidth m-warning
                :alt: Core features

            .. block-default:: Core C++ library

                Do you have a C++ application and want to know how to use *pressio* from C++?
                Follow this link below to read about the userguide.

                .. button-primary:: https://github.com/Pressio/pressio
                    :class: m-fullwidth

                    Explore the C++ library

        .. container:: m-col-m-6 m-text-center

            .. figure: : {static}/img/feature-9.png
                :figclass: m-fullwidth m-info
                :alt: Feature

            .. block-default:: Python bindings

                Do you have a Python application and would like to use Pressio
                *without* touching C++? We have Python bindings for that!
                This is the link for you.

                .. button-primary:: https://github.com/Pressio/pressio4py
                    :class: m-fullwidth

                    Explore **pressio4py**
