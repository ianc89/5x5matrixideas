from rgbmatrix5x5 import RGBMatrix5x5
_ENABLE_OFFSET = 0x00
_BLINK_OFFSET = 0x12
_COLOR_OFFSET = 0x24
class MatrixUpdate(RGBMatrix5x5):
	"""Updated class to adjust some of the access to the LEDs"""
	""" https://buildmedia.readthedocs.org/media/pdf/smbus2/latest/smbus2.pdf """
	def _get_current_state(self):
		output = []
		for offset in range(0,144,32):
			output.extend ( self.i2c.read_i2c_block_data(self.address, _COLOR_OFFSET + offset, 32) )
			
		print (f"Address {self.address}")
		for value in output:
			print (value)

if __name__ == "__main__":
	test = MatrixUpdate()
	test.setup()
	test._get_current_state()