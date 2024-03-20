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


def create_orbit_png(planet, semi_minor_axis, semi_major_axis, focal_length, planet_color, radius_star):
    figure, axes = plt.subplots()
    axes.set(axisbelow=True, facecolor="black")
    print(planet)
    axes.grid(color=light_gray, linestyle="-")
    axes.set(title=planet, xlabel=major_axis_str, ylabel=minor_axis_str)

    theta = np.linspace(0, 2 * pi, 100)
    axes.plot(semi_major_axis * np.cos(theta),
              semi_minor_axis * np.sin(theta),
              color=planet_color,
              linewidth=1)

    axes.plot(focal_length, 0, color="gray", marker=".", markersize=2, zorder=1)
    sun = plt.Circle((focal_length, 0), radius_star, color="yellow", linewidth=0, zorder=2)
    axes.add_patch(sun)
    axes.plot(-focal_length, 0, color="gray", marker=".", markersize=2)

    axes.axis("scaled")
    print("\tCreating Low Res... ", flush=True, end="")
    figure.savefig(fname="../data/lowResOrbits/" + planet + "Ellipse.png", dpi=360)
    print("Done")
    print("\tCreating Medium Res... ", flush=True, end="")
    figure.savefig(fname="../data/mediumResOrbits/" + planet + "Ellipse.png", dpi=720)
    print("Done")
    print("\tCreating High Res... ", flush=True, end="")
    figure.savefig(fname="../data/highResOrbits/" + planet + "Ellipse.png", dpi=1440)
    print("Done")


for i in range(8):
    create_orbit_png(celestials_info[i][0],
                     celestials_info[i][1],
                     celestials_info[i][2],
                     celestials_info[i][3],
                     celestials_info[i][4],
                     radius_sun)
