KINESIS CTP Lab Documentation Website
=====================================

This repository contains the source code for a static website built using Sphinx and the Read the Docs theme. The site presents an overview of the KINESIS CTP Lab, including its facilities, equipment, and research areas, with a modern, web-style interface.

📖 **View the Live Documentation:** https://rtd-kinesis.readthedocs.io

Overview
--------

The website is designed to move beyond traditional documentation and provide a more interactive, visually structured experience. It includes a custom homepage with navigation cards, a toggleable sidebar, and a full-width layout.

Features
--------

- Built with Sphinx
- Read the Docs theme with extensive custom styling
- Full-width responsive homepage with modern design
- Sidebar navigation with "Home" button on documentation pages
- Custom homepage with 4 showcase sections
- Organized content structure:
  
  - Lab Overview (policies, publications, collaborations)
  - Facilities (arena, workspace, safety equipment)
  - Equipment (ground robots, drones, underwater systems, sensors)
  - Computing & Networks (AI workstations, infrastructure)
  - Talks & Demos (presentations, videos, public appearances)

- Equipment documentation with images and detailed specifications
- Consistent formatting with warning sections as bullet points
- Automatic builds on every push to main branch  

Accessing the Documentation
----------------------------

Live Documentation
~~~~~~~~~~~~~~~~~~

The documentation is hosted on Read the Docs and is automatically built from the ``main`` branch:

**🌐 https://rtd-kinesis.readthedocs.io**

The site is automatically rebuilt whenever changes are pushed to the repository, ensuring the documentation is always up to date.

Local Preview
~~~~~~~~~~~~~

If you want to preview changes locally before pushing, follow the `Installation`_ and `Build the Site`_ sections below to generate a local copy of the documentation.

Project Structure
-----------------

::

   rtd-kinesis/
   │
   ├── docs/
   │   ├── source/
   │   │   ├── index.rst (homepage)
   │   │   ├── conf.py (Sphinx configuration)
   │   │   │
   │   │   ├── 1-lab-overview/
   │   │   │   ├── index.rst
   │   │   │   ├── 1-general-policies.rst
   │   │   │   └── ... (other lab overview pages)
   │   │   │
   │   │   ├── 2-equipment/
   │   │   │   ├── index.rst
   │   │   │   ├── ground/ (humanoids, quadrupeds, buggy, robotic arm)
   │   │   │   ├── aerial/ (drones)
   │   │   │   ├── water/ (underwater ROVs)
   │   │   │   └── sensors/ (cameras, LiDAR, 3D scanners, etc.)
   │   │   │
   │   │   ├── 3-computing/
   │   │   │   ├── index.rst
   │   │   │   ├── workstations/ (AI workstations, Vicon PC, DGX Spark)
   │   │   │   └── networks/ (KINESIS CTP network, IP allocation)
   │   │   │
   │   │   ├── 4-facilities/
   │   │   │   ├── index.rst
   │   │   │   ├── arena.rst
   │   │   │   ├── workspace.rst
   │   │   │   └── safety.rst
   │   │   │
   │   │   ├── 5-talks-demos/
   │   │   │   └── ... (presentations, demo videos)
   │   │   │
   │   │   └── _static/
   │   │       ├── custom.css (custom styling)
   │   │       ├── custom.js (custom JavaScript)
   │   │       ├── images/ (equipment and facility images)
   │   │       │   └── README.md (image naming conventions)
   │   │       └── data/
   │   │           └── equipment.json (equipment database)
   │   │
   │   ├── build/
   │   │   └── html/
   │   │
   │   ├── requirements.txt
   │   ├── Makefile
   │   └── make.bat
   │
   └── README.rst

Installation
------------

1. Clone the repository::

   git clone https://github.com/KinesisCTP/rtd-kinesis

   cd rtd-kinesis

2. Install dependencies::

   pip install -r docs/requirements.txt

If ``requirements.txt`` does not include Sphinx::

   pip install sphinx sphinx-rtd-theme

Build the Site
--------------

Navigate to the ``docs`` directory and build the HTML files::

   cd docs
   make html

The generated site will be available at::

   docs/build/html/index.html

Open it in your browser::

   open build/html/index.html

Development Workflow
--------------------

1. Edit ``.rst`` files inside::

      docs/source/

2. Modify styles in::

      docs/source/_static/custom.css

3. Modify interactivity::

      docs/source/_static/custom.js

4. Rebuild the site after changes::

      make clean
      make html

Customization
-------------

Styling
~~~~~~~

Custom styles are defined in::

   docs/source/_static/custom.css

Includes:
- Full-width layout
- Card-based homepage
- Purple theme
- Sidebar animations

JavaScript
~~~~~~~~~~

Custom behavior is handled in::

   docs/source/_static/custom.js

Includes:
- Sidebar toggle
- Layout shifting
- Card interaction effects

Content Sections
----------------

- **Homepage (index.rst)**  
  Modern landing page with hero section and 4 showcase cards for navigation

- **Lab Overview (1-lab-overview/)**  
  Lab presentation, general policies, processes, publications, collaborations, useful links, and contribution guidelines

- **Facilities (4-facilities/)**  
  Arena specifications (17m × 6.4m × 8m motion capture space), workspace details, and safety protocols

- **Equipment (2-equipment/)**  
  Comprehensive catalog organized by category:
  
  - Ground Systems: Humanoid robots (G1, H1), quadrupeds (Spot, Spot+Arm), autonomous buggy, robotic arm
  - Aerial Systems: DJI drones (Matrice 300 RTK, Mavic Pro 2)
  - Underwater Systems: ROVs (Defender, EXRAY)
  - Sensors: 3D scanners, LiDAR, motion capture, cameras, acoustic imager

- **Computing & Networks (3-computing/)**  
  AI workstations (Lambda, DGX Spark), Vicon PC, Linux workstation, network architecture, and IP allocation

- **Talks & Demos (5-talks-demos/)**  
  Lab presentations, demo videos, and public appearances

Equipment Images
----------------

Equipment images follow a consistent naming convention stored in ``docs/source/_static/images/``:

- Format: ``{legacy_id}_{equipment-slug}.{ext}``
- Example: ``99_spot-boston-dynamics.jpg``, ``506_humanoid-g1-unitree.jpg``
- See ``docs/source/_static/images/README.md`` for complete image catalog

Formatting Standards
--------------------

- Warning sections formatted as bullet points for readability
- Location tags: ``KINESIS CTP`` (without duplication)
- Risk assessments explicitly stated as "Risk Assessment Required"
- First letter of each warning sentence capitalized
- Equipment pages include images at 40-60% width

Notes
-----

- Homepage uses a modern, marketing-style design with full-width layout
- Documentation pages use traditional sidebar navigation
- Sidebar includes a "Home" button to return to the modern homepage
- Navigation structure matches homepage showcase order
- All changes are automatically deployed to Read the Docs on push to main branch
- Equipment data is centralized in ``equipment.json`` for consistency

License
-------

This project is for educational and demonstration purposes.
