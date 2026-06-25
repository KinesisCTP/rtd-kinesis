============
Vicon System
============

The Vicon motion capture system provides high-precision position tracking for robots, drones, and other objects in the KINESIS CTP Arena.

The Vicon system consists of:

- 24 high-speed cameras
- 2 dedicated network switches, 12 cameras each
- Vicon PC running Tracker software
- Integration with Hermes wireless network

.. toctree::
   :maxdepth: 1
   :caption: Setup Guide

   arena-setup

How It Works
------------

1. **Capture**: 24 cameras capture reflective markers from multiple angles
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

- **Camera Network**: Two switches connecting 12 cameras each to Vicon PC
- **Hermes Network**: WiFi broadcast of position data from Vicon PC
- **KINESIS CTP Network**: General connectivity for data export and remote access

Using the Vicon System
----------------------

See :doc:`arena-setup` for detailed setup instructions.
