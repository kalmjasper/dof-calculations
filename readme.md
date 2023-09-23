
Depth of field calculation scripts
====================================

Overview
--------

This repository contains three Python scripts that perform various camera calculations related to the depth of field (DOF), given different camera setups and parameters. This collection of scripts is designed to assist photographers in selecting the optimal camera / lens combination for portrait photography. 

Setup
------------

### Prerequisites
- `python`
- `pipenv`

### How to use
1. Clone this repository
`git clone https://github.com/kalmjasper/dof-calculations.git`
2. Navigate to the project root folder
`cd dof-calculations`
3. Install dependencies
`pipenv install`
4. Adjust the required parameters in the desired script
5. Run the script
`pipenv run calculate_dof`
`pipenv run calculate_dof_subject`
`pipenv run calculate_dof_f_stop`

## Terminology
**Sensor width:**
Width of the sensor of the camera used (35mm for FF, 23.5mm for APS-C, ...)

**Focus distance:**
The distance at which the camera is positioned from the subject with the subject in focus

**Focal length:**
Focal length of lens

**F stop number:**
The relative size of the aperture opening to the focal length 
$$N=\frac{f}{D}$$

Where $f$ is the focal length, $D$ the opening diameter of the aperture and $N$ the f/stop number

**Circle of confusion:**
The size of the blurred or "unfocused" spot that a point source of light becomes when it is projected through a camera's lens and onto the sensor

**Sharpness limits:**
The near and far boundaries within an image where objects appear acceptably sharp. The determination of sharpness limits is intrinsically tied to the circle of confusion

**Depth of Field (DoF):**
The distance between the near and far sharpness limit.

**Infinite blur ratio:**
The ratio between the size of the circle projected on the camera sensor by a point source of light at infinite distance and the sensor width. This is a measure for how unsharp the background of a portrait will be in the final image, independent of sensor size.

Script Descriptions
------
### calculate_dof.py
**Inputs:**
- Circle of confusion
- Focus distance
- Sensor width
- Focal length
- F stop number

**Outputs**:
- Sharpness limits
- DoF
- Infinite blur ratio

**Use case:**
Calculating the near far sharpness limits when taking a picture of a subject to make sure the final result will be sharp

### calculate_f_stop.py
**Inputs:**
- Circle of confusion
- Focus distance
- Sensor width
- Focal length
- DoF

**Outputs**:
- Sharpness limits
- F stop number
- Infinite blur ratio

**Use case:**
Choosing a lens for a camera that will produce the same depth of field as with another camera setup

### calculate_dof_subject.py
**Inputs:**
- Subject width
- Subject to frame ratio
The ratio between the width of the subject and the total width of the frame
- Circle of confusion
- Sensor width
- Focal length
- DoF

**Outputs**:
- Sharpness limits
- Focus distance
- F stop number
- Infinite blur ratio

**Use case:**
Two lenses are available, a 35mm f1.4 lens and a 50mm f2 lens. This script can be used to calculate which lens will give the biggest background unsharpness for a similar composition (of the subject, background will be compressed with the higher focal length). 

References
----------

-   Circle of Confusion: [Wikipedia](https://en.wikipedia.org/wiki/Circle_of_confusion)