import math

class Servo:
    
    # range_min and range_max are microsecond duty cycle limits for the servo
    def __init__(self, range_min, range_max):
        self.range_min = range_min
        self.range_max = range_max
        
        self.home_pos = math.floor((self.range_min + self.range_max) / 2)
        self.curr_pos = self.home_pos
        
        self.deadband = 3
        self.multiplier = 1
        
        self.homed = False

    # Increment is a positive value
    def increase_pos(self, increment):
        if(abs(increment) > self.deadband):
            if(self.curr_pos + increment - self.deadband < self.range_max): self.curr_pos += increment*self.multiplier - self.deadband
            else: self.curr_pos = self.range_max

    # Decrement is a negative value
    def decrease_pos(self, decrement):
        if(abs(decrement) > self.deadband):
            if(self.curr_pos + decrement + self.deadband > self.range_min): self.curr_pos += decrement*self.multiplier + self.deadband
            else: self.curr_pos = self.range_min

    def home_servo(self):
        self.curr_pos = self.home_pos
        self.homed = True