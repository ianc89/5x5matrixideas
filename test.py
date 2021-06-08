from matrix_driver import matrix5x5

if __name__ == "__main__":
	# Using busio and board to allow lock on the display
	import busio
	import board
	display = matrix5x5(busio.I2C(board.SCL, board.SDA), 0x74)
	# Test frame switching (seems to function)
	display.frame(2)
	# Turns on all the LED (adjust colour with values)
	for x in range(display.width):
		for y in range(display.height):
			display.set_pixel(x,y,1,20,80,frame=2)


