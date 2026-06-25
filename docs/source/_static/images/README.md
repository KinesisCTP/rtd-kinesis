# Equipment Images

## Naming Convention

Equipment images follow this naming pattern:
```
{legacy_id}_{equipment-slug}.{ext}
```

### Examples:
- `99_spot-boston-dynamics.jpg` - Spot robot without arm
- `100_spot-arm.png` - Spot robot with arm
- `329_drone-matrice-300-dji.png` - Matrice 300 RTK drone
- `506_humanoid-g1-unitree.jpg` - G1 humanoid robot
- `507_h1-unitree.png` - H1 humanoid robot

## Image Categories

### Equipment Images (linked in equipment.json)
- `99_spot-boston-dynamics.jpg` - Quadruped Robot - Spot - Boston Dynamics
- `100_spot-arm.png` - Quadruped Robot with Arm - Spot - Boston Dynamics
- `101_vantage-v16-vicon.jpg` - Motion Capture System - Vantage V16 - Vicon
- `102_goscan-3d-creaform.jpg` - 3D Scanner - Go!SCAN 3D - Creaform
- `103_focus-350s-faro.jpg` - 3D Scanner - Focus 350s plus - FARO
- `106_lbr-iiwa-kuka.jpg` - Robotic Arm - LBR iiwa 14 R820 - KUKA
- `108_wiris-prosc-workswell.jpg` - Thermal/Visual Camera - Wiris ProSc - Workswell
- `329_drone-matrice-300-dji.png` - Drone - Matrice 300 RTK - DJI
- `367_hovermap-emesent.jpg` - LiDAR Mapping Payload - Hovermap ST - Emesent
- `405_hyperspectral-camera.jpg` - Hyperspectral camera
- `451_buggy-rbcar-robotnik.jpg` - Autonomous Buggy - RB-CAR - Robotnik
- `506_humanoid-g1-unitree.jpg` - Humanoid Robot - G1 - Unitree
- `507_h1-unitree.png` - Humanoid Robot - H1 - Unitree
- `517_defender-rov.png` - Underwater ROV - Defender - VideoRay
- `529_rov-exray-hydromea.png` - Underwater ROV - EXRAY - Hydromea
- `601_sv600-fluke.jpg` - Acoustic Imager - SV600 - Fluke
- `602_inspire-hand.jpg` - Dexterous Hand - RH56 - Inspire Robots

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

1. Name the image using the convention: `{legacy_id}_{equipment-slug}.{ext}`
2. Place the image in this directory
3. Update `equipment.json` by adding the `image_filename` field to the corresponding equipment entry:
   ```json
   {
     "legacy_id": 99,
     "name": "Equipment Name",
     "image_filename": "99_equipment-name.jpg"
   }
   ```

## Image Format Guidelines

- **Preferred format**: JPG for photos, PNG for graphics with transparency
- **Recommended size**: 800-1200px wide
- **File size**: Keep under 500KB when possible
- **Quality**: High quality but web-optimized
