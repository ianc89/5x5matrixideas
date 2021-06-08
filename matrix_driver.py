""" Class to drive the matrix """
from adafruit_is31fl3731 import IS31FL3731
from matrix_properties import properties
""" https://circuitpython.readthedocs.io/projects/is31fl3731/en/latest/_modules/adafruit_is31fl3731.html#IS31FL3731 """

class matrix5x5(IS31FL3731):
	width = 5
	height = 5

	def __init__(self, i2c, address=0x74):
		super().__init__(i2c, address)
		self.properties = properties()

	def set_pixel(self,x,y,r=0,g=0,b=0,blink=None,frame=None):
		rgb_loc = self.properties.pixel[(x,y)]
		rgb = self.properties.lookup[rgb_loc]
		super().pixel(rgb,0,r,blink,frame)
		super().pixel(rgb,1,g,blink,frame)
		super().pixel(rgb,2,b,blink,frame)

	@staticmethod
	def pixel_addr(x, y):
		# Note this required to comment out the size check inside the main driver
		return x[y]