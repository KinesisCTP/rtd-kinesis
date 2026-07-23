KINESIS CTP Lab Documentation
=============================

This private repository is the canonical authoring and deployment source for the KINESIS CTP Lab
documentation. It produces two different reader-facing sites:

- the full internal wiki for the intended NYU/KINESIS audience; and
- a sanitized public subset published through a separate generated repository.

Do not author documentation in the generated public repository.

Live Sites
----------

Internal wiki
~~~~~~~~~~~~~

`https://kinesis.abudhabi.nyu.edu/ <https://kinesis.abudhabi.nyu.edu/>`_

The internal site is built from this repository's full Sphinx source. A successful push to
``main`` publishes a private multi-architecture container image to GitHub Container Registry. The
production host follows the accepted ``main`` image, validates each candidate, and preserves the
previous working image for rollback.

The institutional front end and origin controls define the current access boundary. Consult
`deploy/private-wiki/README.md <deploy/private-wiki/README.md>`_ for the deployment design,
security limitations, update service, health checks, and rollback procedure.

Sanitized public wiki
~~~~~~~~~~~~~~~~~~~~~

`https://rtd-kinesis.readthedocs.io/ <https://rtd-kinesis.readthedocs.io/>`_

The public site contains only the export approved for anonymous access. It is generated from this
private source by ``docs/maintenance/export_public.py`` and pushed by automation to
`KinesisCTP/rtd-kinesis <https://github.com/KinesisCTP/rtd-kinesis>`_. Read the Docs builds that
generated repository.

The public repository is an output, not an authoring source. Fix public content or export behavior
here, then regenerate it through the private-to-public workflow.

Publication Model
-----------------

::

   Canonical vault equipment records
                  |
                  v
   rtd-kinesis-internal (this repository)
          |                         |
          | full internal build     | sanitized export
          v                         v
   private GHCR image        KinesisCTP/rtd-kinesis
          |                         |
          v                         v
   internal production wiki  public Read the Docs site

The two publication paths run from ``main``:

- ``.github/workflows/publish-private-image.yml`` builds and smoke-tests the full internal site,
  publishes immutable commit tags plus the ``main`` release channel, and smoke-tests the published
  image.
- ``.github/workflows/publish-public.yml`` runs the public exporter and, when the repository token
  is configured, synchronizes the sanitized result to ``KinesisCTP/rtd-kinesis``.

Repository Contents
-------------------

::

   .github/workflows/              Publication workflows
   deploy/private-wiki/            Production image, proxy, updater, health checks, and runbook
   docs/maintenance/               Public exporter, exclusions, denylist, tests, and roadmap
   docs/source/                    Canonical Sphinx source
     1-lab-overview/               Policies, processes, publications, and contributing guidance
     2-facilities/                 Arena, workspace, safety, and facilities reference
     3-equipment/                  Generated equipment reference grouped by category
     4-computing/                  Workstations, networks, and Vicon infrastructure
     _static/                      Styling, images, generated data, and controlled bundles
     _templates/                   Generated equipment-page templates
   generate_equipment_pages.py     Deterministic equipment-page generator
   test_generate_equipment_pages.py
   AGENTS.md                       Authoring, privacy, roadmap, and validation requirements

Content Ownership and Privacy
-----------------------------

Normal reference pages are authored in ``docs/source``. Equipment facts follow a stricter
source-of-truth direction:

::

   coruscant-vault/equipment/<class>/*.md
       -> sync/equipment_to_wiki.py
       -> docs/source/_static/data/equipment.json
       -> generate_equipment_pages.py
       -> generated equipment RST pages

Do not hand-edit generated equipment JSON or generated equipment pages.

Private/public controls include:

- Sphinx conditional blocks for content that belongs only in the internal build;
- ``docs/maintenance/public-exclude.txt`` for files omitted from the anonymous export;
- a denylist and export tests that block unsafe public output;
- content-addressed private manuals, SOPs, and risk assessments removed by the public exporter; and
- one explicit anonymous onboarding-document allowlist generated from the canonical safety
  register.

The detailed authoring and data-boundary rules are in ``AGENTS.md``.

Local Setup
-----------

Clone this private repository, not the generated public repository:

::

   git clone https://github.com/KinesisCTP/rtd-kinesis-internal.git
   cd rtd-kinesis-internal

Create an environment and install the Sphinx dependencies:

::

   python -m venv .venv
   python -m pip install -r docs/requirements.txt

Activate the virtual environment using the command appropriate for the operating system before
running the checks below.

Strict Internal Build
---------------------

::

   python -m sphinx -W --keep-going -E -a -b html \
     -t internal \
     -D "html_title=KINESIS CTP Lab — Internal" \
     docs/source docs/build/internal-html

The internal tag enables internal-only blocks and the private GitHub edit-link target.

Sanitized Public Check
----------------------

::

   python docs/maintenance/export_public.py \
     --source . \
     --output /tmp/rtd-kinesis-public-export \
     --check

   python -m sphinx -W --keep-going -E -a -b html \
     /tmp/rtd-kinesis-public-export/docs/source \
     docs/build/public-html

Use a suitable temporary path on Windows instead of ``/tmp``.

Generated Equipment Check
-------------------------

::

   python generate_equipment_pages.py --check

Local Visual Preview and Approval
---------------------------------

Rendered wiki changes must be reviewed locally before they enter production history:

1. Build the strict internal and sanitized-public variants.
2. Serve the internal build locally:

   ::

      python -m http.server 8000 \
        --bind 127.0.0.1 \
        --directory docs/build/internal-html

3. Open ``http://127.0.0.1:8000/`` and review the affected desktop and mobile layouts.
4. Obtain explicit visual approval before committing, pushing, opening or merging a pull request,
   or deploying the change.
5. After approval, squash the review iterations into one deliberate production commit.

This approval gate applies to rendered content, layout, navigation, styling, and assets. It keeps
back-and-forth visual drafts out of ``main`` while still allowing thorough local iteration.

Contribution and Release Workflow
---------------------------------

1. Find the relevant issue in ``KinesisCTP/rtd-kinesis-internal`` and its
   ``KinesisCTP`` Project 1 item. Create a sanitized roadmap issue only when no suitable item
   exists.
2. Work locally and run the relevant generator, internal build, public export, and public build
   checks.
3. Serve the local preview and obtain explicit visual approval when the rendered result changes.
4. Create one focused branch and pull request with the approved result and validation evidence.
5. Merge only after required checks pass.
6. Confirm both publication workflows and the final live pages.
7. Close the roadmap issue and mark its Project item Done only after merge and deployment
   acceptance are complete.

Production Deployment
---------------------

The internal production updater checks the private ``main`` image on a two-minute timer. It starts
the candidate separately, waits for health, smoke-tests the published site, and rolls back
automatically if validation fails. The host must not be edited as an authoring surface.

The public export workflow updates the generated public repository. Read the Docs then rebuilds
the public ``main`` branch. Never bypass the exporter by manually editing the public checkout.

Health and release details:

- internal health endpoint: ``https://kinesis.abudhabi.nyu.edu/healthz``;
- private deployment runbook: ``deploy/private-wiki/README.md``;
- public export contract: ``docs/maintenance/export_public.py`` and
  ``docs/maintenance/public-exclude.txt``; and
- roadmap and acceptance model: ``docs/maintenance/wiki-roadmap.md``.

Technology
----------

- Sphinx 7.1
- Read the Docs theme with KINESIS-specific responsive styling
- reStructuredText source
- deterministic equipment-page generation from the canonical vault
- Docker/NGINX production packaging for the internal site
- Read the Docs hosting for the sanitized public site
