from adafruit_is31fl3731 import IS31FL3731
from matrix_properties import properties

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
		return x[y]

if __name__ == "__main__":
	import busio
	import board
	import time
	display = matrix5x5(busio.I2C(board.SCL, board.SDA), 0x74)
	for x in range(display.width):
		for y in range(display.height):
			#print (x,y)
			#rgb_loc = properties.pixel[(x,y)]
			#rgb = properties.lookup[rgb_loc]
			#display.pixel(rgb,0,50)
			#time.sleep(1)
			#display.pixel(rgb,1,50)
			#time.sleep(1)
			#display.pixel(rgb,2,50)
			#time.sleep(1)
			display.set_pixel(x,y,50,50,50,frame=2)


