# Equipment Images

## Naming Convention

Equipment images normally follow this naming pattern when a legacy inventory ID exists:
```
{legacy_id}_{equipment-slug}.{ext}
```

Records without a legacy ID use a stable descriptive slug, for example
`dgx-spark-nvidia.png`. The canonical selector is the equipment note's `image_filename` field in
the KINESIS vault; `equipment.json` and equipment RST pages are generated outputs.

### Examples:
- `99_spot-boston-dynamics.jpg` - Spot robot without arm
- `100_spot-arm.png` - Spot robot with arm
- `329_drone-matrice-300-dji.png` - Matrice 300 RTK drone
- `506_humanoid-g1-unitree.jpg` - G1 humanoid robot
- `507_h1-unitree.png` - H1 humanoid robot

## Image Categories

### Equipment Images (linked in equipment.json)
- `97_drone-mavic-pro-2-dji.png` - Drone - Mavic Pro 2 - DJI
- `99_spot-boston-dynamics.jpg` - Quadruped Robot - Spot - Boston Dynamics
- `100_spot-arm.png` - Quadruped Robot with Arm - Spot - Boston Dynamics
- `101_vantage-v16-vicon.png` - Motion Capture System - Vantage V16 - Vicon
- `102_goscan-3d-creaform.png` - 3D Scanner - Go!SCAN 3D - Creaform
- `103_focus-350s-faro.jpg` - 3D Scanner - Focus 350s plus - FARO
- `106_lbr-iiwa-kuka.png` - Robotic Arm - LBR iiwa 14 R820 - KUKA
- `107_robotic-gripper-3-finger-adaptive-robotiq.png` - Robotic Gripper - 3-Finger Adaptive - Robotiq
- `108_wiris-prosc-workswell.png` - Thermal/Visual Camera - Wiris ProSc - Workswell
- `109_wireless-radio-mpu5-persistent-systems.png` - Wireless Radio - MPU5 - Persistent Systems
- `329_drone-matrice-300-dji.png` - Drone - Matrice 300 RTK - DJI
- `367_hovermap-emesent.jpg` - LiDAR Mapping Payload - Hovermap ST - Emesent
- `398_power-supply-pvs10005-bk-precision.png` - Power Supply - PVS10005 - BK Precision
- `405_hyperspectral-camera.png` - Hyperspectral camera
- `442_event-camera-metavision-evk4-hd-prophesee.png` - Event Camera - Metavision EVK4 HD - Prophesee
- `445_rov-robotic-arm-alpha-5-reach-robotics.png` - ROV Robotic Arm - Alpha 5 - Reach Robotics
- `451_buggy-rbcar-robotnik.jpg` - Autonomous Buggy - RB-CAR - Robotnik
- `506_humanoid-g1-unitree.jpg` - Humanoid Robot - G1 - Unitree
- `507_h1-unitree.png` - Humanoid Robot - H1 - Unitree
- `517_defender-rov.png` - Underwater ROV - Defender - VideoRay
- `529_rov-exray-hydromea.png` - Underwater ROV - EXRAY - Hydromea
- `601_sv600-fluke.jpg` - Acoustic Imager - SV600 - Fluke
- `602_inspire-hand.jpg` - Dexterous Hand - RH56 - Inspire Robots
- `ai-workstation-lambda.jpg` - AI Workstation - Lambda
- `dgx-spark-nvidia.png` - AI Workstation - DGX Spark - NVIDIA

### General Site Images
- `hero.jpg` - Homepage hero banner
- `arena.jpg` - Arena facility showcase image (motion capture arena)
- `facility-arena-motion-capture.jpg` - Homepage Facilities showcase image (motion capture arena)
- `equipment.jpg` - Equipment showcase image
- `research.jpg` - Research showcase image
- `workspace.jpg` - Workspace showcase image
- `workspace-overview.jpg` - Main workspace overview image
- `Core-Technology-Platforms-lockup-DIGITAL-color.png` - NYU Abu Dhabi CTP logo

### Facility Images
- `facility-lipo-charging-station.jpg` - LiPo battery charging safety station
- `facility-battery-storage-cabinet.jpg` - Fireproof battery storage cabinet
- `facility-soldering-station.jpg` - Electronics soldering workspace
- `facility-dremel-station.jpg` - Precision tools and fabrication station
- `facility-fire-blanket.jpg` - Fire blanket and safety sign (two installed in lab)
- `facility-equipment-cabinet-outside.jpg` - Equipment storage cabinets (outside view)
- `facility-equipment-cabinet-inside.jpg` - Equipment storage cabinets (inside, labelled drawers)
- `facility-vicon-command-center.jpg` - Vicon command center with large monitor and KVM switch
- `facility-vicon-kvm-switch.jpg` - KVM switch for Vicon PC, Linux workstation, and auxiliary input

### Network & Infrastructure Images
- `network-kinesis-rack.jpg` - KINESIS CTP network rack (Cisco 48-port + 2x PoE switches)
- `network-kinesis-router.jpg` - KINESIS CTP main router
- `network-hermes-router.jpg` - Hermes arena wireless router
- `network-wired-ports.jpg` - Wired ethernet ports (blue = KINESIS CTP, red = NYUAD network)

### Computing Workstation Images
- `workstation-vicon-pc.jpg` - Vicon PC workstation
- `workstation-linux.jpg` - Linux workstation

## Adding New Equipment Images

1. Preserve the supplied source in the equipment record's canonical working-files
   `05_Media_models` folder.
2. Save the selected wiki-ready derivative in that same folder and duplicate it under
   `02_Equipment/_Shared_assets/Images`.
3. Copy the same derivative into this directory and set the matching vault equipment note's
   `image_filename` field.
4. Regenerate and validate the private wiki through `sync/equipment_to_wiki.py`; do not hand-edit
   `equipment.json` or generated equipment pages.

## Image Format Guidelines

- **Preferred format**: PNG for transparent product cutouts; JPG for contextual installation photos
- **Framing**: Tight subject crop with a small safety margin and no baked-in whitespace
- **Recommended size**: 800-2200px on the longest edge
- **File size**: Optimize when practical without degrading labels, edges, or transparency
- **Quality**: Preserve exact product geometry and model markings
