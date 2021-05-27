from rgbmatrix5x5 import RGBMatrix5x5
_MODE_REGISTER = 0x00
_FRAME_REGISTER = 0x01
_AUTOPLAY1_REGISTER = 0x02
_AUTOPLAY2_REGISTER = 0x03
_BLINK_REGISTER = 0x05
_AUDIOSYNC_REGISTER = 0x06
_BREATH1_REGISTER = 0x08
_BREATH2_REGISTER = 0x09
_SHUTDOWN_REGISTER = 0x0a
_GAIN_REGISTER = 0x0b
_ADC_REGISTER = 0x0c

_CONFIG_BANK = 0x0b
_BANK_ADDRESS = 0xfd

_PICTURE_MODE = 0x00
_AUTOPLAY_MODE = 0x08
_AUDIOPLAY_MODE = 0x18

_ENABLE_OFFSET = 0x00
_BLINK_OFFSET = 0x12
_COLOR_OFFSET = 0x24
class MatrixUpdate(RGBMatrix5x5):
	"""Updated class to adjust some of the access to the LEDs"""
	""" https://buildmedia.readthedocs.org/media/pdf/smbus2/latest/smbus2.pdf """
	def _get_current_state(self):
		"""Read the current buffer back from the LED"""
		output = [] # Size is 144
		for offset in range(0,128,32):
			print (offset)
			output.extend ( self.i2c.read_i2c_block_data(self.address, _COLOR_OFFSET + offset, 32) )
		output.extend ( self.i2c.read_i2c_block_data(self.address, _COLOR_OFFSET + 128, 16) )

		print (len(output))
		print (output)
		
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
		self.buf = tmp_buf
		print (self.buf)

	def _find_buffer(self, iaddress):
		#print (f"Find location of address {iaddress} relative to pixel")
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
		#print (f"Error for {iaddress}")
		return None,None

	def _update_and_show(self):
		"""Return the current state of the display, merge with any updates in the buffer and show"""
		# This will read the matrix and update the buffer (this will overwrite any set_pixel changes)
		self._get_current_state()
		#self.show()

def setup(self):
        """Set up device."""
        if self._is_setup:
            return True

        self._is_setup = True

        if self.i2c is None:
            try:
                import smbus
            except ImportError:
                if version_info[0] < 3:
                    raise ImportError('This library requires python-smbus\nInstall with: sudo apt-get install python-smbus')
                elif version_info[0] == 3:
                    raise ImportError('This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus')

            try:
                self.i2c = smbus.SMBus(1)
            except IOError as e:
                if hasattr(e, 'errno') and e.errno == 2:
                    e.strerror += "\n\nMake sure you've enabled i2c in your Raspberry Pi configuration.\n"
                raise e

        try:
            self._reset()
        except IOError as e:
            if hasattr(e, 'errno') and e.errno == 5:
                e.strerror += '\n\nMake sure your LED SHIM is attached, and double-check your soldering.\n'
            raise e

        #self.show()

        # Display initialization

        # Switch to configuration bank
        self._bank(_CONFIG_BANK)

        # Switch to Picture Mode
        self.i2c.write_i2c_block_data(self.address, _MODE_REGISTER, [_PICTURE_MODE])

        # Disable audio sync
        self.i2c.write_i2c_block_data(self.address, _AUDIOSYNC_REGISTER, [0])

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

        # Switch to bank 1 ( frame 1 )
        self._bank(1)

        # Enable LEDs
        self.i2c.write_i2c_block_data(self.address, 0x00, enable_pattern)

        # Switch to bank 0 ( frame 0 )
        self._bank(0)

        # Enable LEDs
        self.i2c.write_i2c_block_data(self.address, 0x00, enable_pattern)

        try:
            atexit.register(self._exit)
        except NameError:
            pass




if __name__ == "__main__":
	test = MatrixUpdate()
	test.setup()
	test._update_and_show()