import serial

class UART:

    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
        self.ser.reset_input_buffer()

    def read_serial(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            print(line)

    def write_serial(self, msg):
        with_end = msg + '\n'
        self.ser.write(with_end.encode('utf-8'))