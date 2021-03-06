""" Class to hold properties for the driver """
""" https://www.issi.com/WW/pdf/31FL3731.pdf """

class properties():
	def __init__(self):
		# Addresses for registers
		self._FRAME_0   = 0x00
		self._FRAME_1   = 0x01
		self._FRAME_2   = 0x02
		self._FRAME_3   = 0x03
		self._FRAME_4   = 0x04
		self._FRAME_5   = 0x05
		self._FRAME_6   = 0x06
		self._FRAME_7   = 0x07
		self._FRAME_8   = 0x08

		# Addresses for function register
		self._MODE_REGISTER      = 0x00
		self._FRAME_REGISTER     = 0x01
		self._AUTOPLAY1_REGISTER = 0x02
		self._AUTOPLAY2_REGISTER = 0x03
		self._BLINK_REGISTER     = 0x05
		self._AUDIOSYNC_REGISTER = 0x06
		self._BREATH1_REGISTER   = 0x08
		self._BREATH2_REGISTER   = 0x09
		self._SHUTDOWN_REGISTER  = 0x0a
		self._GAIN_REGISTER      = 0x0b
		self._ADC_REGISTER       = 0x0c

		# Config bank == Function register
		self._CONFIG_BANK        = 0x0b
		self._BANK_ADDRESS       = 0xfd

		# Functions in configuration register
		self._PICTURE_MODE       = 0x00 # This is technically only for frame 0
		self._AUTOPLAY_MODE      = 0x08
		self._AUDIOPLAY_MODE     = 0x18
		self._ENABLE_OFFSET      = 0x00
		self._BLINK_OFFSET       = 0x12
		self._COLOR_OFFSET       = 0x24
		# Size
		self.width  = 5
		self.height = 5
		# Gamma (intensity steps for better shifting for human eye, I think)
		self.LED_GAMMA = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
						  0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
						  2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
						  6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 11, 11,
						  11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18,
						  19, 19, 20, 21, 21, 22, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28,
						  29, 29, 30, 31, 31, 32, 33, 34, 34, 35, 36, 37, 37, 38, 39, 40,
						  40, 41, 42, 43, 44, 45, 46, 46, 47, 48, 49, 50, 51, 52, 53, 54,
						  55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
						  71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 88, 89,
						  90, 91, 93, 94, 95, 96, 98, 99, 100, 102, 103, 104, 106, 107, 109, 110,
						  111, 113, 114, 116, 117, 119, 120, 121, 123, 124, 126, 128, 129, 131, 132, 134,
						  135, 137, 138, 140, 142, 143, 145, 146, 148, 150, 151, 153, 155, 157, 158, 160,
						  162, 163, 165, 167, 169, 170, 172, 174, 176, 178, 179, 181, 183, 185, 187, 189,
						  191, 193, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220,
						  222, 224, 227, 229, 231, 233, 235, 237, 239, 241, 244, 246, 248, 250, 252, 255)
		# LED pixel buffer location (x,y)->buffer
		self.pixel = {(0,0) : 0,
					  (1,0) : 9, 
					  (2,0) : 10, 
					  (3,0) : 19, 
					  (4,0) : 20, 
					  (0,1) : 1, 
					  (1,1) : 8, 
					  (2,1) : 11, 
					  (3,1) : 18, 
					  (4,1) : 21, 
					  (0,2) : 2, 
					  (1,2) : 7, 
					  (2,2) : 12, 
					  (3,2) : 17, 
					  (4,2) : 22, 
					  (0,3) : 3, 
					  (1,3) : 6, 
					  (2,3) : 13, 
					  (3,3) : 16, 
					  (4,3) : 23, 
					  (0,4) : 4, 
					  (1,4) : 5, 
					  (2,4) : 14, 
					  (3,4) : 15, 
					  (4,4) : 24,}
		# buffer location to address (index)->[r,g,b]
		self.lookup = [(118, 69, 85),
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
