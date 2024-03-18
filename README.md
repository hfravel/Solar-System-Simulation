# Solar-System-Simulation
Simulation of our Solar System written in Python. This code has been adapted from my Astronomy Interface Project. 
When I was recreating this simulation I realized that I messed up the calculations. 
Below is a table of values I used for simulating out solar system.

| Planet  | Perihelion (10^6 km) | Aphelion (10^6 km) | Orbital Period (days) |
|---------|----------------------|--------------------|-----------------------|
| Mercury | 46.0                 | 69.8               | 88                    |
| Venus   | 107.5                | 108.9              | 224.6                 |
| Earth   | 147.1                | 152.1              | 365.2                 |
| Mars    | 206.7                | 249.3              | 697.0                 |
| Jupiter | 740.6                | 816.4              | 4,331.0               |
| Saturn  | 1,357.6              | 1,506.5            | 10,747.0              |
| Uranus  | 2,732.7              | 3,001.4            | 30,589.0              |
| Neptune | 4,471.1              | 4,558.9            | 59,800.0              |

While there is nothing wrong with this data, assuming the data at https://nssdc.gsfc.nasa.gov/planetary/factsheet/ is correct,
there was something wrong with how I was using the data. I knew the planet's orbits were elliptical and just 
assumed the perihelion and aphelion were the semi-minor and semi-major axis respectively. This is wrong. 
Below are the correct Semi-minor and Semi-major Axes.

| Planet  | Semi-minor Axis (10^6 km) | Semi-major Axis (10^6 km) | Orbital Eccentricity |
|---------|---------------------------|---------------------------|----------------------|
| Mercury | 56.7                      | 57.9                      | 0.206                |
| Venus   | 108.2                     | 108.2                     | 0.007                |
| Earth   | 149.6                     | 149.6                     | 0.017                |
| Mars    | 227.0                     | 228.0                     | 0.094                |
| Jupiter | 777.6                     | 778.5                     | 0.049                |
| Saturn  | 1,430.1                   | 1,432.1                   | 0.052                |
| Uranus  | 2,863.9                   | 2,867.1                   | 0.047                |
| Neptune | 4,514.8                   | 4,515.0                   | 0.010                |

You can see there is a lot less variability in the Semi-minor and Semi-major axis than there was the perihelion and aphelion.
This is because our planets' orbits are not very elliptical. With only one planet having above a 0.1 eccentricity.

![Ellipse Diagram](./data/ellipse.png)