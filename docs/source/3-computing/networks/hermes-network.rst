==============
Hermes Network
==============

The Hermes Network is a dedicated wireless network for distributing real-time Vicon position data in the KINESIS CTP Arena. It is not a general-purpose robot-control, internet, or laboratory data network.

Purpose
-------

Hermes provides:

- Real-time Vicon position-data distribution from the Vicon PC to approved clients
- Low-latency connectivity for robots, drones, and computers only while they need Vicon data
- Isolation from ordinary laboratory traffic so Vicon delivery remains predictable

Do not use Hermes for internet access, general telemetry or control, file transfers,
software updates, or unrelated experiment traffic. Use the
:doc:`KINESIS CTP Network <kinesis-network>` for those purposes.

Security Notes
--------------

- Hermes is physically and logically isolated from the NYUAD campus network
- Only authorized Vicon client devices and users should connect, and only while Vicon data is required
- General robot control, internet access, file transfers, software updates, and unrelated traffic must use the KINESIS CTP network
- Contact the lab manager for access credentials
