#!/bin/env python3
# This script will only be used to move through the frames
# which are currently being populated
from matrix_driver import matrix5x5
from time import sleep

# Extend this list to include additional frames (0->7)
frames = [0,1]
# Time to rest on each frame
display_wait = 20

if __name__ == "__main__":
	# Using busio and board to allow lock on the display
	import busio
	import board
	# Attach to the device
	display = matrix5x5(busio.I2C(board.SCL, board.SDA), 0x74)
	while True:
		for f in frames:
			display.frame(f)
			sleep(display_wait)