import helpers.calculations as calculations
import helpers.sensor_widths as sensor_widths
from tabulate import tabulate

"""
First, this script calculates the distance at which you need
to take a picture to get a subject with a given width to fill
a given ratio of the image from the focal length and sensor size.

Second, the DOF, sharpness limits and infinite blurratio are calculated
"""

def main():
    """
    CHANGE THESE PARAMETERS (all parameters in meters)
    """

    # For example with subject_width = 0.5 and subject_frame_ratio = 0.2:
    # A subject with a width of 0.5m should fill 20% of the width of the frame

    subject_width = 0.5
    subject_frame_ratio = 0.2

    # Fullframe equivalent circle of confusion. (see https://en.wikipedia.org/wiki/Circle_of_confusion)
    # Will be scaled with sensor size so end result has equivalent unsharpness
    circle_of_confusion_ff = 32e-6

    # REFERENCE CAMERA / LENS
    sensor_width = sensor_widths.APS_C
    focal_length = 200e-3
    f_stop = 2

    """
    Calculation is performed here
    """

    focus_distance = focal_length * (1 + (subject_width / subject_frame_ratio) / sensor_width)

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