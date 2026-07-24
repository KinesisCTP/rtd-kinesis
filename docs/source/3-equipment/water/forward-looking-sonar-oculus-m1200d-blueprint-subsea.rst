.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: eceef530-e8c3-4fe3-ae7c-7a42ba91ae02

========================================================
Forward-Looking Sonar - Oculus M1200d - Blueprint Subsea
========================================================

.. container:: equipment-kicker

   Blueprint Subsea · Oculus M1200d


.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - Blueprint Subsea
   * - **Model**
     - Oculus M1200d
   * - **Equipment class**
     - Multibeam forward-looking sonar
   * - **Location**
     - C3.B2.029.E (KINESIS CTP)
   * - **Quantity**
     - 1
   * - **Status**
     - Active

.. note::

   This record describes a managed component or accessory. Check the related equipment and
   system documentation before planning standalone use.

Overview
--------

The Blueprint Subsea Oculus M1200d is a compact dual-frequency multibeam imaging sonar installed on the VideoRay Mission Specialist Defender. It provides a wide low-frequency navigation mode with up to 40 m range and a shorter-range high-frequency mode for detailed inspection imagery.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Sensing modalities**
     - Sonar
   * - **Sensor type**
     - dual-frequency multibeam imaging sonar
   * - **Maximum range**
     - 40 m
   * - **Minimum range**
     - 0.1 m
   * - **Field of view**
     - 130 °
   * - **Resolution**
     - 2.5 mm range resolution
   * - **Frame rate**
     - Up to 40 Hz
   * - **Interfaces**
     - 100BASE-T Ethernet
   * - **Power consumption**
     - 10-35 W
   * - **Operating temperature**
     - -5 to +35 °C
   * - **Additional specifications**
     - High-frequency maximum range: 10 m. Low-frequency beam: 130 x 20 degrees. High-frequency beam: 60 x 12 degrees.

Typical workflows
-----------------

1. Forward obstacle detection and navigation in limited visibility
2. Close-range underwater inspection and target identification
3. Locating and measuring submerged objects using acoustic imagery
4. Recording sonar imagery for post-mission review

.. note::

   These examples are an overview. Follow the current equipment manual and SOP,
   where available, together with the applicable risk assessment and training,
   for the complete procedure.

Software & dependencies
-----------------------

- Greensea Professional Workspace
- Greensea openfls
- Blueprint Subsea ViewPoint for Windows diagnostics


Safety & operating limits
-------------------------

.. warning::

   - Assess acoustic image quality only with the sonar face submerged and aimed at a target.
   - Keep the transducer face clean and unobstructed.
   - Do not modify firmware or advanced ViewPoint settings without first recording the current model, serial, firmware, network, Gain Assist, and Gamma configuration.

**Access and operational conditions**

- Installed as part of the VideoRay Defender system. Defender operator training, supervision, launch/recovery controls, and the current Defender SOP and risk assessment apply.

**Environmental limits**

- Operate only in the water conditions and depth limits stated in the equipment manual.
- Keep the sonar within its -5 °C to 35 °C operating range.
- Follow the Defender system's limits for dry operation, deployment, recovery, and storage.

**Operational controls**

- Supervisor required
- Use only while integrated with the VideoRay Defender system.


Related equipment & documentation
---------------------------------

- **Parent system:** :doc:`Underwater ROV - Defender - VideoRay </3-equipment/water/underwater-rov-defender-videoray>`

Keywords
--------

``sonar`` · ``multibeam`` · ``forward-looking sonar`` · ``imaging sonar`` · ``Oculus`` · ``M1200d`` · ``underwater`` · ``inspection`` · ``navigation`` · ``VideoRay Defender``


.. include:: /_includes/contact-lab-manager.inc
