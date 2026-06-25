============
Contributing
============

How to Contribute to This Documentation
---------------------------------------

We welcome contributions from all lab members! This documentation is meant to be collaboratively maintained.

Using AI Assistants
-------------------

To make contributing easier, we've created an ``AGENTS.md`` file in the repository root that provides comprehensive instructions for AI coding assistants (like GitHub Copilot, Claude, ChatGPT, etc.).

**To contribute using an AI assistant:**

1. Read the ``AGENTS.md`` file in the repository root
2. Share it with your AI assistant along with your proposed changes
3. The AI will help format your contribution correctly

GitHub Web Interface (Simplest)
-------------------------------

For small changes like fixing typos or updating information:

1. Navigate to the file on GitHub
2. Click the pencil icon (Edit this file)
3. Make your changes
4. Scroll down and click "Propose changes"
5. Create a pull request

Fork and Clone (Advanced)
-------------------------

For larger contributions:

1. Fork the repository to your GitHub account
2. Clone your fork locally:

   .. code-block:: bash

      git clone https://github.com/YOUR-USERNAME/rtd-kinesis.git

3. Create a new branch:

   .. code-block:: bash

      git checkout -b my-contribution

4. Make your changes
5. Commit and push:

   .. code-block:: bash

      git add .
      git commit -m "Description of changes"
      git push origin my-contribution

6. Create a pull request on GitHub

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

To add new equipment:

1. Edit ``docs/source/_static/data/equipment.json``
2. Add a new entry with all required fields (see existing entries as examples)
3. Optionally create a dedicated RST page in the appropriate equipment category

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
