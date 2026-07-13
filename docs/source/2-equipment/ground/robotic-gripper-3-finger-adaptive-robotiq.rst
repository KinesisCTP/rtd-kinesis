.. GENERATED FROM THE KINESIS VAULT — DO NOT EDIT THIS PAGE DIRECTLY.
.. equipment_id: e18fcb75-4bdc-4b54-a54e-8d573ecb68b3

=============================================
Robotic Gripper - 3-Finger Adaptive - Robotiq
=============================================

.. container:: equipment-kicker

   Robotiq · 3-Finger Adaptive


.. list-table:: At a glance
   :class: equipment-facts-table
   :widths: 32 68
   :header-rows: 0

   * - **Manufacturer**
     - Robotiq
   * - **Model**
     - 3-Finger Adaptive
   * - **Equipment class**
     - Robot manipulation
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

.. note::

   This record describes a managed component or accessory. Check the related equipment and
   system documentation before planning standalone use.

Overview
--------

The Robotiq 3-Finger Adaptive Gripper is a robotic end-effector designed to be mounted on a robotic arm for grasping, manipulating, and releasing objects of varying shapes and sizes. It supports multiple grasp modes (basic, wide, pinch, scissor) and is typically used in supervised lab conditions for grasping experiments and manipulation research.

Specifications
--------------

.. list-table::
   :class: equipment-spec-table
   :widths: 38 62
   :header-rows: 0

   * - **Mobility**
     - Robot-mounted
   * - **Operating environment**
     - Indoor

Typical workflows
-----------------

1. mounting the gripper on a robotic arm for grasping and manipulation experiments
2. selecting grasp mode (basic, wide, pinch, scissor) and tuning speed/force parameters
3. activating and controlling the gripper via robot integration or Robotiq User Interface
4. gripping, manipulating, and releasing test objects under supervised lab conditions

Software & dependencies
-----------------------

- Robotiq User Interface
- Modbus RTU
- Modbus TCP

Access, training & booking
--------------------------

Indoor operation on a level, non-slip floor. Requires a dedicated 24 V DC bench supply and Ethernet/fieldbus cabling routed along the robot harness.

- **Training:** Hands-on training is required before operation.
- **Risk assessment:** A task-appropriate risk assessment is required before use.

Safety & operating limits
-------------------------

.. warning::

   Primary hazards: pinch/crush points (fingers can exert up to 60 N), projectile risk from dropped/ejected objects during fast motion, entanglement, and electrical hazards from damaged 24 V DC SELV wiring. Controls: only trained personnel operate; keep hands/clothing clear while powered; verify mode/speed/force in teach mode before automated runs; use a certified 24 V DC supply with a 4 A fuse; inspect and strain-relieve cables; never connect to AC or modify wiring; eye protection required. Emergency shutdown: press robot E-stop or cut 24 V DC supply. Storage: power off, disconnect cables, store dry indoors away from dust/moisture and temperature extremes.

**Environmental requirements**

- Indoor only
- Tethered operation

**Operational controls**

- Supervisor required
- Risk assessment required
- Training required
- PPE required



Keywords
--------

``gripper`` · ``robotic gripper`` · ``manipulation`` · ``adaptive`` · ``3-finger`` · ``Robotiq`` · ``end effector``


.. note::

   For current availability or details not recorded here, contact
   Samuel A. Prieto (sxp8070).
