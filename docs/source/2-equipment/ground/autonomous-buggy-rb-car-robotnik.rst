.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: 863085cf-39f1-490e-90f5-e2a55823835e

====================================
Autonomous Buggy - RB-CAR - Robotnik
====================================

.. container:: equipment-kicker

   Robotnik · RB-CAR

.. figure:: ../../_static/images/451_buggy-rbcar-robotnik.jpg
   :alt: Autonomous Buggy - RB-CAR - Robotnik
   :class: equipment-page-image
   :align: center

   Autonomous Buggy - RB-CAR - Robotnik

.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - Robotnik
   * - **Model**
     - RB-CAR
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

The Robotnik RB-CAR is a 4x4 electric research buggy (based on a Polaris RANGER EV chassis) with servo-actuated steering and traction controlled by an onboard computer for manual driving, teleoperation, or autonomous operation. It is used for autonomous navigation R&D, perception testing, and data collection in controlled indoor lab areas and approved outdoor campus test roads.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Output formats**
     - Rosbag
   * - **Mobility**
     - Wheeled
   * - **Maximum speed**
     - 5.56 m/s
   * - **Operating environment**
     - Indoor and outdoor
   * - **Sensing modalities**
     - LiDAR, GPS

Typical workflows
-----------------

1. pre-drive checks and safety system reset (local/remote E-stop and handbrake interlock)
2. manual driving with steering wheel and pedals
3. teleoperation using gamepad (with remote E-stop as safety device)
4. autonomous navigation research and perception testing in controlled areas
5. data collection using onboard sensors (e.g., lidar, GPS) via ROS
6. battery charging in a ventilated area after use

Software & dependencies
-----------------------

- ROS
- Ubuntu 20.04
- Safety Designer (Windows)

Access, training & booking
--------------------------

Use restricted to trained and authorised operators. Outdoor operation approved only on the Service Road behind campus and the Ring Road (Amber Zones). Mandatory: do not operate during peak traffic hours (07:00–09:00 and 15:00–17:00); notify the DCS Command Centre before each experiment; minimum two researchers at all times (one designated driver with a valid UAE licence and one perimeter watcher); deploy warning signs; install and activate a warning strobe light; maximum speed 20 km/h; do not operate in low-visibility conditions (fog or sandstorm).

- **Training:** Hands-on training is required before operation.
- **Risk assessment:** A task-appropriate risk assessment is required before use.

Safety & operating limits
-------------------------

.. warning::

   Keep a clear perimeter and do not allow anyone near the vehicle while motor drives are enabled; always keep an operator seated when the vehicle is powered and safety is restarted; use seat belts; do not rely on laser stop at higher speeds (configured for low-speed auto operation); keyswitch must be OFF and main power isolated before accessing the rear control cabinet (qualified personnel only). Battery system is high-current 48 V DC lead-acid; charge only with the provided charger and only in a well-ventilated area with hood/doors open; do not cover while charging; avoid wet conditions and do not sprinkle water/oil on the robot or charging cord. Hot components (motor/controller/brake discs) can exceed 80°C; enforce cool-down and use gloves for work inside the rear electronics bay.

**Operational controls**

- Training required
- Restricted operating area
- PPE required
- Two-person operation
- Risk assessment required



Keywords
--------

``autonomous vehicle`` · ``ground robot`` · ``self-driving`` · ``car`` · ``outdoor`` · ``ROS`` · ``wheeled`` · ``research platform``


.. note::

   For current availability or details not recorded here, contact
   Samuel A. Prieto (sxp8070).
