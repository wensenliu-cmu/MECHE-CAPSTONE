from actuator_control import Servo, Motor
from read_joystick import Joystick
from display import DataWindow
from comms import UART

import pygame
import math
import time

display_window = DataWindow()
PS5_Controller = Joystick(screen=display_window.screen, text_print=display_window.text_print)
conn = UART()

base_servo = Servo(range_min=850, range_max=1500)
arm_servo = Servo(range_min=500, range_max=1820)
grip_servo = Servo(range_min=730, range_max=1970)

while not PS5_Controller.done:
    
    #init_time = time.time()
    
    ### Joystick input handling

    # Initialization for joystick and display
    PS5_Controller.event_handler()
    display_window.clear_display()
    PS5_Controller.count_joysticks()

    # Data parsing from joystick
    PS5_Controller.parse_joysticks()
    PS5_Controller.return_labeled_axes()
    PS5_Controller.return_labeled_buttons()

    # Display updates for window tracking joystick values
    PS5_Controller.display_axes()
    PS5_Controller.display_buttons()
    PS5_Controller.display_hats()
    
    ### Compiling and sending control inputs
    axes_values = PS5_Controller.labeled_axes

    # Base servo (controlled by lknob_x)
    if not base_servo.homed: base_servo.home_servo()
    else:
        val_lknob_x = axes_values["lknob_x"]
        if val_lknob_x < 0: base_servo.decrease_pos(val_lknob_x)
        else: base_servo.increase_pos(val_lknob_x)
    display_window.print_string(f"Base Servo Position: {base_servo.curr_pos}")
    
    conn.write_serial(f"B{base_servo.curr_pos}") # Encoding cannot encode periods, so must be integers
    conn.read_serial()

    # Arm servo (controlled by lknob_y)
    if not arm_servo.homed: arm_servo.home_servo()
    else:
        val_lknob_y = axes_values["lknob_y"]
        if val_lknob_y < 0: arm_servo.decrease_pos(val_lknob_y)
        else: arm_servo.increase_pos(val_lknob_y)
    display_window.print_string(f"Arm Servo Position: {arm_servo.curr_pos}")

    conn.write_serial(f"A{arm_servo.curr_pos}") # Encoding cannot encode periods, so must be integers
    conn.read_serial()

    # Gripper servo (controlled by rknob_y)
    if not grip_servo.homed: grip_servo.home_servo()
    else:
        val_rknob_y = axes_values["rknob_y"]
        if val_rknob_y < 0: grip_servo.decrease_pos(val_rknob_y)
        else: grip_servo.increase_pos(val_rknob_y)
    display_window.print_string(f"Gripper Servo Position: {grip_servo.curr_pos}")

    conn.write_serial(f"G{grip_servo.curr_pos}") # Encoding cannot encode periods, so must be integers
    conn.read_serial()

    #conn.write_serial(f"lknob_x is {2.5}") # Encoding cannot encode periods, so must be integers
    #conn.read_serial()

    # Push updates to display
    display_window.update_display()

    # Delay to FPS rate
    PS5_Controller.delay_to_fps(60)

    # Verification of delay
    #end_time = time.time()
    #print(f"Elapsed: {end_time-init_time}")

PS5_Controller.quit_pygame()