import numpy as np
import matplotlib.pyplot as plt
import helpers.calculations as calculations

circle_of_confusion = 0.032e-3
F_number = 1.4

focal_lengths = np.linspace(10e-3, 100e-3, num=1000)
focus_distances = np.linspace(1, 200, num=1000)

assymetries = np.zeros((len(focus_distances), len(focal_lengths)))

for j, focal_length in enumerate(focal_lengths):
    for k, focus_distance in enumerate(focus_distances):

        rv = calculations.get_sharpness_limits_blur_radius(focal_length, focus_distance, circle_of_confusion, F_number)

        if rv.sharpness_limits[1] < 0:
            rv.sharpness_limits[1] = np.nan

        shapness_deltas = rv.sharpness_limits - focus_distance
        dof_assymetry = -shapness_deltas[1] / shapness_deltas[0]

        assymetries[k, j] = dof_assymetry

pc = plt.pcolor(focal_lengths * 1e3, focus_distances, assymetries, shading='auto', vmin=1, vmax=5)
plt.colorbar()

# print(assymetries)

plt.xlabel('Focal Length (mm)')
plt.ylabel('Focus Distance (m)')
plt.title('Depth of Field (DOF) Asymmetry with F1.4')
plt.grid(True)

plt.show()
