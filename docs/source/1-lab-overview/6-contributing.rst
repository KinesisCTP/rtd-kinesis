============
Contributing
============

How to Contribute to This Documentation
---------------------------------------

Contributions from lab members are welcome. This documentation is collaboratively maintained.

AI-Assisted Contributions
-------------------------

The repository-root ``AGENTS.md`` defines the formatting, source-of-truth, and validation rules for
AI-assisted contributions. Review all resulting changes before submission.

GitHub Web Interface (Simplest)
-------------------------------

For small changes like fixing typos or updating information:

1. Navigate to the file on GitHub
2. Click the pencil icon (Edit this file)
3. Make your changes
4. Scroll down and click "Propose changes"
5. Create a pull request

Private Repository Workflow (Advanced)
--------------------------------------

The private ``KinesisCTP/rtd-kinesis-internal`` repository is the canonical documentation
source. The public ``KinesisCTP/rtd-kinesis`` repository is generated automatically and must not
be edited directly.

For larger contributions, contributors with private-repository access can:

1. Clone the private repository locally:

   .. code-block:: bash

      git clone git@github.com:KinesisCTP/rtd-kinesis-internal.git

2. Create a new branch:

   .. code-block:: bash

      git checkout -b my-contribution

3. Make the changes
4. Commit and push the branch:

   .. code-block:: bash

      git add .
      git commit -m "Description of changes"
      git push origin my-contribution

5. Create a pull request against the private repository

reStructuredText Basics
-----------------------

This documentation uses reStructuredText (RST) format. Key syntax:

**Headers:**

.. code-block:: rst

   Document Title
   ==============

   Section
   -------

   Subsection
   ^^^^^^^^^^

**Links:**

.. code-block:: rst

   `Link text <https://example.com>`_

**Images:**

.. code-block:: rst

   .. image:: ../_static/images/filename.jpg
      :alt: Description
      :width: 600px

**Admonitions:**

.. code-block:: rst

   .. note::

      This is a note.

   .. warning::

      This is a warning.

Adding Equipment
----------------

Equipment records originate in the canonical KINESIS vault. The JSON data and dedicated RST pages
in this repository are generated outputs and must not be edited directly.

To add or update equipment:

1. Create or update the canonical Markdown note under ``equipment/<class>/`` in the vault
2. Complete the required structured fields and explicit wiki disposition
3. Run the vault equipment sync in validation mode, then in write mode
4. Verify the generated equipment data, pages, navigation, and private/public documentation builds

Pull Request Process
--------------------

1. Ensure your changes follow the existing style and format
2. Check that links and images work correctly
3. Write a clear description of your changes in the PR
4. A maintainer will review and provide feedback
5. Once approved, your contribution will be merged

Questions?
----------

Contact the lab maintainers for assistance with contributions.
