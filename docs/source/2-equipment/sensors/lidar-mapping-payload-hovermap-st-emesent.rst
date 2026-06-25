=============================================
LiDAR Mapping Payload - Hovermap ST - Emesent
=============================================

.. figure:: ../../_static/images/367_hovermap-emesent.jpg
   :alt: Emesent Hovermap ST LiDAR Mapping Payload
   :width: 40%
   :align: center

   Emesent Hovermap ST LiDAR Mapping Payload

.. admonition:: Quick Info
   :class: equipment-info

   - **Manufacturer:** Emesent
   - **Model:** Hovermap ST
   - **Category:** 3D Scanning
   - **Location:** C3.B2.029.E (KINESIS CTP)
   - **Contact:** Samuel A. Prieto (sxp8070)

Overview
--------

The Emesent Hovermap ST is a mobile, spinning 360° LiDAR mapping payload that captures 3D point clouds while using onboard SLAM to localise itself in GPS-denied environments. It can be operated handheld, mounted to a robot, or flown under compatible drones to map indoor, outdoor, and underground spaces for surveying and digital-twin generation.

Capabilities
------------

- **Mobility:** ['handheld', 'robot-mount', 'drone-mount']
- **Range Max M:** 100
- **Range Min M:** 0.5
- **Indoor Outdoor:** both
- **Points Per Sec:** 300000

**Sensing Modality:**

- lidar
- rgb


Typical Workflow
----------------

1. Handheld walking scans for indoor mapping
2. Robot-mounted mapping in GPS-denied environments
3. Drone-mounted mapping (indoor, underground, and outdoor asset scans)
4. Processing and merging scans into dense point clouds in Emesent Aura

Software Requirements
---------------------

- Emesent Commander
- Emesent Aura

Availability Notes
------------------

Operations occur mainly inside the KINESIS CTP Lab with occasional outdoor field demonstrations. Only trained operators may connect power, start scans, or mount the unit on drones or vehicles.

Training Required
-----------------

Yes - hands-on training is required before operating this equipment.

Risk Assessment
---------------

A risk assessment is required before using this equipment.

Safety and Operational Notes
-----------------------------

.. warning::

   - Power from an external 12–54 V DC source
   - Scans typically <35 minutes, data downloaded to USB.
   - Hazards: electrical shock from damaged leads/connectors (inspect before use, only trained operators connect/disconnect)
   - Moving parts from the continuously rotating sensor head (keep hands/hair/clothing clear
   - Use protective cage for handheld use)
   - Class 1 eye-safe lasers (do not open sealed optical enclosure
   - Avoid staring into aperture at close range)
   - Dropped-load risk when handheld or drone-mounted (~1.8 kg).
   - IP65 rated but not recommended in rain or fog
   - Maintain ≥10 m from elevated EMI sources
   - Operating temperature -10 °C to 45 °C.
   - Emergency shutdown: hold power button >10 s if frozen, then disconnect battery once LEDs are dark.
   - Storage: indoors dry at 10–30 °C in padded case
   - Fit protective cap
   - Disconnect battery.
   - PPE: long pants, closed-toed shoes.

**Environmental Requirements:**

- No Wet
- Tethered Operation

**Safety Requirements:**

- Training Required
- Risk Assessment Required
- Ppe Required

**Software License:** Required

Tags
----

``lidar``  
``3d scanning``  
``UAV mapping``  
``SLAM``  
``drone-mount``  
``indoor``  
``outdoor``  
``point cloud``  
``Hovermap``  
``mine mapping``  

.. note::

   For more detailed information, contact Samuel A. Prieto (sxp8070).
