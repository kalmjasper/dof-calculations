import helpers.calculations as calculations
import helpers.sensor_widths as sensor_widths
from tabulate import tabulate

"""
Calculates the required f stop value for a given DOF,
focus distance, focal length, sensor size and ff equivalent
circle of confusion
"""

def main():
    """
    CHANGE THESE PARAMETERS (all parameters in meters)
    """

    # Fullframe equivalent circle of confusion. (see https://en.wikipedia.org/wiki/Circle_of_confusion)
    # Will be scaled with sensor size so end result has equivalent unsharpness
    circle_of_confusion_ff = 32e-6
    focus_distance = 2
    dof = 0.2

    # REFERENCE CAMERA / LENS
    sensor_width = sensor_widths.FULLFRAME
    focal_length = 50e-3

    """
    Calculation is performed here
    """

    # Calculate the equivalent circle of confusion for the given camera sensors
    circle_of_confusion = circle_of_confusion_ff * (sensor_width / sensor_widths.FULLFRAME)

    aperture_opening_calc = calculations.get_aperture_opening_from_dof(
        focal_length,
        focus_distance,
        circle_of_confusion,
        dof
    )

    f_stop = focal_length / aperture_opening_calc

    sharpness_blur = calculations.get_sharpness_limits_blur_radius(
        focal_length,
        focus_distance,
        circle_of_confusion,
        f_stop
    )

    infinity_blurratio = sharpness_blur.blur_radius / sensor_width

    """
    Print results
    """

    res_table = [
        ["Sensor width", sensor_width],
        ["Focus distance", focus_distance],
        ["Focal length", focal_length],
        ["F stop number", f_stop],
        ["Sharpness limits", str(sharpness_blur.sharpness_limits)],
        ["Inf blurratio", infinity_blurratio]
    ]

    print(tabulate(res_table))

if __name__ == '__main__':
    main()