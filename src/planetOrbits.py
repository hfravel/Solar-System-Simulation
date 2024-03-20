import numpy as np
import matplotlib.pyplot as plt
from math import pi

# [Celestial Object, Semi-Minor Axis (10^6 km), Semi-Major Axis (10^6 km), Focal Length (10^6 km), Color]
celestials_info = [("Mercury", 56.7, 57.9, 11.9, "grey"),
                   ("Venus", 108.2, 108.2, 0.7, "orange"),
                   ("Earth", 149.6, 149.6, 2.5, "green"),
                   ("Mars", 227.0, 228.0, 21.3, "red"),
                   ("Jupiter", 777.6, 778.5, 37.9, "tan"),
                   ("Saturn", 1430.1, 1432.1, 74.5, "brown"),
                   ("Uranus", 2863.9, 2867.1, 134.4, "lightblue"),
                   ("Neptune", 4514.8, 4515.0, 43.9, "blue")]
radius_sun = 0.696  # 10^6 km
light_gray = "#303030"
major_axis_str = "Major Axis (10^6 km)"
minor_axis_str = "Minor Axis (10^6 km)"

fig, ax = plt.subplots()
ax.set(axisbelow=True, facecolor="black")

for i in range(8):
    print(celestials_info[i][0])
    ax.grid(color=light_gray, linestyle="-")
    ax.set(title=celestials_info[i][0], xlabel=major_axis_str, ylabel=minor_axis_str)

    theta = np.linspace(0, 2 * pi, 100)
    ax.plot(celestials_info[i][2] * np.cos(theta),
            celestials_info[i][1] * np.sin(theta),
            color=celestials_info[i][4],
            linewidth=1)

    ax.plot(celestials_info[i][3], 0, color="gray", marker=".", markersize=2, zorder=1)
    sun = plt.Circle((celestials_info[i][3], 0), radius_sun, color="yellow", linewidth=0, zorder=2)
    ax.add_patch(sun)
    ax.plot(-celestials_info[i][3], 0, color="gray", marker=".", markersize=2)

    ax.axis("scaled")
    fig.savefig(fname="../data/lowResOrbits/" + celestials_info[i][0] + "Ellipse.png", dpi=360)
    fig.savefig(fname="../data/mediumResOrbits/" + celestials_info[i][0] + "Ellipse.png", dpi=720)
    fig.savefig(fname="../data/highResOrbits/" + celestials_info[i][0] + "Ellipse.png", dpi=1440)
    ax.cla()
