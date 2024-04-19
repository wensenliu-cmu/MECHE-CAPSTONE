from read_joystick import Joystick

PS5_Controller = Joystick()

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
    PS5_Controller.delay_to_fps(30)

PS5_Controller.quit_pygame()