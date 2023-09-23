import numpy as np
import math
from dataclasses import dataclass

@dataclass
class RvSharpnessLimits:
    sharpness_limits: np.array
    blur_radius: float

def get_sharpness_limits_blur_radius(
        focal_length: float,
        focus_distance: float,
        circle_of_confusion: float,
        F_number: float
) -> RvSharpnessLimits:
    """
    Calculates the sharpness limits and the radius of the
    projection of a point at infinite distance at the sensor.
    """
    D = focal_length / F_number

    sharpness_limits = focal_length * (1 + np.array([1, -1]) * (circle_of_confusion / (D + np.array([1, -1]) * circle_of_confusion))) / \
            ((1 + np.array([1, -1]) * (circle_of_confusion / (D + np.array([1, -1]) * circle_of_confusion))) - 1 + focal_length / focus_distance)
    
    blur_radius = D * ((focus_distance / (focus_distance - focal_length)) - 1)

    if sharpness_limits[1] < 0:
            sharpness_limits[1] = np.nan

    return RvSharpnessLimits(sharpness_limits, blur_radius)

def get_aperture_opening_from_dof(
    focal_length: float, focus_distance: float, circle_of_confusion: float, dof: float
) -> float:

    return (
        circle_of_confusion * math.pow(focus_distance, 2)
        - circle_of_confusion * focus_distance * focal_length
        + math.sqrt(
            math.pow(focus_distance, 4)
            + math.pow(focus_distance, 2) * math.pow(dof, 2)
            + (math.pow(focus_distance, 2) + math.pow(dof, 2))
            * math.pow(focal_length, 2)
            - 2
            * (math.pow(focus_distance, 3) - focus_distance * math.pow(dof, 2))
            * focal_length
        )
        * circle_of_confusion
    ) / (dof * focal_length)


# def get_aperture_opening_from_dof(
#         focal_length: float,
#         focus_distance: float,
#         circle_of_confusion: float,
#         dof: float
# ) -> float:
     
#     return (circle_of_confusion*math.pow(focus_distance, 2) - circle_of_confusion*focus_distance*focal_length + math.sqrt(math.pow(focus_distance, 4) + math.pow(focus_distance, 2)*math.pow(dof, 2) + (math.pow(focus_distance, 2) + math.pow(dof, 2))*math.pow(focal_length, 2) - 2*(math.pow(focus_distance, 3) - focus_distance*math.pow(dof, 2))*focal_length)*circle_of_confusion)/(dof*focal_length)