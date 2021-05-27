from rgbmatrix5x5 import RGBMatrix5x5
_ENABLE_OFFSET = 0x00
_BLINK_OFFSET = 0x12
_COLOR_OFFSET = 0x24
class MatrixUpdate(RGBMatrix5x5):
	"""Updated class to adjust some of the access to the LEDs"""
	""" https://buildmedia.readthedocs.org/media/pdf/smbus2/latest/smbus2.pdf """
	def _get_current_state(self):
		"""Read the current buffer back from the LED"""
		output = []
		for offset in range(0,144,32):
			output.extend ( self.i2c.read_i2c_block_data(self.address, _COLOR_OFFSET + offset, 32) )
			
		print (f"Address {self.address}")
		for value in output:
			print (value)
		return output

	def _update_and_show(self):
		"""Return the current state of the display, merge with any updates in the buffer and show"""
		# Local pixel updates : self.buf
		# Device status : _get_current_state()
		# If we have been careful to not touch each others state, we should be able to add together
		for local_pix, global_pix in zip(self.buff, self._get_current_state()):
			print (local_pix, global_pix)


if __name__ == "__main__":
	test = MatrixUpdate()
	test.setup()
	test._get_current_state()
	test._update_and_show()