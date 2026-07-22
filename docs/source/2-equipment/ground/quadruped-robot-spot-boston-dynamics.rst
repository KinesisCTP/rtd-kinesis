.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: 04c98a0d-3984-44dd-8960-a9ef8abdfa6b

========================================
Quadruped Robot - Spot - Boston Dynamics
========================================

.. container:: equipment-kicker

   Boston Dynamics · Spot

.. figure:: ../../_static/images/99_spot-boston-dynamics.jpg
   :alt: Quadruped Robot - Spot - Boston Dynamics
   :class: equipment-page-image
   :figclass: equipment-page-figure
   :align: center

   Quadruped Robot - Spot - Boston Dynamics

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

The Boston Dynamics Spot is a legged, mobile ground robot used for remote inspection, data collection, and autonomous navigation in indoor and outdoor environments. It can be driven manually with a tablet controller or operated programmatically via the Spot API, and supports a variety of sensor and equipment payloads mounted on its back.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Standing dimensions**
     - L 1100 x W 500 x H 610 mm
   * - **Weight**
     - 33.8 kg
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

Typical workflows
-----------------

1. Remote teleoperation for indoor/outdoor inspection
2. Autonomous or semi-autonomous navigation with obstacle avoidance
3. Data collection with mounted sensors (cameras, LiDAR, thermal imagers)
4. Recording and replaying missions (Autowalk) with data capture actions
5. Payload-based inspection tasks using the Spot API

Software & dependencies
-----------------------

- Spot tablet controller app
- Spot API

Access, training & booking
--------------------------

Access restricted to trained and authorised personnel. Minimum 3 m clearance around the robot must be maintained during all operations.

- **Training:** Hands-on training is required before operation.
- **Risk assessment:** A task-appropriate risk assessment is required before use.

Safety & operating limits
-------------------------

.. warning::

   - Intended for professional use in industrial, restricted, or controlled environments; do not use for collaborative applications involving physical interaction with humans.
   - Do not use Spot in home environments, to transport persons or animals, or to transport hazardous materials.
   - Maintain at least 3 m clearance during all operations and use slow speed when working near people.
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

``mobile robot`` · ``quadruped`` · ``ground robot`` · ``inspection`` · ``indoor`` · ``outdoor`` · ``autonomous`` · ``Spot`` · ``legged``


.. include:: /_includes/contact-lab-manager.inc
