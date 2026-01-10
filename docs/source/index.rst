Motivation and Philosophy
=========================

Simulating parameterized systems of equations is fundamental in science and engineering but is often computationally expensive. In many-query settings such as uncertainty quantification and optimization, reduced-order models (ROMs) are required to make these analyses tractable. Model reduction comprises a range of approaches with different tradeoffs, and no single method is universally applicable.

Projection-based reduced-order modeling (pROM) constructs reduced models by projecting the governing equations onto low-dimensional subspaces, thereby preserving key physical structure. Despite demonstrated effectiveness, pROM adoption has been limited by its intrusive implementation requirements, which constrain applicability and large-scale testing.

The Pressio ecosystem addresses this limitation by providing a framework that reduces the intrusiveness of pROMs for large-scale simulation codes and supports the development, evaluation, and comparison of reduced-order modeling methods across applications.


The `Pressio EcoSystem <https://github.com/Pressio>`_ includes:

.. list-table::
   :widths: 25 35 20 20
   :header-rows: 1
   :align: left

   * - Name
     - Info
     - Latest Release
     -

   * - ``pressio-demoapps``
     - Suite of 1D, 2D, 3D problems spanning multiple physics and native support for sample mesh
     - 0.17.0
     - `Documentation <https://pressio.github.io/pressio-demoapps>`__

   * - ``pressio-log``
     - Header-only logging utility for Pressio libraries
     - 0.17.0
     - `GitHub <https://github.com/Pressio/pressio-log>`__

   * - ``pressio-ops``
     - Core operations for the Pressio ecosystem
     - 0.17.0
     - `Documentation <https://pressio.github.io/pressio-ops>`__

   * - ``pressio-rom``
     - C++ core library: ode, solvers, ROMs, etc
     - 0.17.0
     - `Documentation <https://pressio.github.io/pressio-rom>`__

   * - ``pressio-tutorials``
     - Tutorials suite for the pressio C++ library
     - 0.17.0
     - `Documentation <https://pressio.github.io/pressio-tutorials/>`__

   * - ``pressio-schwarz``
     - Schwarz coupling for projection-based ROMs with Pressio
     - 0.17.0
     - `GitHub <https://github.com/Pressio/pressio-schwarz>`__

   * - ``pressio4py``
     - Python bindings to the core C++ library
     - 0.12.0 (see disclaimer below)
     - `Documentation <https://pressio.github.io/pressio4py/html/index.html>`__

   * - ``rom-tools-and-workflows``
     - Tools and workflows for reduced-order modeling
     - 0.2.0
     - `GitHub <https://github.com/Pressio/rom-tools-and-workflows>`__


.. warning::

   Disclaimer: due to limited resources/time, we are currently forced to
   pause the development of ``pressio4py``, so it will stay out of sync until
   we will find the time to update it and push another release.

.. toctree::
    :maxdepth: 1
    :hidden:

    description

.. toctree::
    :caption: Libraries
    :maxdepth: 1
    :hidden:

    pressio-demoapps <https://pressio.github.io/pressio-demoapps>
    pressio-log <https://github.com/Pressio/pressio-log>
    pressio-ops <https://pressio.github.io/pressio-ops>
    pressio-rom <https://pressio.github.io/pressio-rom>
    pressio-tutorials <https://pressio.github.io/pressio-tutorials>
    pressio-schwarz <https://github.com/Pressio/pressio-schwarz>
    pressio4py <https://pressio.github.io/pressio4py/html/index.html>
    rom-tools-and-workflows <https://github.com/Pressio/rom-tools-and-workflows>

.. toctree::
    :caption: Portfolio
    :maxdepth: 1
    :hidden:

    hifire
    blottner
    seismic

.. toctree::
    :caption: Miscellanea
    :maxdepth: 1
    :hidden:

    Pressio GitHub <https://github.com/Pressio>
    license
