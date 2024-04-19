import pygame

# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

class Joystick:
    
    def __init__(self):
        
        pygame.init()

        # Set the width and height of the screen (width, height), and name the window.
        self.screen = pygame.display.set_mode((500, 700))
        pygame.display.set_caption("Joystick example")

        # Used to manage how fast the screen updates.
        self.clock = pygame.time.Clock()

        # Get ready to print.
        self.text_print = TextPrint()

        # Joystick data
        self.joysticks = {}
        self.joystick_count = 0

        self.jid = None             # Joystick ID
        self.name = None            # Joystick Name
        self.guid = None            # Joystick GUID
        self.power_level = None     # Joystick Power Level
        self.num_axes = None        # Num Axes
        self.num_buttons = None     # Num Buttons
        self.num_hats = None        # Num Hats
        self.axes = None            # List of Axes
        self.buttons = None         # List of Buttons
        self.hats = None            # List of Hats

        # Program complete tag
        self.done = False
    
    def event_handler(self):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                if event.button == 0:
                    joystick = self.joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print(f"Rumble effect played on joystick {event.instance_id}")

            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                self.joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connected")

            if event.type == pygame.JOYDEVICEREMOVED:
                del self.joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")
    
    def clear_display(self):
        # Drawing step
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        self.screen.fill((255, 255, 255))
        self.text_print.reset()

    def count_joysticks(self):
        # Get count of joysticks.
        self.joystick_count = pygame.joystick.get_count()

        self.text_print.tprint(self.screen, f"Number of joysticks: {self.joystick_count}")
        self.text_print.indent()
    
    def parse_joysticks(self):
        for joystick in self.joysticks.values():
            self.jid = joystick.get_instance_id()

            self.text_print.tprint(self.screen, f"Joystick {self.jid}")
            self.text_print.indent()

            # Get the name from the OS for the controller/joystick.
            self.name = joystick.get_name()
            self.text_print.tprint(self.screen, f"Joystick name: {self.name}")

            self.guid = joystick.get_guid()
            self.text_print.tprint(self.screen, f"GUID: {self.guid}")

            self.power_level = joystick.get_power_level()
            self.text_print.tprint(self.screen, f"Joystick's power level: {self.power_level}")

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other. Triggers count as axes.
            self.num_axes = joystick.get_numaxes()
            self.text_print.tprint(self.screen, f"Number of axes: {self.num_axes}")
            self.axes = [joystick.get_axis(i) for i in range(self.num_axes)]

            # Get buttons
            self.num_buttons = joystick.get_numbuttons()
            self.text_print.tprint(self.screen, f"Number of buttons: {self.num_buttons}")
            self.buttons = [joystick.get_button(i) for i in range(self.num_buttons)]

            # Get hats
            self.num_hats = joystick.get_numhats()
            self.text_print.tprint(self.screen, f"Number of hats: {self.num_hats}")
            self.hats = [joystick.get_hat(i) for i in range(self.num_hats)]
    
    def display_axes(self):
        self.text_print.indent()
        i = 0
        for axis in self.axes:
            self.text_print.tprint(self.screen, f"Axis {i} value: {axis:>6.3f}")
            i += 1
        self.text_print.unindent()

    def display_buttons(self):
        self.text_print.indent()
        i = 0
        for button in self.buttons:
            self.text_print.tprint(self.screen, f"Button {i:>2} value: {button}")
            i += 1
        self.text_print.unindent()

    def display_hats(self):
        self.text_print.indent()
        i = 0
        for hat in self.hats:
            self.text_print.tprint(self.screen, f"Hat {i} value: {str(hat)}")
            i += 1
        self.text_print.unindent()

    def update_display(self):
        pygame.display.flip()

    def delay_to_fps(self, fps):
        self.clock.tick(fps)

    def quit_pygame(self):
        pygame.quit()