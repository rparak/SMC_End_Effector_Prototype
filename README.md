# SMC Industrial Automation: End-Effector Prototypes

## Requirements:

**Software (optional):**

```bash
Autodesk Inventor 2023 (3D Modeling for Mechanical Design), PrusaSlicer (3D Printing), Blender
```

## Project Description:

The project demonstrates the creation of several modular end-effector  prototypes for robotic arms (ABB IRB 120, ABB IRB 14000 YuMi, Universal Robots UR3) as well as the creation of a 3D Viewpoint to better understand the Tool Center Point (TCP) of robots in 3D space. The modularity of end-effectors consist in their easy adaptability to a different type of robot by changing one part rather than the whole concept. The individual parts that make up the construction of each end-effector were created using 3D printing (using PLA material).

The repository contains 3D models of individual components and a Blender project for easy integration into the robot simulation model. Inside the blender file are prototypes of end-effectors with origins, position/rotation, etc. with the corresponding script in Python programming language.

Images with demonstrations on real robots can be found in the text below

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/SMC_EE_Series.png" width="800" height="500">
</p>

## Project Hierarchy:

**Repositary [/Data_Converter/]:**
```bash

[/Blender/]
Description:
  Blender project with corresponding Python script and 3D prototype models.
    
[/SMC_EE_*/]
Description:
    End-effectors created using SMC Industrial automation products.
    
[/ABB_EE_SmartGripper_SMC_Vacuum/]
Description:
    Smart grippers of the ABB company extended with SMC vacuum suction cups.
   
[/RealSense_D435i_+_Holder/]
Description:
    RealSense 3D camera system mount for attachment to a robotic arm.
    
[/Viewpoint/]
Description:
    3D Viewpoint to better understand the Tool Center Point (TCP) of robots in 3D space.
    
```

## Catalogue of prototypes:

**SMC Magnetic Gripper:**

|          | Weight [kg] | Position [m] | Orientation [-] |
| :------: | :-----------: | :----------: | :-------------: |
| EE_SMC_MHM_ABB_IRB_120_001 | 0.710           | [0.0, 0.0, 0.2177] | [1.0, 0.0, 0.0, 0.0] |
| EE_SMC_MHM_Universal_Robots_UR3_001 | 0.720           | [0.0, 0.0, 0.2177] | [1.0, 0.0, 0.0, 0.0] |

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/EE_SMC_MHM.png" width="500" height="300">
</p>

Product Link: [SMC (MHM-X6400)](https://www.smc.eu/en-eu/products/magnetic-gripper-mhm-x6400~138779~cfg?partNumber=MHM-32D1-X6400)

**SMC Non-contact Gripper, Cyclone Type:**

|          | Weight [kg] | Position [m] | Orientation [-] |
| :------: | :-----------: | :----------: | :-------------: |
| EE_SMC_XT661_2A_ABB_IRB_120_001 | 0.110           | [0.0, 0.0, 0.1765] | [1.0, 0.0, 0.0, 0.0] |
| EE_SMC_XT661_2A_Universal_Robots_UR3_001 | 0.120           | [0.0, 0.0, 0.1765] | [1.0, 0.0, 0.0, 0.0] |

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/EE_SMC_XT661_2A.png" width="500" height="300">
</p>

Product Link: [SMC (XT661-2A-R)](https://www.smc.eu/en-eu/products/cyclone-type-xt661~128119~cfg?partNumber=XT661-2A-R)

**SMC Non-contact Gripper, Bernoulli Type:**

|          | Weight [kg] | Position [m] | Orientation [-] |
| :------: | :-----------: | :----------: | :-------------: |
| EE_SMC_XT661_4C_ABB_IRB_120_001 | 0.295           | [0.0, 0.0, 0.1877] | [1.0, 0.0, 0.0, 0.0] |
| EE_SMC_XT661_4C_Universal_Robots_UR3_001 | 0.305           | [0.0, 0.0, 0.1877] | [1.0, 0.0, 0.0, 0.0] |

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/EE_SMC_XT661.png" width="500" height="300">
</p>

Product Link: [SMC (XT661-4C-X427)](https://www.smc.eu/en-eu/products/bernouilli-round-type-xt661-x321~128121~cfg?partNumber=XT661-4C-X321)

**SMC 4.5 Stage Bellows Vacuum Pad with Adapter:**

|          | Weight [kg] | Position [m] | Orientation [-] |
| :------: | :-----------: | :----------: | :-------------: |
| EE_SMC_ZP2_ABB_IRB_120_001 | 0.095           | [0.0, 0.0, 0.186] | [1.0, 0.0, 0.0, 0.0] |
| EE_SMC_ZP2_Universal_Robots_UR3_001 | 0.105           | [0.0, 0.0, 0.186] | [1.0, 0.0, 0.0, 0.0] |

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/EE_SMC_ZP2.png" width="500" height="300">
</p>

Product Link: [SMC (ZP2-TB15ZJS6-AL12-06)](https://www.smc.eu/en-eu/products/4-5-stage-bellows-with-adapter-zp2-t-zj~138574~cfg?partNumber=ZP2-TB15ZJS6-AL12-06)

**ABB Smart Gripper with SMC Vacuum Pad:**

Notes:
  - F  = Fingers
  - VL = Vacuum Suction Cup (L)
  - VR = Vacuum Suction Cup (R)
  - C  = Camera


|          | Weight [kg] | Position [m] | Orientation [-] |
| :------: | :-----------: | :----------: | :-------------: |
| ABB_Smart_Gripper_R_Type_1_001 | 0.300           | <ul><li>F: [0.0, 0.0, 0.1142]</li><li>VL: [0.059, 0.0185, 0.0375]</li></ul><li> VR: [-0.059, 0.0185]</li></ul> | <ul><li>F: [1.0, 0.0, 0.0, 0.0]</li><li>VL: [0.707107, 0.0, 0.707107, 0.0]</li></ul><li> VR: [0.0, -0.707107, 0.0, 0.707107]</li></ul> |
| ABB_Smart_Gripper_L_Type_1_001 | 0.275           | <ul><li>F: [0.0, 0.0, 0.1142]</li><li>VL: [0.059, 0.0185, 0.0375]</li></ul><li> C: [-0.00727, 0.0297, 0.03506]</li></ul> | <ul><li>F: [1.0, 0.0, 0.0, 0.0]</li><li>VL: [0.707107, 0.0, 0.707107, 0.0]</li></ul><li> C: [0.5, -0.5, 0.5, 0.5]</li></ul> |
| ABB_Smart_Gripper_R_Type_2_001 | 0.295           | <ul><li>F: [0.0, 0.0, 0.1142]</li><li>VL: [0.0585, 0.0185, 0.0375]</li></ul><li> VR: [-0.0585, 0.0185, 0.0375]</li></ul> | <ul><li>F: [1.0, 0.0, 0.0, 0.0]</li><li>VL: [0.707107, 0.0, 0.707107, 0.0]</li></ul><li> VR: [0.0, -0.707107, 0.0, 0.707107]</li></ul> |
| ABB_Smart_Gripper_L_Type_2_001 | 0.270           | <ul><li>F: [0.0, 0.0, 0.1142]</li><li>VL: [0.0585, 0.0185, 0.0375]</li></ul><li> C: [-0.00727, 0.0297, 0.03506]</li></ul> | <ul><li>F: [1.0, 0.0, 0.0, 0.0]</li><li>VL: [0.707107, 0.0, 0.707107, 0.0]</li></ul><li> C: [0.5, -0.5, 0.5, 0.5]</li></ul> |

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/ABB_Smart_Gripper_T12.png" width="500" height="200">
</p>

Product Link: [SMC (ZP3-ZP3-T13BS-A5)](https://www.smc.eu/en-eu/products/with-adapter-zp3-t-b~138577~cfg?partNumber=ZP3-T13BS-A5)

**Intel® RealSense™ Depth Camera D435i:**

|          | Weight [kg] | Position [m] | Orientation [-] |
| :------: | :-----------: | :----------: | :-------------: |
| EE_Intel_Camera_HT_Circular_001 | 0.095          | <ul><li>Centroid: [0.0, 0.0, 0.005]</li><li>Camera: [-0.1, 0.0, 0.03]</li></ul> | <ul><li>Centroid: [1.0, 0.0, 0.0, 0.0]</li><li>Camera: [1.0, 0.0, 0.0, 0.0]</li></ul> |
| EE_Intel_Camera_HT_Square_001 | 0.095           | <ul><li>Centroid: [0.0, 0.0, 0.005]</li><li>Camera: [-0.1, 0.0, 0.03]</li></ul> | <ul><li>Centroid: [1.0, 0.0, 0.0, 0.0]</li><li>Camera: [1.0, 0.0, 0.0, 0.0]</li></ul> |

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/EE_Intel_Camera_HT_12.png" width="400" height="200">
</p>

Product Link: [Intel (D435i)](https://www.intelrealsense.com/depth-camera-d435i/)

## Real-World Test:

**Universal Robots UR3:**

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/SMC_EE_UR3.png" width="700" height="250">
</p>

**ABB IRB 120:**

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/SMC_EE_ABB_IRB_120.png" width="700" height="250">
</p>

**ABB IRB 140000 (YuMi):**

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/ABB_YUMI.png" width="700" height="500">
</p>

**General Overview:**

<p align="center">
  <img src="https://github.com/rparak/SMC_End_Effector_Prototype/blob/main/images/SMC_Series_Real.png" width="700" height="500">
</p>

## Contact Info:
Roman.Parak@outlook.com

## Citation (BibTex)
```bash
@misc{RomanParak_DataConverter,
  author = {Roman Parak},
  title = {Modular prototypes of end-effector for robotic arms.},
  year = {2022-2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://https://github.com/rparak/SMC_End_Effector_Prototype}}
}
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

