import tkinter as tk
import math

simulation_name = "Solar System Simulation"
main_font = ["Times New Roman", 24, "bold underline"]
background_color = "black"
circle_size = 10
two_pi = 2 * math.pi
# [Celestial Object, Semi-Minor Axis, Semi-Major Axis, Orbital Period (days), Color]
celestials_info = [("Sun", 0.0, 0.0, 0.0, "yellow"),
                   ("Mercury",   56.7,   57.9,    88.0, "grey"),
                   ("Venus",    108.2,  108.2,   224.6, "orange"),
                   ("Earth",    149.6,  149.6,   365.2, "green"),
                   ("Mars",     227.0,  228.0,   687.0, "red"),
                   ("Jupiter",  777.6,  778.5,  4331.0, "tan"),
                   ("Saturn",  1430.1, 1432.1, 10747.0, "brown"),
                   ("Uranus",  2863.9, 2867.1, 30589.0, "light blue"),
                   ("Neptune", 4514.8, 4515.0, 59800.0, "blue")]


def create_simulation_window():
    simulation_root = tk.Tk(className=simulation_name)
    simulation_root.geometry("500x500")
    create_title(simulation_root)
    create_simulation(simulation_root)
    simulation_root.mainloop()


def create_title(simulation):
    title_frame = tk.Frame(simulation, height=1)
    title_frame.pack(fill=tk.X)
    title_label = tk.Label(text=simulation_name, height=1, font=main_font)
    title_label.pack(in_=title_frame, fill=tk.X)


def calculate_new_pos(center_coord, curr_radians, grid_size, semi_minor_axis, semi_major_axis):
    return (grid_size * semi_major_axis * math.cos(curr_radians) + center_coord[0],
            grid_size * semi_minor_axis * math.sin(curr_radians) + center_coord[1])


def create_simulation(simulation):
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


create_simulation_window()
