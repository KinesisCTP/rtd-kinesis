============
Vicon System
============

The Vicon motion capture system provides high-precision position tracking for robots, drones, and other objects in the KINESIS CTP Arena.

The Vicon system consists of:

- 24 high-speed cameras in the physical inventory
- 2 interconnected dedicated network switches
- Intel NUC 11 Enthusiast Vicon PC running Tracker software
- Integration with Hermes wireless network

The current ``Kinesis.System`` configuration expects 23 cameras. After the 2026-07-10 host
cutover and a camera reboot, Tracker detected all 23 expected cameras. The difference from the
24-camera physical inventory remains an open reconciliation item.

.. toctree::
   :maxdepth: 1
   :caption: Setup Guide

   arena-setup

How It Works
------------

1. **Capture**: the active camera set captures reflective markers from multiple angles
2. **Processing**: Vicon PC reconstructs 3D positions in real-time
3. **Broadcast**: Position data is transmitted over Hermes network
4. **Control**: Robots/drones use position data for navigation and control

Specifications
--------------

- **Capture volume:** 17 m × 6.4 m × 8 m, full Arena
- **Cameras:** 24 × Vicon Vantage V16, 16 MP, IR, 850 nm strobe
- **Position accuracy:** Sub-millimeter
- **Update rate:** Up to 120 Hz, configurable
- **Marker type:** Retro-reflective spherical markers, various sizes
- **Data output:** Vicon DataStream SDK, VRPN, C3D export

Network Architecture
--------------------

The Vicon system's network architecture:

- **Camera Network**: Two interconnected PoE switches feeding one active host Ethernet link
- **Hermes Network**: WiFi broadcast of position data from Vicon PC
- **KINESIS CTP Network**: Wi-Fi connectivity for data export and remote access

Using the Vicon System
----------------------

See :doc:`arena-setup` for detailed setup instructions.
