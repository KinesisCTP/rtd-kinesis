.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: a8e767a0-0d13-4f27-ac77-6415617a0e49

=======================================
Power Supply - PVS10005 - B&K Precision
=======================================

.. container:: equipment-kicker

   B&K Precision · PVS10005

.. figure:: ../../_static/images/398_power-supply-pvs10005-bk-precision.png
   :alt: Power Supply - PVS10005 - B&K Precision
   :class: equipment-page-image
   :figclass: equipment-page-figure
   :align: center

   Power Supply - PVS10005 - B&K Precision

.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - B&K Precision
   * - **Model**
     - PVS10005
   * - **Equipment class**
     - Power supply
   * - **Location**
     - C3.B2.029.E (KINESIS CTP)
   * - **Quantity**
     - 1
   * - **Status**
     - Active


Overview
--------

The B&K Precision PVS10005 is a programmable, single-output high-voltage DC power supply providing 0–1000 V, 0–5 A, and up to 5000 W. Its fixed output range does not exchange unused voltage capacity for current above 5 A. It supports CV/CC regulation, programmable protection, adjustable slopes and list sequences, remote control, and solar-array simulation.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Configuration**
     - Single programmable DC output with a fixed 1000 V / 5 A range
   * - **Maximum voltage**
     - 1,000 V
   * - **Maximum current**
     - 5 A
   * - **Maximum power**
     - 5,000 W
   * - **Regulation modes**
     - CV, CC
   * - **Programming / readback resolution**
     - 0.1 V / 0.1 mA
   * - **Ripple / noise**
     - ≤100 mVrms / ≤600 mVpp voltage; 10 mA current
   * - **Remote-sense compensation**
     - 10 V
   * - **Interfaces**
     - Analog programming, USB, RS-232, RS-485, GPIB, Ethernet
   * - **Networking**
     - SCPI over supported remote interfaces
   * - **Power input**
     - 170–265 VAC single-phase, 47–63 Hz; output derated 10% below 190 VAC; 5800 VA maximum
   * - **Dimensions**
     - 420 x 88 x 532 mm
   * - **Mobility**
     - Fixed
   * - **Weight**
     - 14.6 kg
   * - **Operating temperature**
     - 0 to 40 °C
   * - **Operating environment**
     - Indoor
   * - **Additional specifications**
     - OVP, OCP, OPP, CV-to-CC, and CC-to-CV protection; ≤0.5 ms transient response; 90% typical efficiency and 0.99 power factor; nine 100-step list programs; built-in storage for 16 solar-array I-V curves; parallel operation up to 50 units, with B&K consultation advised above ten units.

Typical workflows
-----------------

1. High-voltage DC testing up to 1000 V and 5 A
2. Motor-inverter testing
3. Solar-array simulation and solar-inverter or MPPT validation
4. Bench and ATE use for research, design verification, and production test
5. Programmable ramp, timer, or list/step testing in CV or CC mode
6. Remote control and data logging over supported interfaces

.. note::

   These examples are an overview. Follow the current equipment manual and SOP,
   where available, together with the applicable risk assessment and training,
   for the complete procedure.



Safety & operating limits
-------------------------

.. warning::

   - Hazardous voltages can exist at the output and load connections because this supply is rated above 40 V. Ensure that the load and its connections have no accessible live parts.
   - Turn the supply off before connecting or changing output wiring. Size load wiring for the maximum continuous short-circuit output current, and use insulation rated above the supply's maximum output voltage.
   - Use the supplied, correctly rated AC power assembly and maintain protective earth. AC-source wiring, connection, or modification must be performed by qualified personnel.
   - OVP, OCP, OPP, CV-to-CC, and CC-to-CV protection are disabled by factory default; set protections appropriate to the DUT before enabling the output.
   - Do not remove covers, disassemble the case, or attempt internal fuse replacement. Internal service is restricted to qualified authorized personnel, and dangerous internal voltages may remain after power is removed.
   - If the instrument is damaged or contaminated, remove it from service, label it not to be operated, and arrange service through B&K Precision.

**Access and operational conditions**

- Equipment-specific training and SOP review are mandatory before operation. "High Voltage" signage must be posted whenever the supply is in use.

**Approved operating area**

- A designated electrical workbench inside the KINESIS CTP Lab.

**Environmental limits**

- Operate indoors only.
- Keep the equipment dry; do not operate it in rain, spray, or wet conditions.
- Use and handle the equipment in a clean, low-dust environment.
- Operate indoors in a Pollution Degree 2 environment from 0–40 °C at no more than 90% relative humidity, non-condensing.
- Storage temperature is −40–85 °C.
- Maintain at least 25 mm clearance around sides containing air inlet or exhaust ports; do not operate in direct sunlight or where cooling airflow is restricted.
- Do not operate around corrosive, noxious, or flammable fumes, gases, vapors, chemicals, or finely divided particulates, or where liquid spill or condensation is possible.



Keywords
--------

``power supply`` · ``electronics`` · ``bench equipment`` · ``precision`` · ``indoor``


.. include:: /_includes/contact-lab-manager.inc
