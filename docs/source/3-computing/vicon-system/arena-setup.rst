=================
Arena Setup Guide
=================

Prerequisites
-------------

Before starting:

- Complete Vicon system training
- Understand your robot/drone's network configuration
- Have appropriate reflective markers
- Coordinate with lab personnel for Arena access

Overview of the System
----------------------

The Arena uses the Hermes wireless network to connect:

1. Vicon PC, which broadcasts position data
2. Your robot/drone, which receives position data
3. Your control laptop, which sends commands

Step-by-Step Setup
------------------

Prepare Your Robot/Drone
^^^^^^^^^^^^^^^^^^^^^^^^

**Physical Setup:**

- Attach reflective markers in a unique configuration
- Ensure markers are visible from multiple camera angles
- Secure all components to prevent marker movement

**Network Configuration:**

- Configure your device to connect to Hermes WiFi
- Set up to receive Vicon position data broadcast
- Test network connectivity before entering Arena

Configure Vicon Tracker
^^^^^^^^^^^^^^^^^^^^^^^

**Create Object Definition:**

- Launch Vicon Tracker on the Vicon PC
- Create a new object with your marker configuration
- Name the object clearly, for example ``Spot_Robot_01``

**Calibration:**

- Place your robot/drone in the capture volume
- Verify all markers are detected
- Check for marker swap or occlusion issues

Connect to Hermes Network
^^^^^^^^^^^^^^^^^^^^^^^^^

**On Your Robot/Drone:**

.. code-block:: bash

   # Example configuration; adapt to your system
   nmcli device wifi connect Hermes password [PASSWORD]

**On Your Control Laptop:**

- Connect to Hermes WiFi
- Verify you can reach your robot/drone
- Verify you can receive Vicon data stream

Receive Position Data
^^^^^^^^^^^^^^^^^^^^^

The Vicon PC broadcasts position data in real-time. Your robot/drone needs to:

- Subscribe to the data stream
- Parse position and orientation
- Integrate into control loop

Test in Arena
^^^^^^^^^^^^^

**Safety First:**

- Start with stationary tests
- Verify position data accuracy
- Test failsafe behaviors
- Have emergency stop ready

**Flight/Movement Test:**

- Begin with slow, controlled movements
- Monitor position data quality
- Check for latency issues
- Verify control responsiveness

Common Issues
-------------

**Marker Not Detected:**

- Check lighting conditions
- Verify marker reflectivity
- Adjust camera exposure if needed
- Ensure no occlusion

**Network Issues:**

- Verify Hermes connection
- Check firewall settings
- Confirm correct IP addresses
- Test latency

**Position Data Quality:**

- Recalibrate if needed
- Check for marker swap
- Verify rigid body definition
- Monitor system performance

Data Recording
--------------

To record your session:

1. Set recording parameters in Vicon Tracker
2. Start recording before beginning operations
3. Stop and save after completion
4. Export data in desired format

Best Practices
--------------

- Test thoroughly before live demonstrations
- Always have a safety observer
- Start simple, increase complexity gradually
- Document your setup for future reference
- Clean up after your session
