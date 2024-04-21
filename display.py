import pygame

class DataWindow:
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((500, 700))
        pygame.display.set_caption("Joystick example")

        self.text_print = TextPrint()
    
    def clear_display(self):
        # Drawing step
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        self.screen.fill((255, 255, 255))
        self.text_print.reset()

    def update_display(self):
        pygame.display.flip()

    def print_string(self, data):
        self.text_print.tprint(self.screen, data)

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