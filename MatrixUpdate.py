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
		
		# This gives the address array, which needs to be undone to put into same state as buffer	
		tmp_buf = [[0, 0, 0, 1.0] for x in range(self._width * self._height)]

		for iadd, out in enumerate(output):
			i,rgb = self._find_buffer(iadd)
			print (i,rgb,iadd,out)
			if i == None:
				continue
			tmp_buf[i][rgb] = out
		print (tmp_buf)
		print (self.buf)

	def _find_buffer(self, iaddress):
		print (f"Find location of address {iaddress} relative to pixel")
		lookup = [(118, 69, 85),
				  (117, 68, 101),
				  (116, 84, 100),
				  (115, 83, 99),
				  (114, 82, 98),
				  (113, 81, 97),
				  (112, 80, 96),
				  (134, 21, 37),
				  (133, 20, 36),
				  (132, 19, 35),
				  (131, 18, 34),
				  (130, 17, 50),
				  (129, 33, 49),
				  (128, 32, 48),
				  (127, 47, 63),
				  (121, 41, 57),
				  (122, 25, 58),
				  (123, 26, 42),
				  (124, 27, 43),
				  (125, 28, 44),
				  (126, 29, 45),
				  (15, 95, 111),
				  (8, 89, 105),
				  (9, 90, 106),
				  (10, 91, 107),
				  (11, 92, 108),
				  (12, 76, 109),
				  (13, 77, 93),]
		for i,(r,g,b) in enumerate(lookup):
			if r == iaddress:
				return i,0
			elif g == iaddress:
				return i,1
			elif b == iaddress:
				return i,2
			else:
				continue
		print (f"Error for {iaddress}")
		return None,None

	def _update_and_show(self):
		"""Return the current state of the display, merge with any updates in the buffer and show"""
		# This will read the matrix and update the buffer (this will overwrite any set_pixel changes)
		self._get_current_state()
		self.show()



if __name__ == "__main__":
	test = MatrixUpdate()
	test.setup()
	test._update_and_show()