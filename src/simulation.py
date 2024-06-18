import tkinter as tk
import math
from PIL import Image, ImageTk

simulation_name = "Solar System Simulation"
main_font = ["Times New Roman", 24, "bold underline"]
background_color = "black"
circle_size = 10
two_pi = 2.0 * math.pi
half_pi = math.pi / 2.0
# Gravitational Constant converted from m^3 / (s^2kg) to 10^6km^3 / (0.365days^2 10^24kg)
gravitational_constant = 0.000000000066743 * 994519.296
# convert from km / s^2 to 10^6km / 0.365days^2
acceleration_speed = 994.519296
# convert from km / s to 10^6km / 0.365days
base_velocity = 0.031536
# [Celestial Object, Semi-Minor Axis (10^6 km), Semi-Major Axis (10^6 km), Orbital Period (days), Color]
celestials_info = [("Sun", 0.0, 0.0, 0.0, "yellow"),
                   ("Mercury", 56.7, 57.9, 88.0, "grey"),
                   ("Venus", 108.2, 108.2, 224.6, "orange"),
                   ("Earth", 149.6, 149.6, 365.2, "green"),
                   ("Mars", 227.0, 228.0, 687.0, "red"),
                   ("Jupiter", 777.6, 778.5, 4331.0, "tan"),
                   ("Saturn", 1430.1, 1432.1, 10747.0, "brown"),
                   ("Uranus", 2863.9, 2867.1, 30589.0, "light blue"),
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
# Neptune: X = 4.465081382539217E+09 Y =-2.310890716657726E+08 Z =-9.814325490398000E+07
# Planets locations & velocities on March 20th
planet_locations = [[-1.1311, -0.5145, 0.0308],
                    [-2.6369, 45.5508, 3.9334],
                    [71.6401, -81.4081, -5.2791],
                    [-150.0999, 0.6834, 0.0312],
                    [118.9463, -171.7443, -6.5030],
                    [453.0145, 593.9629, -12.5993],
                    [1364.7719, -495.0326, 45.7307],
                    [1797.6897, 2315.0823, -14.6911],
                    [4465.0814, -231.0891, -98.1433]]
# Sun: VX= 9.436577189104194E-03 VY=-1.116925453165473E-02 VZ=-1.103808024457472E-04
# Mercury: VX=-5.845100836810801E+01 VY= 1.669856050245631E-01 VZ= 5.376633687112422E+00
# Venus: VX= 2.581708739932919E+01 VY= 2.328274725558281E+01 VZ=-1.169326180959195E+00
# Earth: VX=-7.047251692568980E-01 VY=-2.990517698393922E+01 VZ= 1.829159525938095E-03
# Mars: VX= 2.076190915469121E+01 VY= 1.597586834815308E+01 VZ=-1.740941772629139E-01
# Jupiter: VX=-1.053352894910712E+01 VY= 8.543798399251099E+00 VZ= 2.002467936169445E-01
# Saturn: VX= 2.755453800479755E+00 VY= 9.060365323150547E+00 VZ=-2.667267884808333E-01
# Uranus: VX=-5.428504763241280E+00 VY= 3.859263759552261E+00 VZ= 8.457204155273312E-02
# Neptune: VX= 2.450130378210048E-01 VY= 5.460312578226561E+00 VZ=-1.180327296355499E-01
planet_velocities = [[9.436577189104194E-03, -1.116925453165473E-02, -1.103808024457472E-04],
                     [-5.845100836810801E+01, 1.669856050245631E-01, 5.376633687112422E+00],
                     [2.581708739932919E+01, 2.328274725558281E+01, -1.169326180959195E+00],
                     [-7.047251692568980E-01, -2.990517698393922E+01, 1.829159525938095E-03],
                     [2.076190915469121E+01, 1.597586834815308E+01, -1.740941772629139E-01],
                     [-1.053352894910712E+01, 8.543798399251099E+00, 2.002467936169445E-01],
                     [2.755453800479755E+00, 9.060365323150547E+00, -2.667267884808333E-01],
                     [-5.428504763241280E+00, 3.859263759552261E+00, 8.457204155273312E-02],
                     [2.450130378210048E-01, 5.460312578226561E+00, -1.180327296355499E-01]]
# 10^24 kg
planet_masses = [1988500.0, 0.3302, 4.8685, 5.97219, 0.6417, 1898.1872, 568.34, 86.813, 102.409]


def create_simulation_window(physics_accurate):
    simulation_root = tk.Tk(className=simulation_name)
    simulation_root.geometry()
    create_title(simulation_root)
    if physics_accurate:
        # show_image(simulation_root)
        create_physics_simulation(simulation_root)
    else:
        create_original_simulation(simulation_root)
    simulation_root.mainloop()


def show_image(simulation):
    simulation_frame = tk.Frame(simulation, height=1)
    simulation_frame.pack(fill=tk.BOTH, expand=True)

    simulation_canvas = tk.Canvas(simulation_frame, bg=background_color, width=840, height=859)
    simulation_canvas.pack(in_=simulation_frame, fill=tk.BOTH, expand=True)

    # img = tk.PhotoImage(file='.\\..\\data\\planetImages\\github.png')
    img = tk.PhotoImage(file=r'.\..\data\planetImages\sun.png')
    simulation_canvas.create_image(0, 0, anchor=tk.NW, image=img)


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


def calculate_2d_orientation(diff_x, diff_y):
    if diff_x == 0.0:
        xy_theta = half_pi
    else:
        xy_theta = math.atan(diff_y / diff_x)
    distance = diff_x if diff_y == 0.0 else diff_y / math.sin(xy_theta)
    return distance, xy_theta


def calculate_3d_orientation(xyz1, xyz2):
    diff_x = xyz2[0] - xyz1[0]
    sign_x = -1 if diff_x < 0.0 else 1
    diff_y = xyz2[1] - xyz1[1]
    sign_y = -1 if diff_y < 0.0 else 1
    diff_z = xyz2[2] - xyz1[2]
    sign_z = -1 if diff_z < 0.0 else 1
    xz_hypotenuse, xz_theta = calculate_2d_orientation(math.fabs(diff_x), math.fabs(diff_z))
    distance, xyz_theta = calculate_2d_orientation(xz_hypotenuse, math.fabs(diff_y))
    return distance, xz_theta, xyz_theta, (sign_x, sign_y, sign_z)


def get_3d_vector_components(magnitude, xz_theta, xyz_theta):
    y_force = magnitude * math.sin(xyz_theta)
    xz_force = magnitude * math.cos(xyz_theta)
    x_force = xz_force * math.cos(xz_theta)
    z_force = xz_force * math.sin(xz_theta)
    return x_force, y_force, z_force


def calculate_acceleration_due_to_gravity(mass2, distance):
    return gravitational_constant * mass2 / (distance * distance)


def calculate_acceleration(main_index, all_masses, all_coord):
    length = len(all_masses)
    if length != len(all_coord):
        return "Fail"
    x_acc = 0.0
    y_acc = 0.0
    z_acc = 0.0

    for i in range(length):
        if i == main_index:
            continue
        distance, xz_theta, xyz_theta, signs = calculate_3d_orientation(all_coord[main_index], all_coord[i])
        gravity = calculate_acceleration_due_to_gravity(all_masses[i], distance)
        temp_x, temp_y, temp_z = get_3d_vector_components(gravity, xz_theta, xyz_theta)
        x_acc += temp_x * signs[0]
        y_acc += temp_y * signs[1]
        z_acc += temp_z * signs[2]

    return x_acc, y_acc, z_acc


def create_physics_simulation(simulation):
    simulation_frame = tk.Frame(simulation, height=1)
    simulation_frame.pack(fill=tk.BOTH, expand=True)

    simulation_canvas = tk.Canvas(simulation_frame, bg=background_color)
    simulation_canvas.pack(in_=simulation_frame, fill=tk.BOTH, expand=True)

    celestials_curr_position = [planet_locations[i] for i in range(9)]
    celestials_curr_velocity = [planet_velocities[i] for i in range(9)]
    for i in range(9):
        celestials_curr_velocity[i][0] *= base_velocity
        celestials_curr_velocity[i][1] *= base_velocity
        celestials_curr_velocity[i][2] *= base_velocity

    for i in range(9):
        simulation_canvas.create_oval(
            (0, 0, circle_size, circle_size),
            fill=celestials_info[i][4],
            tags=celestials_info[i][0])
        # simulation_canvas.move(temp_oval, march20_planet_locations[i][0], march20_planet_locations[i][1])

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
            new_pos = (grid_size * celestials_curr_position[j][0] + center_coordinates[0],
                       center_coordinates[1] - grid_size * celestials_curr_position[j][1])
            simulation_canvas.move(celestials_info[j][0], new_pos[0] - old_pos[0], new_pos[1] - old_pos[1])

    def run_simulation():
        try:
            for j in range(9):
                temp_ax, temp_ay, temp_az = calculate_acceleration(j, planet_masses, celestials_curr_position)
                celestials_curr_velocity[j][0] += temp_ax
                celestials_curr_velocity[j][1] += temp_ay
                celestials_curr_velocity[j][2] += temp_az
                celestials_curr_position[j][0] += celestials_curr_velocity[j][0]
                celestials_curr_position[j][1] += celestials_curr_velocity[j][1]
                celestials_curr_position[j][2] += celestials_curr_velocity[j][2]
            update_planets()
            simulation.after(10, run_simulation)
        except Exception as e:
            print(e)

    run_simulation()


if __name__ == "__main__":
    create_simulation_window(True)
    # print(str(gravitational_constant * 10 / 5**2  * math.cos(0.92729) +
    #           gravitational_constant * 20 / 10**2 * math.cos(0.6435)))
    # print(str(gravitational_constant * 30 / 68.55555 * math.cos(0.6998)))
