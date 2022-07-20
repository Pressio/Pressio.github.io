Motivation and Philosophy
=========================

Simulating parameterized systems of equations is ubiquitous in science and engineering.
It is often the case that solving such systems with high level of accuracy is
a computationally intensive process.
For many-query analyses such as uncertainty quantification and optimization,
reduced models are required to make the analysis tractable.
Model reduction is a broad and active field.
Several techniques exist, but there is no such thing as "one method to rule them all".

We believe in model reduction techniques that use data but are grounded in physical laws. 
`Projection-based reduced-order modeling (pROM) <description.html>`_ falls in this category, 
and it is our current focus. This technique relies on a projection process applied to the governing 
equations of interest and, therefore, it adheres to physical laws.
It has shown large potential, but its main drawback is an intrusive nature.
This has been, historically, one of the key barriers (if not the main one) precluding 
this technique from impacting more broadly science and engineering. 
As a consequence, this has also limited the range of applications and the capabilities tested.
We believe this barrier can be broken, thus opening up large
opportunities to explore and mature this field.

The Pressio ecosystem is aimed at mitigating the intrusive nature of pROMs for large-scale codes, 
and providing a framework available to the community to foster research 
of new ideas and as well as more broad testing. This is our "why" and motivates this project.


The `Pressio EcoSystem <https://github.com/Pressio>`_ includes:

.. list-table::
   :widths: 30 50 20
   :header-rows: 1
   :align: left

   * - Name
     - Info
     -

   * - ``pressio``
     - Core C++ library
     - `Github link <https://pressio.github.io/pressio/html/index.html>`__

   * - ``pressio4py``
     - Python bindings to the core C++ library
     - `Github link <https://pressio.github.io/pressio4py/html/index.html>`__

   * - ``pressio-tools``
     - Distributed and on-node SVD and QR; sample mesh indices computation
     - `Github link <https://github.com/Pressio/pressio-tools>`__

   * - ``pressio-demoapps``
     - Suite of 1D, 2D, 3D problems with native support for sample mesh
     - `Github link <https://pressio.github.io/pressio-demoapps/index.html>`__


.. toctree::
    :maxdepth: 1
    :hidden:

    description

.. toctree::
    :caption: Libraries
    :maxdepth: 1
    :hidden:

    C++ library <https://pressio.github.io/pressio/html/index.html>
    pressio4py <https://pressio.github.io/pressio4py/html/index.html>
    pressio-tools <https://github.com/Pressio/pressio-tools>
    pressio-demoapps <https://pressio.github.io/pressio-demoapps/index.html>
    pressio-tutorials <https://pressio.github.io/pressio-tutorials>


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

    license

