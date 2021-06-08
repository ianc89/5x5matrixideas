from adafruit_is31fl3731 import IS31FL3731

class matrix5x5(IS31FL3731):
	width = 5
	height = 5
	@staticmethod
	def pixel_addr(x, y):
		pixel = {(0,0) : 0,
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
		return pixel[(x,y)]


if __name__ == "__main__":
	display = matrix5x5()
	# draw a box on the display
	# first draw the top and bottom edges
	for x in range(display.width):
		display.pixel(x, 0, 50)
		display.pixel(x, display.height - 1, 50)
	# now draw the left and right edges
		for y in range(display.height):
			display.pixel(0, y, 50)
			display.pixel(display.width - 1, y, 50)