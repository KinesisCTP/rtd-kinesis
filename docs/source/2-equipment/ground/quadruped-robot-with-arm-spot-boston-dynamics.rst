.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: d97faae7-de64-45b8-ac47-8996696129c2

=================================================
Quadruped Robot with Arm - Spot - Boston Dynamics
=================================================

.. container:: equipment-kicker

   Boston Dynamics · Spot

.. figure:: ../../_static/images/100_spot-arm.png
   :alt: Quadruped Robot with Arm - Spot - Boston Dynamics
   :class: equipment-page-image
   :figclass: equipment-page-figure
   :align: center

   Quadruped Robot with Arm - Spot - Boston Dynamics

.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - Boston Dynamics
   * - **Model**
     - Spot
   * - **Equipment class**
     - Ground Robot
   * - **Location**
     - C3.B2.029.E (KINESIS CTP)
   * - **Quantity**
     - 1
   * - **Status**
     - Active
   * - **Training**
     - Required
   * - **Risk assessment**
     - Required
   * - **Primary contact**
     - Samuel A. Prieto (sxp8070)


Overview
--------

The Boston Dynamics Spot with Spot Arm is a legged, mobile ground robot with a 6-DOF manipulator and gripper used for remote inspection and general-purpose manipulation tasks. It can be driven manually with a tablet controller or operated programmatically via the Spot API, and can perform tasks like grasping objects, turning valves, and opening doors in industrial or controlled environments.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Standing dimensions**
     - L 1100 x W 500 x H 610 mm
   * - **Weight**
     - 40.5 kg
   * - **Degrees of freedom**
     - 12
   * - **Mobility**
     - Legged
   * - **Maximum speed**
     - 1.6 m/s
   * - **Operating environment**
     - Indoor and outdoor
   * - **Total mounted-payload limit**
     - 14 kg
   * - **Battery energy capacity**
     - 564 Wh
   * - **Battery life**
     - 90 min
   * - **Ingress protection**
     - IP54
   * - **Operating temperature**
     - -20 to 45 °C
   * - **Sensing modalities**
     - RGB, Stereo vision, Infrared
   * - **Stereo camera pairs**
     - 5
   * - **Built-in optical coverage**
     - 360 °
   * - **Built-in depth range**
     - 2 m
   * - **Arm degrees of freedom**
     - 6
   * - **Arm length at full extension**
     - 984 mm
   * - **Arm weight including gripper**
     - 8 kg
   * - **Maximum arm lift**
     - 11 kg
   * - **Continuous arm lift**
     - 5 kg
   * - **Maximum vertical arm reach**
     - 1,820 mm
   * - **Gripper aperture**
     - 175 mm
   * - **Peak gripper clamp force**
     - 130 N
   * - **Enterprise upgrade**
     - Spot Enterprise upgrade and Spot battery assigned to this robot.

Typical workflows
-----------------

1. Remote teleoperation for indoor/outdoor inspection
2. Grasping and picking up objects using the gripper
3. Turning/twisting/pulling tasks such as operating valves
4. Opening doors in manual operation or Autowalk missions
5. Recording and replaying missions (Autowalk) with data capture actions

Software & dependencies
-----------------------

- Spot tablet controller app
- Spot API

Access, training & booking
--------------------------

Access is restricted to trained and authorised personnel. Complete the required safety sign-off before operation and maintain a minimum 3 m clearance around the robot during all operations.

- **Training:** Hands-on training is required before operation.
- **Risk assessment:** A task-appropriate risk assessment is required before use.

Safety & operating limits
-------------------------

.. warning::

   - Intended for professional use in industrial, restricted, or controlled environments; do not use for collaborative applications involving physical interaction with humans.
   - Do not use Spot in home environments, to transport persons or animals, or to transport hazardous materials.
   - Keep clear of pinch and crush points at the arm joints and gripper, and account for unexpected motion during manipulation.
   - An extended arm or heavy payload can reduce stability; more than 5 kg at 0.5 m extension can unbalance Spot.
   - Maintain at least 3 m clearance, keep the arm stowed when not manipulating, and use slow speed when teaching or working near people.
   - Store batteries at approximately 50% state of charge for long-term storage.

**Approved operating area**

- KINESIS CTP Lab and its designated KINESIS controlled operating areas.

Operations outside the approved area require a submitted and approved
`Robotics Review Committee (RRC) Mission Review Form <https://docs.google.com/forms/d/e/1FAIpQLSdj0OyfnCpAIcmQqXW_oNY_B6kJzBgunmGXpXxznvEGFAQ2Ew/viewform>`_ before the experiment begins.

**Environmental limits**

- Operate at -20 °C to 45 °C and at no more than 99% non-condensing relative humidity.
- IP54: protect the robot from submersion and avoid rapid temperature transitions that can cause internal condensation.
- Do not operate Spot underwater or airborne.
- Assess the surface, debris, slopes, narrow passages, elevated edges, and lighting before operation.

**Required attire and conditional PPE**

- Long pants.
- Closed-toed shoes.
- Safety footwear is recommended when lifting or physically handling Spot.
- Hearing protection may be required if the configured A/V warning-system volume warrants it.

**Operational controls**

- Training required
- Risk assessment required
- Supervisor required



Keywords
--------

``mobile robot`` · ``quadruped`` · ``ground robot`` · ``robotic arm`` · ``manipulation`` · ``inspection`` · ``indoor`` · ``outdoor`` · ``Spot`` · ``legged``


.. include:: /_includes/contact-lab-manager.inc
