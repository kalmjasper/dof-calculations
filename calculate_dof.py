import helpers.calculations as calculations
import helpers.sensor_widths as sensor_widths
from tabulate import tabulate

"""
This script can be used to calculate the depth of field
and the infinity blur radius for a given camera setup
"""

def main():
    """
    CHANGE THESE PARAMETERS (all parameters in meters)
    """

    # Fullframe equivalent circle of confusion. (see https://en.wikipedia.org/wiki/Circle_of_confusion)
    # Will be scaled with sensor size so end result has equivalent unsharpness
    circle_of_confusion_ff = 32e-6
    focus_distance = 2

    # REFERENCE CAMERA / LENS
    sensor_width = sensor_widths.APS_C
    focal_length = 56e-3
    f_stop = 1.2

    """
    Calculation is performed here
    """

    # Calculate the equivalent circle of confusion for the given camera sensors
    circle_of_confusion = circle_of_confusion_ff * (sensor_width / sensor_widths.FULLFRAME)

    sharpness_blur = calculations.get_sharpness_limits_blur_radius(
        focal_length,
        focus_distance,
        circle_of_confusion,
        f_stop
    )

    infinity_blurratio = sharpness_blur.blur_radius / sensor_width

    dof = sharpness_blur.sharpness_limits[1] - sharpness_blur.sharpness_limits[0]

    """
    Print results
    """

    res_table = [
        ["Sensor width", sensor_width],
        ["Focus distance", focus_distance],
        ["Focal length", focal_length],
        ["F stop number", f_stop],
        ["Sharpness limits", str(sharpness_blur.sharpness_limits)],
        ["DOF", dof],
        ["Inf blurratio", infinity_blurratio]
    ]

    print(tabulate(res_table))

if __name__ == '__main__':
    main()