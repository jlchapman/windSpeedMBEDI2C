import smbus
import time

class BBB_WINDMBED:
    """A basic class used for interacting with MBED doing 
    windspeed and direction."""

    def __init__(self, address, bus=0):
        self.address = address
        self.i2cbus = smbus.SMBus(bus)
        
    def get_interrupt(self):
        self.read_data()
        return self.registers[0x03] & 0x0F

    def get_distance(self):
        self.read_data()
        if self.registers[0x07] & 0x3F == 0x3F:
            return False
        else:
            return self.registers[0x07] & 0x3F


    def set_byte(self, register, value):
        self.i2cbus.write_byte_data(self.address, register, value)

    def read_data(self):
        self.registers = self.i2cbus.read_i2c_block_data(self.address, 0x00)
