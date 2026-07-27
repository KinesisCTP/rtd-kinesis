=========
Workspace
=========

The Workspace is the KINESIS CTP Lab's shared area for software development,
electronics, prototyping, equipment preparation, charging, storage, and
collaborative work. It contains the fixed work surfaces and support stations
used to prepare experiments before equipment enters the Arena.

.. figure:: ../_static/images/workspace.jpg
   :alt: KINESIS CTP Workspace with workbenches, storage, and mobile robots
   :width: 85%
   :align: center

   KINESIS CTP Workspace

Physical Space
--------------

.. list-table::
   :class: equipment-facts-table
   :widths: 30 70
   :header-rows: 0

   * - **Work surfaces**
     - Perimeter desks, shared tables, and dedicated technical workbenches
   * - **Computing and control**
     - Shared workstations and the Vicon Command Center
   * - **Charging**
     - Dedicated LiPo and controller-charging stations
   * - **Tools**
     - Soldering, rotary-tool, precision-tool, and general tool stations
   * - **Storage**
     - Labelled shelving, cabinets, drawers, and assigned floor positions
   * - **Lighting**
     - Adjustable smart lighting for general work and controlled experiments

The :ref:`KINESIS CTP Lab reference layout <main-lab-floorplans>` identifies the
fixed desks, tables, shelves, charging stations, tool areas, and command center.

Computing and Control
---------------------

Shared computers support motion capture, robotics development, AI workloads,
scanning, simulation, and data processing. Specifications, access information,
and operating guidance are maintained in
:doc:`Workstations </4-computing/workstations/index>`.

The Vicon Command Center sits at the boundary between the Workspace and Arena,
providing a protected position for experiment monitoring and motion-capture
control. See the :doc:`Arena <arena>` page for its location and role.

Use :doc:`Networks & Connectivity
</4-computing/networks/index>` for ordinary laboratory connectivity,
robot control, file transfers, software updates, and research traffic. The
:ref:`Hermes network <hermes-network>` is reserved for
real-time Vicon position-data distribution.

Charging Stations
-----------------

.. _lipo-battery-charging-station:

.. figure:: ../_static/images/facility-lipo-charging-station.jpg
   :alt: Designated LiPo battery charging station in the KINESIS CTP Workspace
   :width: 50%
   :align: center

   LiPo battery charging station (LC01)

The designated LiPo battery charging station, identified as **LC01** on the
reference layout, is the approved location for supervised charging with an
appropriate charger. It is a charging area, not a battery-storage location.

The controller charging station, **CS01**, is reserved for compatible
controllers and accessories. It does not replace LC01 when the applicable
battery procedure requires use of the LiPo charging station.

Battery inspection, charging, storage, quarantine, and disposal requirements
are summarized on the :doc:`Facilities Safety <safety>` page.

Storage and Shared Work Surfaces
--------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - .. image:: ../_static/images/facility-equipment-cabinet-outside.jpg
          :alt: Equipment storage cabinets in the KINESIS CTP Workspace
          :width: 100%
     - .. image:: ../_static/images/facility-equipment-cabinet-inside.jpg
          :alt: Labelled drawers inside a KINESIS CTP equipment cabinet
          :width: 100%
   * - *Equipment storage cabinets*
     - *Labelled storage drawers*

Shared cabinets, shelves, and drawers hold equipment accessories, cables,
chargers, adapters, mounting hardware, and other ancillary components.
Assigned storage locations are identified by equipment name or asset tag where
applicable. Work surfaces must be cleared after use, and all items returned to
their assigned locations in accordance with
General Policies.

Workshop Tools
--------------

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - .. image:: ../_static/images/facility-soldering-station.jpg
          :alt: Soldering station in the KINESIS CTP Workspace
          :width: 100%
     - .. image:: ../_static/images/facility-dremel-station.jpg
          :alt: Rotary and precision-tool station in the KINESIS CTP Workspace
          :width: 100%
   * - *Soldering station*
     - *Rotary and precision-tool station*

The soldering and rotary-tool area, **SD01**, supports electronics assembly,
rework, cutting, grinding, polishing, and other small fabrication tasks. The
general tool workbench, **TS01**, provides a separate surface for hand-tool and
equipment-preparation work.

Use these stations only for tasks covered by the applicable training, risk
assessment, operating instructions, attire, and PPE requirements. See
:doc:`Safety <safety>` and the relevant equipment documentation before work
begins.

.. important::

   Leave **SD01** and **TS01** clean, clear, and ready for the next user after
   every task. Remove components, offcuts, dust, and other debris; return tools
   and accessories to their assigned locations; and restore the unobstructed
   work surfaces shown in the photographs above.

.. _workspace-lighting-system:

Lighting System
---------------

Adjustable smart lighting covers both the Workspace and Arena. The two lighting
zones can be controlled from the installed wall switches or the Philips Hue
app, allowing colour and intensity to be adjusted for general work, recording,
and controlled experimental conditions.

The control labelled **Vicon Cameras** operates the motion-capture camera power
circuit rather than a lighting zone. Camera power requirements and shutdown
guidance are maintained in the
:doc:`Vicon System documentation </4-computing/vicon-system/index>`.

The round Philips Hue switch at the Vicon Command Center provides physical
control of the same camera power circuit. All four buttons are configured for
Vicon camera power control.

.. list-table::
   :class: lighting-control-comparison
   :widths: 50 50
   :header-rows: 0

   * - .. image:: ../_static/images/hue_app_dashboard.png
          :alt: Philips Hue dashboard for KINESIS CTP Lab lighting and Vicon power
          :width: 100%
     - .. image:: ../_static/images/facility-vicon-camera-power-switch.jpg
          :alt: Round four-button Philips Hue switch controlling Vicon camera power
          :width: 100%
   * - *KINESIS CTP Lab controls in the Philips Hue app*
     - *Four-button Vicon camera power switch at the Vicon Command Center*

Planning Workspace Work
-----------------------

- Review General Policies for access, authorization, equipment,
  battery, network, and data requirements.
- Check the :doc:`equipment index </3-equipment/index>` and the relevant
  equipment page for training, risk-assessment, attire, PPE, and operating
  requirements.
- Keep desks, walkways, emergency equipment, charging stations, and assigned
  storage locations clear.
- Move active robot or drone testing into the Arena whenever the activity
  requires its enclosed operating volume or safety controls.
