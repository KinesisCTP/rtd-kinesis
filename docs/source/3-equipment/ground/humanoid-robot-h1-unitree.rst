.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: 0c0c108f-7171-4ea7-bbea-46882ddc78af

===============================
Humanoid Robot - H1-2 - Unitree
===============================

.. container:: equipment-kicker

   Unitree · H1-2

.. figure:: ../../_static/images/507_h1-unitree.png
   :alt: Humanoid Robot - H1-2 - Unitree
   :class: equipment-page-image
   :figclass: equipment-page-figure
   :align: center

   Humanoid Robot - H1-2 - Unitree

.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - Unitree
   * - **Model**
     - H1-2
   * - **Equipment class**
     - Ground Robot
   * - **Location**
     - C3.B2.029.E (KINESIS CTP)
   * - **Quantity**
     - 1
   * - **Status**
     - Active



Overview
--------

The Unitree H1-2 is a full-sized humanoid robot used for research and public demonstrations involving dynamic locomotion and human-robot interaction. It can be operated manually with a wireless handheld controller or programmatically via the Unitree SDK/API over a wired Ethernet connection, and includes onboard perception sensors for balance and environment awareness.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Standing dimensions**
     - H (1503 + 285) x W 510 x D 287 mm
   * - **Height**
     - approximately 1780 mm
   * - **Weight**
     - approximately 70 kg
   * - **Degrees of freedom**
     - 27
   * - **Leg degrees of freedom**
     - 6 per leg
   * - **Waist degrees of freedom**
     - 1
   * - **Arm degrees of freedom**
     - 7 per arm
   * - **Mobility**
     - Legged
   * - **Maximum speed**
     - under 2 m/s
   * - **Operating environment**
     - Indoor and outdoor
   * - **Battery energy capacity**
     - 864 Wh
   * - **Battery charge capacity**
     - 15 Ah
   * - **Maximum voltage**
     - 67.2 V
   * - **Arm load**
     - approximately 7 kg rated; approximately 21 kg peak
   * - **Maximum arm-joint torque**
     - approximately 120 N·m
   * - **Maximum knee-joint torque**
     - approximately 360 N·m
   * - **Processor**
     - Intel Core i5 for platform functions and Intel Core i7 for user development
   * - **Sensor type**
     - Livox MID-360 3D LiDAR and Intel RealSense D435i depth camera

Typical workflows
-----------------

1. Manual operation via wireless handheld remote for locomotion demonstrations
2. Programmatic control via Unitree SDK/API over wired Ethernet for autonomous tasks
3. Community engagement or promotional demonstrations in controlled indoor/outdoor spaces

.. note::

   These examples are an overview. Follow the current equipment manual and SOP,
   where available, together with the applicable risk assessment and training,
   for the complete procedure.

Software & dependencies
-----------------------

- Unitree SDK
- Unitree API


Safety & operating limits
-------------------------

.. warning::

   - Maintain a safe working radius of at least 2 m and avoid standing directly in front of or behind the robot because it may lose stability or fall.
   - For emergency stop, press L1+A on the remote to enter damping mode; the motors power down and the robot falls in place.
   - If the robot is unresponsive, use the battery power-off sequence or remove the battery.
   - Only trained personnel may charge, connect, or replace the battery.
   - The SELV system monitors critical faults and alerts or locks the robot when required.
   - For storage, enter damping mode, power off, remove the battery, and support the robot in a seated or suspended position; never store it standing unsupported.

**Access and operational conditions**

- Only trained and authorised personnel are allowed to operate or programme the robot. Operators must remind bystanders not to approach the robot during demonstrations.

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

``humanoid`` · ``bipedal`` · ``ground robot`` · ``legged`` · ``Unitree`` · ``H1-2`` · ``H1`` · ``human-robot interaction`` · ``research``


.. include:: /_includes/contact-lab-manager.inc
