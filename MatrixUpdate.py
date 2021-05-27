from rgbmatrix5x5 import RGBMatrix5x5
class MatrixUpdate(RGBMatrix5x5):
	"""Updated class to adjust some of the access to the LEDs"""
	""" https://buildmedia.readthedocs.org/media/pdf/smbus2/latest/smbus2.pdf """
	def _get_current_state():
		output = []
		for offset in range(0,144,32):
			output.extend ( self.i2c.read_i2c_block_data(self.address, _COLOR_OFFSET + offset, 32) )
			
		print (f"Address {self.address}")
		for value in output:
			print (value)