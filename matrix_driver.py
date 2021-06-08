""" Class to drive the matrix """
from matrix_properties import properties

class driver():
	def __init__(self, address=0x74):
		self.i2c        = None
		self.address    = address
		self.properties = properties()
		self.LED_GAMMA  = self.properties.LED_GAMMA
		self.buffer     = {}

	def switch_bank(self, bank):
		"""Switch display driver memory bank."""
		self.i2c.write_i2c_block_data(self.address, self.properties._BANK_ADDRESS, [bank])

	def setup(self):
		# Connect to the bus
		#import smbus
		#self.i2c = smbus.SMBus(1)
		import smbus2
		self.i2c = smbus2.SMBus(1)
		self.i2c.enable_pec(True)
		# Configure the chip
		# Switch to configuration bank
		self.switch_bank(self.properties._CONFIG_BANK)
		# Switch to Picture Mode
		self.i2c.write_i2c_block_data(self.address, self.properties._MODE_REGISTER, [self.properties._PICTURE_MODE])
		# Disable audio sync
		self.i2c.write_i2c_block_data(self.address, self.properties._AUDIOSYNC_REGISTER, [0])
		# Pattern (?)
		enable_pattern = [
		    0b00000000, 0b10111111,
		    0b00111110, 0b00111110,
		    0b00111111, 0b10111110,
		    0b00000111, 0b10000110,
		    0b00110000, 0b00110000,
		    0b00111111, 0b10111110,
		    0b00111111, 0b10111110,
		    0b01111111, 0b11111110,
		    0b01111111, 0b00000000,
		]
		# Loop through the banks (frames)
		for frame in range(8):
			self.switch_bank(frame)
			self.i2c.write_i2c_block_data(self.address, self.properties._FRAME_REGISTER, [frame] )
			self.i2c.write_i2c_block_data(self.address, self.properties._MODE_REGISTER, enable_pattern)

	def activate_pixel(self, frame, x, y, rgb):
		self.switch_bank(self.properties._FRAME_0)

		# Write a function which only touches LED for single pixel
		# Given x,y -> get the lookup index
		addr_loc = self.properties.pixel[(x,y)]
		print (addr_loc)
		# From the lookup index, get the rgb addresses
		ir = self.properties.lookup[addr_loc][0]
		ig = self.properties.lookup[addr_loc][1]
		ib = self.properties.lookup[addr_loc][2]
		print (ir,ig,ib)
		# Using rgb address, write data relating to activation
		self.i2c.write_byte_data(self.address, ir, rgb[0])
		self.i2c.write_byte_data(self.address, ig, rgb[1])
		self.i2c.write_byte_data(self.address, ib, rgb[2])


	def test(self):
		self.activate_pixel(0, 0,0,[200,0,0])
		self.activate_pixel(0, 0,1,[200,0,0])
		self.activate_pixel(0, 0,2,[200,0,0])
		self.activate_pixel(0, 0,3,[200,0,0])
		self.activate_pixel(0, 0,4,[200,0,0])
		self.activate_pixel(0, 4,4,[200,0,0])


		






