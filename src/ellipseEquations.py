import math


# Below are the equations I actually needed for figuring out the major and minor axis
# using the Perihelion, Aphelion, and Eccentricity of each orbit
def major_axis_eq(perihelion, aphelion):
    return perihelion + aphelion


def semi_major_axis_eq(perihelion, aphelion):
    return major_axis_eq(perihelion, aphelion) / 2


def semi_minor_axis_eq(eccentricity, perihelion, aphelion):
    return math.sqrt(semi_major_axis_eq(perihelion, aphelion)**2 * (1 - eccentricity**2))


def minor_axis_eq(eccentricity, perihelion, aphelion):
    return semi_minor_axis_eq(eccentricity, perihelion, aphelion) * 2


def print_semi_minor_and_major_axis(planet, eccentricity, perihelion, aphelion):
    return (planet + ": Minor = " + str(semi_minor_axis_eq(eccentricity, perihelion, aphelion))
            + ", Major = " + str(semi_major_axis_eq(perihelion, aphelion)))


print(print_semi_minor_and_major_axis("Mercury", 0.206, 46.0, 69.8))
print(print_semi_minor_and_major_axis("Venus", 0.007, 107.5, 108.9))
print(print_semi_minor_and_major_axis("Earth", 0.017, 147.1, 152.1))
print(print_semi_minor_and_major_axis("Mars", 0.094, 206.7, 249.3))
print(print_semi_minor_and_major_axis("Jupiter", 0.049, 740.6, 816.4))
print(print_semi_minor_and_major_axis("Saturn", 0.052, 1357.6, 1506.5))
print(print_semi_minor_and_major_axis("Uranus", 0.047, 2732.7, 3001.4))
print(print_semi_minor_and_major_axis("Neptune", 0.010, 4471.1, 4558.9))


# Below are equations relating to ellipses that I found fun to program
def eccentricity_eq1(focal_length, semi_major_axis):
    return focal_length / semi_major_axis


def eccentricity_eq2(semi_major, semi_minor):
    return math.sqrt(1 - (semi_minor**2 / semi_major**2))


def focal_length_eq1(semi_major_axis, semi_minor_axis):
    return math.sqrt(semi_major_axis**2 - semi_minor_axis**2)


def focal_length_eq2(perihelion, aphelion):
    return perihelion - aphelion
