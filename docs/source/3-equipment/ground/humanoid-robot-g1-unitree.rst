.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: 7e021f5e-e159-49a7-b6e4-3620541f4db2

====================================
Humanoid Robot - G1 EDU U4 - Unitree
====================================

.. container:: equipment-kicker

   Unitree · G1 EDU U4

.. figure:: ../../_static/images/506_humanoid-g1-unitree.jpg
   :alt: Humanoid Robot - G1 EDU U4 - Unitree
   :class: equipment-page-image
   :figclass: equipment-page-figure
   :align: center

   Humanoid Robot - G1 EDU U4 - Unitree

.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - Unitree
   * - **Model**
     - G1 EDU U4
   * - **Equipment class**
     - Ground Robot
   * - **Location**
     - C3.B2.029.E (KINESIS CTP)
   * - **Quantity**
     - 1
   * - **Status**
     - Active


.. container:: equipment-booking-card

   **Check availability before planning**

   Review availability and reserve the equipment through the CTP Scheduling System.
   Access the system from the NYUAD network or through the VPN.

   .. container:: equipment-booking-actions

      `Book this equipment <https://corelabs.abudhabi.nyu.edu>`_


Overview
--------

The Unitree G1 EDU U4 is a compact 43-DOF humanoid robot with two force-controlled Dex3-1 three-fingered hands. It is used for research and demonstrations involving locomotion, dexterous manipulation, dynamic control, and human-robot interaction, with manual or programmatic operation through the Unitree SDK/API.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Standing dimensions**
     - H 1320 x W 450 x D 200 mm
   * - **Folded dimensions**
     - H 690 x W 450 x D 300 mm
   * - **Height**
     - 1,320 mm
   * - **Weight**
     - more than 35 kg
   * - **Degrees of freedom**
     - 43
   * - **Leg degrees of freedom**
     - 6 per leg
   * - **Waist degrees of freedom**
     - 3
   * - **Arm degrees of freedom**
     - 5 per arm
   * - **Additional wrist degrees of freedom**
     - 2 per wrist
   * - **Hand degrees of freedom**
     - 7 per Dex3-1 hand
   * - **Mobility**
     - Legged
   * - **Maximum speed**
     - over 2 m/s
   * - **Operating environment**
     - Indoor and outdoor
   * - **Battery charge capacity**
     - 9,000 mAh
   * - **Battery life**
     - approximately 120 min
   * - **Arm load**
     - approximately 3 kg maximum
   * - **Maximum knee-joint torque**
     - 120 N·m
   * - **Sensor type**
     - 3D LiDAR and depth camera
   * - **Included accessories**
     - 2 Unitree Dex3-1 force-controlled three-fingered hands with tactile sensor arrays

Typical workflows
-----------------

1. Manual operation via wireless handheld remote for locomotion and demonstrations
2. Programmatic control via Unitree SDK/API over wired Ethernet for autonomous tasks
3. Research in human-robot interaction, locomotion, dynamic control, and multi-agent tasks

.. note::

   These examples are an overview. Follow the current equipment manual and SOP,
   where available, together with the applicable risk assessment and training,
   for the complete procedure.

Software & dependencies
-----------------------

- Unitree SDK
- ROS/ROS2


Safety & operating limits
-------------------------

.. warning::

   - Key hazards include high-torque actuators, loss of stability or falling during locomotion, battery fire or burns if damaged, and heat after extended use.
   - Maintain a safe working radius of at least 2 m.
   - Never attempt to catch or support the robot if it begins to fall, and do not touch the joints or core immediately after use.
   - For emergency stop, press L1+A on the remote to enter damping mode; if the robot is unresponsive, use the battery power-off sequence or remove the battery.
   - For storage, enter damping mode, power off, remove the battery, and support the robot in a seated or suspended position.

**Access and operational conditions**

- Only trained and authorised personnel are allowed to operate or programme the robot. Operating area must be clear of obstacles and bystanders with a minimum 2 m radius.

**Approved operating area**

- KINESIS CTP Lab and its designated KINESIS controlled operating areas.

Operations outside the approved area require a submitted and approved
`Robotics Review Committee (RRC) Mission Review Form <https://docs.google.com/forms/d/e/1FAIpQLSdj0OyfnCpAIcmQqXW_oNY_B6kJzBgunmGXpXxznvEGFAQ2Ew/viewform>`_ before the experiment begins.

**Environmental limits**

- Keep the equipment dry; do not operate it in rain, spray, or wet conditions.

**Required attire and conditional PPE**

- Long pants.
- Closed-toed shoes.


Related equipment & documentation
---------------------------------

- **Compatible equipment:** :doc:`Dexterous Hand - RH56 - Inspire Robots </3-equipment/ground/dexterous-hand-rh56-inspire-robots>`

Keywords
--------

``humanoid`` · ``bipedal`` · ``ground robot`` · ``legged`` · ``Unitree`` · ``G1`` · ``G1 EDU U4`` · ``U4`` · ``Dex3-1`` · ``dexterous manipulation`` · ``research`` · ``indoor``


.. include:: /_includes/contact-lab-manager.inc
