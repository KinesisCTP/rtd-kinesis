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
   :figclass: equipment-page-figure
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

   * - **Mobility**
     - Wheeled
   * - **Dimensions**
     - 2727 x 1444 x 2082 (L x W x H) mm
   * - **Weight**
     - 800 kg
   * - **Passenger capacity**
     - 2
   * - **Payload**
     - 227 kg
   * - **Manufacturer maximum speed**
     - 9.72 m/s
   * - **Lab operational speed limit**
     - 5.56 m/s
   * - **Maximum range**
     - 70 km
   * - **Maximum slope**
     - 30 %
   * - **Towing capacity**
     - 680 kg
   * - **Battery charge capacity**
     - 240 Ah
   * - **Battery voltage**
     - 48 V
   * - **Ingress protection**
     - IP54
   * - **Operating environment**
     - Indoor and outdoor
   * - **Sensing modalities**
     - LiDAR, GPS
   * - **Output formats**
     - Rosbag

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

   - Keep a clear perimeter and do not allow anyone near the vehicle while the motor drives are enabled.
   - Keep an operator seated whenever the vehicle is powered and safety has been restarted, and use the seat belts.
   - Do not rely on the laser stop at higher speeds; it is configured for low-speed autonomous operation.
   - Set the keyswitch to OFF and isolate main power before qualified personnel access the rear control cabinet.
   - The battery system is high-current 48 V DC lead-acid; use only the provided charger and never cover the battery or charger while charging.
   - Motor, controller, and brake components can exceed 80 °C; enforce a cool-down period before authorised maintenance inside the rear electronics bay.

**Approved operating area**

- KINESIS CTP Lab and approved KINESIS controlled test areas.
- The approved Service Road behind campus and Ring Road Amber Zones, subject to the operating restrictions listed on this page.

Operations outside the approved area require a submitted and approved
`Robotics Review Committee (RRC) Mission Review Form <https://docs.google.com/forms/d/e/1FAIpQLSdj0OyfnCpAIcmQqXW_oNY_B6kJzBgunmGXpXxznvEGFAQ2Ew/viewform>`_ before the experiment begins.

**Environmental limits**

- Keep the equipment dry; do not operate it in rain, spray, or wet conditions.
- Charge only in a well-ventilated area with the hood or doors open.
- Do not operate in fog, sandstorms, or other low-visibility conditions.

**Required attire and conditional PPE**

- Long pants.
- Closed-toed shoes.
- Protective gloves are required only for authorised maintenance inside the isolated rear electronics bay after hot components have cooled sufficiently for the task.

**Operational controls**

- Training required
- Two-person operation
- Risk assessment required



Keywords
--------

``autonomous vehicle`` · ``ground robot`` · ``self-driving`` · ``car`` · ``outdoor`` · ``ROS`` · ``wheeled`` · ``research platform``


.. note::

   For current availability or details not recorded here, contact
   Samuel A. Prieto (sxp8070).
