.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: 6d14d3a9-820d-4940-afba-fba4b0b2a57e

=============================================
LiDAR Mapping Payload - Hovermap ST - Emesent
=============================================

.. container:: equipment-kicker

   Emesent · Hovermap ST

.. figure:: ../../_static/images/367_hovermap-emesent.jpg
   :alt: LiDAR Mapping Payload - Hovermap ST - Emesent
   :class: equipment-page-image
   :figclass: equipment-page-figure
   :align: center

   LiDAR Mapping Payload - Hovermap ST - Emesent

.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - Emesent
   * - **Model**
     - Hovermap ST
   * - **Equipment class**
     - 3D Scanning
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

The Emesent Hovermap ST is a mobile, spinning 360° LiDAR mapping payload that captures 3D point clouds while using onboard SLAM to localise itself in GPS-denied environments. It can be operated handheld, mounted to a robot, or flown under compatible drones to map indoor, outdoor, and underground spaces for surveying and digital-twin generation.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Sensing modalities**
     - LiDAR, RGB
   * - **Capture rate**
     - Up to 300,000 points/s single-return; up to 600,000 points/s dual-return
   * - **Minimum range**
     - 0.4 m
   * - **Maximum range**
     - 100 m
   * - **Distance accuracy**
     - ±30 mm
   * - **Mapping accuracy**
     - ±20 mm general; ±15 mm typical indoor and underground
   * - **Field of view**
     - 360 x 290 °
   * - **Ingress protection**
     - IP65
   * - **Storage**
     - 512 GB (approximately 8 hours of sensor data)
   * - **Interfaces**
     - USB 3.0
   * - **Mobility**
     - Handheld, Robot-mounted, Drone-mount
   * - **SLAM capable**
     - Yes
   * - **Operating environment**
     - Indoor and outdoor
   * - **Weight**
     - 1.6 kg
   * - **Output formats**
     - .las, .laz, .ply, .dxf, .e57

Typical workflows
-----------------

1. Handheld walking scans for indoor mapping
2. Robot-mounted mapping in GPS-denied environments
3. Drone-mounted mapping (indoor, underground, and outdoor asset scans)
4. Processing and merging scans into dense point clouds in Emesent Aura

.. note::

   These examples are an overview. Follow the current equipment manual and SOP,
   where available, together with the applicable risk assessment and training,
   for the complete procedure.

Software & dependencies
-----------------------

- Emesent Commander
- Emesent Aura


Safety & operating limits
-------------------------

.. warning::

   - Use an approved external 12–54 V DC power source and inspect leads and connectors before use; only trained operators may connect or disconnect power.
   - Keep hands, hair, and clothing clear of the continuously rotating sensor head, and use the protective cage for handheld operation.
   - The unit contains Class 1 lasers; never open the sealed optical enclosure or stare into the aperture at close range.
   - Control the approximately 1.6 kg dropped-load risk during handheld, robot-mounted, or drone-mounted operation.
   - If the unit freezes, hold the power button for more than 10 seconds and disconnect the battery only after the LEDs are dark.
   - For storage, disconnect the battery and fit the protective cap before placing the unit in its padded case.

**Access and operational conditions**

- Operations occur mainly inside the KINESIS CTP Lab with occasional outdoor field demonstrations. Only trained operators may connect power, start scans, or mount the unit on drones or vehicles.

**Environmental limits**

- Keep the equipment dry; do not operate it in rain, spray, or wet conditions.
- Do not operate in rain or fog, despite the IP65 enclosure rating.
- Operate at -10 °C to 45 °C and maintain at least 10 m separation from elevated electromagnetic-interference sources.
- Store dry indoors at 10–30 °C in the padded case.

**Operational controls**

- Plan, route, and supervise the tether or cable throughout operation.

- **Software licence:** Required.

Related equipment & documentation
---------------------------------

- **Compatible equipment:** :doc:`Drone - Matrice 300 RTK - DJI </3-equipment/aerial/drone-matrice-300-rtk-dji>`
- **Compatible equipment:** :doc:`Quadruped Robot - Spot - Boston Dynamics </3-equipment/ground/quadruped-robot-spot-boston-dynamics>`
- **Compatible equipment:** :doc:`Quadruped Robot with Arm - Spot - Boston Dynamics </3-equipment/ground/quadruped-robot-with-arm-spot-boston-dynamics>`

Keywords
--------

``lidar`` · ``3d scanning`` · ``UAV mapping`` · ``SLAM`` · ``drone-mount`` · ``indoor`` · ``outdoor`` · ``point cloud`` · ``Hovermap`` · ``mine mapping``


.. include:: /_includes/contact-lab-manager.inc
