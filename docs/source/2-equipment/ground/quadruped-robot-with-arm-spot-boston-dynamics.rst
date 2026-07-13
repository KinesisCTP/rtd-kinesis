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

   * - **Arm degrees of freedom**
     - 6
   * - **Body degrees of freedom**
     - 12
   * - **Mobility**
     - Legged
   * - **Maximum arm lift**
     - 11 kg
   * - **Maximum range**
     - 2 m
   * - **Maximum speed**
     - 1.6 m/s
   * - **Operating environment**
     - Indoor and outdoor
   * - **Body payload**
     - 14 kg
   * - **Battery life**
     - 90 min
   * - **Sensing modalities**
     - RGB, LiDAR, Thermal
   * - **Enterprise upgrade**
     - Spot Enterprise upgrade and Spot battery assigned to this robot.
   * - **Continuous arm lift**
     - 5 kg

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

Operation is covered by the Operation of Ground Robots risk assessment (1450RA) and the Quadruped Demonstration risk assessment (2758RA), both associated with Basement 2, B2 029 (Robotics Lab) and CTP. Each requires digital sign-off by an Authorised User before operation. Access is restricted to trained and authorised personnel. A minimum 3 m clearance around the robot must be maintained during all operations.

- **Training:** Hands-on training is required before operation.
- **Risk assessment:** A task-appropriate risk assessment is required before use.

Safety & operating limits
-------------------------

.. warning::

   Intended for professional use in industrial, restricted, or controlled environments — not for collaborative applications involving physical interaction with humans. Prohibited uses include underwater/airborne applications, home environments, transporting persons/animals, and transporting hazardous materials. Key hazards: pinch/crush risks at arm joints and gripper; loss of stability with extended arm or heavy payloads (>5 kg at 0.5 m extension can unbalance Spot); unexpected motion during manipulation. Controls: maintain at least 3 m clearance, keep arm stowed when not manipulating, use slow speed when teaching or working near people. Storage: stow the arm, power off and remove the battery, store indoors at -20 °C to 45 °C (IP54); store batteries at ~50% state-of-charge for long-term storage.

**Environmental requirements**

- Restricted operating area

**Operational controls**

- Training required
- Risk assessment required
- PPE required
- Supervisor required
- Restricted operating area



Keywords
--------

``mobile robot`` · ``quadruped`` · ``ground robot`` · ``robotic arm`` · ``manipulation`` · ``inspection`` · ``indoor`` · ``outdoor`` · ``Spot`` · ``legged``


.. note::

   For current availability or details not recorded here, contact
   Samuel A. Prieto (sxp8070).
