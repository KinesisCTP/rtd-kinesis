==========================
Computing Infrastructure
==========================

The KINESIS CTP Lab features a comprehensive computing infrastructure supporting research and development activities across robotics, AI, and motion capture systems.

Our infrastructure includes:

- **Networks**: KINESIS CTP (main lab network) and Hermes (arena wireless network)
- **Workstations**: Specialized computers for Vicon control, general R&D, and AI/ML workloads
- **Motion Capture Integration**: Vicon system with dedicated networking for real-time position tracking

Infrastructure at a Glance
--------------------------

- :doc:`networks/index` covers KINESIS CTP, Hermes, routers, wired ports, and IP assignment.
- index covers the Vicon PC, Linux workstation, AI workstation, and DGX Spark.
- :doc:`vicon-system/index` covers motion capture networking, tracking workflows, setup, and data broadcast.

Common Tasks
------------

- Use ip allocation before assigning a static IP.
- Check workstation pages before starting GPU or motion-capture workloads.
- Review Vicon setup guidance before relying on Arena tracking data.

.. toctree::
   :maxdepth: 2
   :caption: Infrastructure Components
   :hidden:

   networks/index
   vicon-system/index
