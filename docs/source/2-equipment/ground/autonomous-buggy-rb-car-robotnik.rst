====================================
Autonomous Buggy - RB-CAR - Robotnik
====================================

.. figure:: ../../_static/images/451_buggy-rbcar-robotnik.jpg
   :alt: Robotnik RB-CAR Autonomous Buggy
   :width: 40%
   :align: center

   Robotnik RB-CAR Autonomous Buggy

.. admonition:: Quick Info
   :class: equipment-info

   - **Manufacturer:** Robotnik
   - **Model:** RB-CAR
   - **Category:** Ground Robot
   - **Location:** C3.B2.029.E (KINESIS CTP)
   - **Contact:** Samuel A. Prieto (sxp8070)

Overview
--------

The Robotnik RB-CAR is a 4x4 electric research buggy (based on a Polaris RANGER EV chassis) with servo-actuated steering and traction controlled by an onboard computer for manual driving, teleoperation, or autonomous operation. It is used for autonomous navigation R&D, perception testing, and data collection in controlled indoor lab areas and approved outdoor campus test roads.

Capabilities
------------

**Outputs:**

- rosbag

- **Mobility:** wheeled
- **Indoor Outdoor:** both
- **Max Speed Ms:** 5.56

**Sensing Modality:**

- lidar
- gps


Typical Workflow
----------------

1. pre-drive checks and safety system reset (local/remote E-stop and handbrake interlock)
2. manual driving with steering wheel and pedals
3. teleoperation using gamepad (with remote E-stop as safety device)
4. autonomous navigation research and perception testing in controlled areas
5. data collection using onboard sensors (e.g., lidar, GPS) via ROS
6. battery charging in a ventilated area after use

Software Requirements
---------------------

- ROS
- Ubuntu 20.04
- Safety Designer (Windows)

Availability Notes
------------------

Use restricted to trained and authorised operators. Outdoor operation approved only on the Service Road behind campus and the Ring Road (Amber Zones). Mandatory: do not operate during peak traffic hours (07:00–09:00 and 15:00–17:00); notify the DCS Command Centre before each experiment; minimum two researchers at all times (one designated driver with a valid UAE licence and one perimeter watcher); deploy warning signs; install and activate a warning strobe light; maximum speed 20 km/h; do not operate in low-visibility conditions (fog or sandstorm).

Training Required
-----------------

Yes - hands-on training is required before operating this equipment.

Risk Assessment
---------------

A risk assessment is required before using this equipment.

Safety and Operational Notes
-----------------------------

.. warning::

   - Keep a clear perimeter and do not allow anyone near the vehicle while motor drives are enabled
   - Always keep an operator seated when the vehicle is powered and safety is restarted
   - Use seat belts
   - Do not rely on laser stop at higher speeds (configured for low-speed auto operation)
   - Keyswitch must be OFF and main power isolated before accessing the rear control cabinet (qualified personnel only).
   - Battery system is high-current 48 V DC lead-acid
   - Charge only with the provided charger and only in a well-ventilated area with hood/doors open
   - Do not cover while charging
   - Avoid wet conditions and do not sprinkle water/oil on the robot or charging cord.
   - Hot components (motor/controller/brake discs) can exceed 80°C
   - Enforce cool-down and use gloves for work inside the rear electronics bay.

**Safety Requirements:**

- Training Required
- Restricted Area
- Ppe Required
- Two Person Operation
- Risk Assessment Required

Tags
----

``autonomous vehicle``  
``ground robot``  
``self-driving``  
``car``  
``outdoor``  
``ROS``  
``wheeled``  
``research platform``  

.. note::

   For more detailed information, contact Samuel A. Prieto (sxp8070).
