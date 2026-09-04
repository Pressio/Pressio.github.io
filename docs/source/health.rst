Pressio ecosystem health
========================

This dashboard gives maintainers a shared view of release readiness and the
most important work across the core Pressio repositories. Repository data was
last collected **2026-09-04 00:41 UTC**. Lifecycle assessments and next objectives
are curated by the Pressio team; releases, CI, and issue counts come from GitHub.

.. raw:: html

   <div class="health-summary" aria-label="Ecosystem summary">
     <div><strong>5</strong><span>Repositories tracked</span></div>
     <div><strong>4</strong><span>Healthy</span></div>
     <div><strong>0</strong><span>Need attention</span></div>
     <div><strong>1</strong><span>Being modernized</span></div>
   </div>

Repository health
-----------------

.. raw:: html

   <div class="health-grid">
   
   <article class="health-card" data-status="healthy">
     <div class="health-card__header">
       <div>
         <h2><a href="https://github.com/Pressio/pressio-rom">pressio-rom</a></h2>
         <p class="health-role">Core C++ library for projection-based reduced-order modeling</p>
       </div>
       <span class="health-status health-status--healthy">Healthy</span>
     </div>
     <div class="health-metrics">
       <a class="health-metric" href="https://github.com/Pressio/pressio-rom/releases/tag/0.17.0">
         <span>Latest release</span><strong>0.17.0</strong>
         <small>2025-09-10</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-rom/actions/runs/17616318704">
         <span>Default-branch CI</span><strong class="ci-success">Success</strong>
         <small>Latest completed run</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-rom/issues?q=is%3Aissue+is%3Aopen">
         <span>Open issues</span><strong>14</strong>
         <small>Pull requests excluded</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-rom/issues?q=is%3Aissue+is%3Aopen+label%3Arelease-blocker">
         <span>Release blockers</span><strong>0</strong>
         <small>Curated by label</small>
       </a>
     </div>
     <div class="health-next">
       <span>Next objective</span>
       <p>Keep the core API, supported toolchains, and downstream libraries release-ready.</p>
       
     </div>
     <div class="health-card__footer">
       <span>Actively maintained core library</span>
       <a href="https://pressio.github.io/pressio-rom">Documentation <span aria-hidden="true">→</span></a>
     </div>
   </article>
   
   <article class="health-card" data-status="healthy">
     <div class="health-card__header">
       <div>
         <h2><a href="https://github.com/Pressio/pressio-ops">pressio-ops</a></h2>
         <p class="health-role">Portable linear algebra operations used across Pressio</p>
       </div>
       <span class="health-status health-status--healthy">Healthy</span>
     </div>
     <div class="health-metrics">
       <a class="health-metric" href="https://github.com/Pressio/pressio-ops/releases/tag/0.17.0">
         <span>Latest release</span><strong>0.17.0</strong>
         <small>2025-09-08</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-ops/actions/runs/17556985390">
         <span>Default-branch CI</span><strong class="ci-success">Success</strong>
         <small>Latest completed run</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-ops/issues?q=is%3Aissue+is%3Aopen">
         <span>Open issues</span><strong>3</strong>
         <small>Pull requests excluded</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-ops/issues?q=is%3Aissue+is%3Aopen+label%3Arelease-blocker">
         <span>Release blockers</span><strong>0</strong>
         <small>Curated by label</small>
       </a>
     </div>
     <div class="health-next">
       <span>Next objective</span>
       <p>Maintain backend coverage and compatibility with pressio-rom.</p>
       
     </div>
     <div class="health-card__footer">
       <span>Actively maintained core library</span>
       <a href="https://pressio.github.io/pressio-ops">Documentation <span aria-hidden="true">→</span></a>
     </div>
   </article>
   
   <article class="health-card" data-status="healthy">
     <div class="health-card__header">
       <div>
         <h2><a href="https://github.com/Pressio/pressio-demoapps">pressio-demoapps</a></h2>
         <p class="health-role">Reference applications and reproducible ROM demonstrations</p>
       </div>
       <span class="health-status health-status--healthy">Healthy</span>
     </div>
     <div class="health-metrics">
       <a class="health-metric" href="https://github.com/Pressio/pressio-demoapps/releases/tag/0.17.0">
         <span>Latest release</span><strong>0.17.0</strong>
         <small>2025-09-09</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-demoapps/actions/runs/17574823969">
         <span>Default-branch CI</span><strong class="ci-success">Success</strong>
         <small>Latest completed run</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-demoapps/issues?q=is%3Aissue+is%3Aopen">
         <span>Open issues</span><strong>26</strong>
         <small>Pull requests excluded</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio-demoapps/issues?q=is%3Aissue+is%3Aopen+label%3Arelease-blocker">
         <span>Release blockers</span><strong>0</strong>
         <small>Curated by label</small>
       </a>
     </div>
     <div class="health-next">
       <span>Next objective</span>
       <p>Keep examples building against supported Pressio releases.</p>
       
     </div>
     <div class="health-card__footer">
       <span>Actively maintained validation repository</span>
       <a href="https://pressio.github.io/pressio-demoapps">Documentation <span aria-hidden="true">→</span></a>
     </div>
   </article>
   
   <article class="health-card" data-status="modernization">
     <div class="health-card__header">
       <div>
         <h2><a href="https://github.com/Pressio/pressio4py">pressio4py</a></h2>
         <p class="health-role">Python bindings for the Pressio C++ libraries</p>
       </div>
       <span class="health-status health-status--modernization">Modernization underway</span>
     </div>
     <div class="health-metrics">
       <a class="health-metric" href="https://github.com/Pressio/pressio4py/releases/tag/v0.12.0">
         <span>Latest release</span><strong>v0.12.0</strong>
         <small>2021-10-15</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio4py/actions">
         <span>Default-branch CI</span><strong class="ci-unknown">Unknown</strong>
         <small>Latest completed run</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio4py/issues?q=is%3Aissue+is%3Aopen">
         <span>Open issues</span><strong>12</strong>
         <small>Pull requests excluded</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/pressio4py/issues?q=is%3Aissue+is%3Aopen+label%3Arelease-blocker">
         <span>Release blockers</span><strong>0</strong>
         <small>Curated by label</small>
       </a>
     </div>
     <div class="health-next">
       <span>Next objective</span>
       <p>Restore packaging and CI, then port the bindings to the current pressio-rom API.</p>
       <p class="health-tracking">Tracking: <a href="https://github.com/Pressio/pressio4py/issues/29">#29</a>, <a href="https://github.com/Pressio/pressio4py/issues/30">#30</a></p>
     </div>
     <div class="health-card__footer">
       <span>Modernization work is planned</span>
       <a href="https://pressio.github.io/pressio4py/html/index.html">Documentation <span aria-hidden="true">→</span></a>
     </div>
   </article>
   
   <article class="health-card" data-status="healthy">
     <div class="health-card__header">
       <div>
         <h2><a href="https://github.com/Pressio/rom-tools-and-workflows">rom-tools-and-workflows</a></h2>
         <p class="health-role">Python tools and workflows for constructing and using ROMs</p>
       </div>
       <span class="health-status health-status--healthy">Healthy</span>
     </div>
     <div class="health-metrics">
       <a class="health-metric" href="https://github.com/Pressio/rom-tools-and-workflows/releases/tag/v0.2.0">
         <span>Latest release</span><strong>v0.2.0</strong>
         <small>2025-09-29</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/rom-tools-and-workflows/actions/runs/33421873202">
         <span>Default-branch CI</span><strong class="ci-success">Success</strong>
         <small>Latest completed run</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/rom-tools-and-workflows/issues?q=is%3Aissue+is%3Aopen">
         <span>Open issues</span><strong>27</strong>
         <small>Pull requests excluded</small>
       </a>
       <a class="health-metric" href="https://github.com/Pressio/rom-tools-and-workflows/issues?q=is%3Aissue+is%3Aopen+label%3Arelease-blocker">
         <span>Release blockers</span><strong>0</strong>
         <small>Curated by label</small>
       </a>
     </div>
     <div class="health-next">
       <span>Next objective</span>
       <p>Maintain tested workflows, examples, and a dependable release process.</p>
       
     </div>
     <div class="health-card__footer">
       <span>Actively maintained workflow library</span>
       <a href="https://github.com/Pressio/rom-tools-and-workflows#readme">Documentation <span aria-hidden="true">→</span></a>
     </div>
   </article>
   </div>

How to read this page
---------------------

``Healthy`` means the repository is actively maintained and expected to work
on its supported platforms. ``Needs attention`` identifies a usable repository
with specific maintenance work. ``Modernization underway`` indicates a larger
planned migration. These lifecycle assessments are deliberately separate from
the latest CI result: a passing build alone does not establish project health.

The dashboard does not treat a large issue count as inherently unhealthy.
Release blockers are issues explicitly classified by maintainers and are the
most useful starting point for release planning.
