========
Vicon PC
========

.. figure:: ../../_static/images/workstation-vicon-pc.jpg
   :alt: Vicon PC Workstation
   :width: 60%
   :align: center

   Vicon PC Workstation

The Vicon PC is an Intel NUC 11 Enthusiast ("Phantom Canyon") mini PC dedicated to controlling the motion capture system. It serves as the central hub for arena operations, running Vicon Tracker and broadcasting position data to the Hermes network.

Role
----

The Vicon PC:

- Connects to all 24 Vicon cameras via two dedicated switches
- Runs Vicon Tracker software for real-time position capture
- Processes and broadcasts position data to the Hermes network
- Provides data recording and playback capabilities

Network Connectivity
--------------------

The Vicon PC is connected to three distinct networks:

1. **Vicon Camera Network** via 2 PoE switches

   - Switch 1: Cameras 1–12
   - Switch 2: Cameras 13–24
   - High-bandwidth dedicated connection for camera data

2. **Hermes Network** via wired Ethernet

   - Connected directly to the Hermes router via Ethernet
   - Broadcasts real-time position data to robots and drones in the arena
   - Researcher laptops connect to Hermes wirelessly

3. **KINESIS CTP Network** via wired Ethernet

   - General lab connectivity
   - File transfer and remote access

Hardware Specifications
-----------------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Model**
     - Intel NUC 11 Enthusiast Kit (NUC11PHKi7C, "Phantom Canyon")
   * - **CPU**
     - Intel Core i7-1165G7 (11th Gen Tiger Lake) — 4 cores / 8 threads, 2.8–4.7 GHz, 28W TDP
   * - **Integrated GPU**
     - Intel Iris Xe (96 EU)
   * - **Dedicated GPU**
     - NVIDIA GeForce RTX 2060 Mobile — 4 GB GDDR6
   * - **RAM**
     - 64 GB DDR4-3200 SO-DIMM *(to be confirmed)*
   * - **Storage**
     - 2 TB M.2 NVMe *(to be confirmed)*
   * - **Ethernet**
     - 1× 2.5 GbE (Intel i225)
   * - **Wi-Fi / BT**
     - Wi-Fi 6 (Intel AX201), Bluetooth 5.1
   * - **Ports**
     - 4× USB 3.0 Type-A, 2× USB 3.2 Gen 2, 2× Thunderbolt 4
   * - **Display out**
     - 2× HDMI 2.0b, 1× DisplayPort 1.4, up to 4 displays
   * - **Dimensions**
     - 227 × 145 × 40 mm, 1.4 kg

Software
--------

- **Vicon Tracker** — primary software for real-time robot/drone pose tracking and DataStream broadcast
- **Vicon Nexus** — biomechanics and gait analysis
- **Vicon Shogun** — animation and live performance capture
- **VAULT** — data management and session archiving

Data Management
---------------

- Vicon session data is saved locally on the Vicon PC by default
- Name sessions clearly, for example ``2026-05-01_Spot_Navigation_Test``
- Export important sessions to shared network storage or your own device after completion
- Delete old test sessions periodically to free disk space
- For long-term archival, export to C3D format and store on NYUAD research storage
