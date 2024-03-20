import tkinter as tk
import math

simulation_name = "Solar System Simulation"
main_font = ["Times New Roman", 24, "bold underline"]
background_color = "black"
circle_size = 10
two_pi = 2 * math.pi
gravitational_constant = 0.000000000066743
# [Celestial Object, Semi-Minor Axis (10^6 km), Semi-Major Axis (10^6 km), Orbital Period (days), Color]
celestials_info = [("Sun", 0.0, 0.0, 0.0, "yellow"),
                   ("Mercury",   56.7,   57.9,    88.0, "grey"),
                   ("Venus",    108.2,  108.2,   224.6, "orange"),
                   ("Earth",    149.6,  149.6,   365.2, "green"),
                   ("Mars",     227.0,  228.0,   687.0, "red"),
                   ("Jupiter",  777.6,  778.5,  4331.0, "tan"),
                   ("Saturn",  1430.1, 1432.1, 10747.0, "brown"),
                   ("Uranus",  2863.9, 2867.1, 30589.0, "light blue"),
                   ("Neptune", 4514.8, 4515.0, 59800.0, "blue")]
# Go on Horizons Web Application with the following settings:
# Ephemeris Type = "Vector Table", Coordinate Center = "Solar System Barycenter (SSB),
# Time Specification = "Start=2024-03-20 TBD, Stop=2024-03-21", Table Settings = "default"
# -----------------------------------------------------------------------------------------
# Sun: X =-1.131090720605570E+06 Y =-5.145333496736483E+05 Z = 3.082875878525921E+04
# Mercury: X =-2.636929220111852E+06 Y = 4.555085651148096E+07 Z = 3.933457569130151E+06
# Venus: X = 7.164018335450876E+07 Y =-8.140812352752428E+07 Z =-5.279084883507226E+06
# Earth: X = -1.500999867885233E+08 Y = 6.834400710257996E+05 Z = 3.121362015459809E+04
# Mars: X = 1.189462835555445E+08 Y =-1.717443298724728E+08 Z =-6.503006384505823E+06
# Jupiter: X = 4.530145325860761E+08 Y = 5.939629036180155E+08 Z =-1.259930540914109E+07
# Saturn: X = 1.364771897234220E+09 Y =-4.950326275014771E+08 Z =-4.573073979849464E+07
# Uranus: X = 1.797689731156021E+09 Y = 2.315082283331097E+09 Z =-1.469112499741995E+07
# Neptune: 4.465081382539217E+09 Y =-2.310890716657726E+08 Z =-9.814325490398000E+07
march20_planet_locations = [(-1.1311, -0.5145, 0.0308),
                            (-2.6369, 45.5508, 3.9334),
                            (71.6401, -81.4081, -5.2791),
                            (-150.0999, 0.6834, 0.0312),
                            (118.9463, -171.7443, -6.5030),
                            (453.0145, 593.9629, -12.5993),
                            (1364.7719, -495.0326, 45.7307),
                            (1797.6897, 2315.0823, -14.6911),
                            (4465.0814, -231.0891, -98.1433)]


def create_simulation_window():
    simulation_root = tk.Tk(className=simulation_name)
    simulation_root.geometry("500x500")
    create_title(simulation_root)
    create_original_simulation(simulation_root)
    simulation_root.mainloop()


def create_title(simulation):
    title_frame = tk.Frame(simulation, height=1)
    title_frame.pack(fill=tk.X)
    title_label = tk.Label(text=simulation_name, height=1, font=main_font)
    title_label.pack(in_=title_frame, fill=tk.X)


def calculate_new_pos(center_coord, curr_radians, grid_size, semi_minor_axis, semi_major_axis):
    return (grid_size * semi_major_axis * math.cos(curr_radians) + center_coord[0],
            grid_size * semi_minor_axis * math.sin(curr_radians) + center_coord[1])


def create_original_simulation(simulation):
    simulation_frame = tk.Frame(simulation, height=1)
    simulation_frame.pack(fill=tk.BOTH, expand=True)

    simulation_canvas = tk.Canvas(simulation_frame, bg=background_color)
    simulation_canvas.pack(in_=simulation_frame, fill=tk.BOTH, expand=True)

    celestials_curr_radians = [0.0 for _ in range(9)]
    simulation_speed = 3
    is_running = True

    for i in range(9):
        simulation_canvas.create_oval(
            (0, 0, circle_size, circle_size),
            fill=celestials_info[i][4],
            tags=celestials_info[i][0])

    def update_planets():
        # Provides a buffer to the edge of the canvas so planets don't go off the screen
        canvas_buffer = 1.05
        # Makes sure winfo.width() gets right size of canvas
        simulation.update()
        width = simulation_canvas.winfo_width()
        height = simulation_canvas.winfo_height()
        center_coordinates = ((width - circle_size) / 2, (height - circle_size) / 2)

        grid_size = width / (celestials_info[8][2] * 2 * canvas_buffer)

        for j in range(9):
            old_pos = simulation_canvas.coords(celestials_info[j][0])
            new_pos = calculate_new_pos(center_coordinates,
                                        celestials_curr_radians[j],
                                        grid_size,
                                        celestials_info[j][1],
                                        celestials_info[j][2])
            simulation_canvas.move(celestials_info[j][0], new_pos[0] - old_pos[0], new_pos[1] - old_pos[1])

    def run_simulation():
        try:
            for j in range(1, 9):
                celestials_curr_radians[j] = ((celestials_curr_radians[j] - (simulation_speed / celestials_info[j][3]))
                                              % two_pi)
            update_planets()
            if is_running:
                simulation.after(10, run_simulation)
        except Exception as e:
            print(e)

    run_simulation()


def calculate_gravity(mass1, mass2, distance):
    return gravitational_constant * mass1 * mass2 / (distance*distance)


def calculate_acceleration_for_multiple_bodies(masses, distances):
    num_masses = len(masses)
    if num_masses != len(distances):
        return float("nan")
    acceleration = 0
    mass_over_distances = [0.0 for _ in range(num_masses)]
    result_accelerations = [0.0 for _ in range(num_masses)]

    for i in range(1, num_masses):
        mass_over_distances[i] = masses[i] / (distances[i]*distances[i])
        acceleration += mass_over_distances[i]

    result_accelerations[0] = gravitational_constant * acceleration
    acceleration += masses[0] / (distances[0]*distances[0])

    for i in range(1, num_masses):
        result_accelerations[i] = gravitational_constant * (acceleration - mass_over_distances[i])

    return result_accelerations


def create_physics_simulation(simulation):
    simulation_frame = tk.Frame(simulation, height=1)
    simulation_frame.pack(fill=tk.BOTH, expand=True)

    simulation_canvas = tk.Canvas(simulation_frame, bg=background_color)
    simulation_canvas.pack(in_=simulation_frame, fill=tk.BOTH, expand=True)

    celestials_curr_position = [march20_planet_locations[i] for i in range(9)]


create_simulation_window()
