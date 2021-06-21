Projection-based reduced-order models and Pressio
##################################################

:breadcrumb: {filename}/overview.rst Overview
:summary: Intro to pROMs

Executive summary
=================
In a nutshell, projection-based reduced-order models are fast and accurate surrogate models. They are constructed via a combination of *a priori* training data and projection processes applied to governing equations. Many pROMs are *intrusive*, meaning that they require interfacing with the application code that they are seeking to approximate.  Implementing this coupling into large-scale codes poses numerous practical challenges. Pressio aims to address this issue by providing intrusive model reduction capabilities to large-scale application codes.



Why do we need pROMs?
=====================
  Simulating parameterized systems of equations is ubiquitous in science and engineering, playing an important role in fields such as engineering, ecology, and epidemiology. It is often the case that solving such systems is a computationally intensive process. For many-query analyses such as uncertainty quantification and optimization, lower-cost approximate models are need to make the analysis tractable.


What exactly are pROMs?
=======================
  Projection-based ROMs (pROMs) comprise a class of approximation techniques that, at their core, operate by replacing a high-dimensional system with a low-dimensional system. pROMs operate in an online—offline paradigm. In the offline stage, a computationally intensive process is undertaken to identify a low-dimensional trial subspace on which the system state can be well approximated. Typically, this process involves solving the original system, i.e., the *full-order model (FOM)*, for select parameter instances. In the online phase, pROMs then compute approximations to the governing equations that reside on this low-dimensional trial subspace. The results of this process is a fast approximate model that adheres to the governing equations.


What role does Pressio play?
============================
 Broadly speaking, pROM methods can be classified as *non-intrusive* or *intrusive*. For systems described by complex nonlinear dynamics, *intrusive* pROM techniques are popular. The online phase of these intrusive pROMs involves querying operators associated with the original full-order model, which means that these methods need to interface with the full-order model. Implementing this coupling into large-scale codes poses numerous practical challenges, including managing different data types and data communication. Further, intrusive pROMs often require solvers that are not standard in application codes. These aforementioned challenges pose a significant entry barrier for intrusive pROM methods. **Pressio is designed to address the entry barrier associated with intrusive ROM methods.**

What is Pressio, and how does it address the intrusiveness of pROMs?
====================================================================
  Pressio is an open-source project aimed at providing intrusive model reduction capabilities to large-scale application codes. The core of the Pressio project is a header-only C++ library that is designed to (1) interface with applications characterized by arbitrary data-types and (2) provide these applications with the necessary routines for performing model reduction, such as Galerkin and least-squares Petrov--Galerkin projections.




.. container:: m-row m-container-inflate

    .. container:: m-col-c-10 m-text-center

        .. block-primary:: Design of Pressio 

            Want to know about how Pressio is designed, and how it works? 

            .. button-primary:: {filename}/overview/design.rst
                :class: m-fullwidth

                Take me there
