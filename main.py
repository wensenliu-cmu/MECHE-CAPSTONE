from read_joystick import Joystick
from comms import UART
import math

PS5_Controller = Joystick()
conn = UART()

while not PS5_Controller.done:
    PS5_Controller.event_handler()
    PS5_Controller.clear_display()
    PS5_Controller.count_joysticks()

    PS5_Controller.parse_joysticks()
    PS5_Controller.return_labeled_axes()
    PS5_Controller.return_labeled_buttons()

    PS5_Controller.display_axes()
    PS5_Controller.display_buttons()
    PS5_Controller.display_hats()

    PS5_Controller.update_display()
    
    axes_values = PS5_Controller.labeled_axes
    axis_data = axes_values["lknob_x"]
    print(axis_data)

    conn.write_serial(f"lknob_x is {math.floor(axis_data * 100)}") # Encoding cannot encode periods, so must be integers
    conn.read_serial()

    PS5_Controller.delay_to_fps(30)

PS5_Controller.quit_pygame()