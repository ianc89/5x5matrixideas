#!/usr/bin/env python
import time
from datetime import datetime
# Using busio and board to allow lock on the display
from matrix_driver import matrix5x5
import busio
import board


print("""
Clock.py
Light up pixels in the first two rows as a binary clock
First row is hour
Second row is minutes, with colour variant for 0-30,31-60
Press Ctrl+C to exit!
""")

# Attach to the device
rgbmatrix5x5 = matrix5x5(busio.I2C(board.SCL, board.SDA), 0x74)
# Place into initial display frame
rgbmatrix5x5.frame(0)
y_hour   = 0
y_minute = 1
y_second = 2

# Quick colour setup
colours = {}
colours["Black"] = (0,0,0)	
colours["White"] = (255,255,255)	
colours["Red"] = (255,0,0)	
colours["Lime"] = (0,255,0)	
colours["Blue"] = (0,0,255)	
colours["Yellow"] = (255,255,0)	
colours["Cyan"] = (0,255,255)
colours["Magenta"] = (255,0,255) 	
colours["Silver"] = (192,192,192)	
colours["Gray"] = (128,128,128)	
colours["Maroon"] = (128,0,0)	
colours["Olive"] = (128,128,0)	
colours["LightGreen"] = (102,255,102)
colours["Green"] = (0,128,0)	
colours["DarkGreen"] = (0,102,0)	
colours["LightPurple"] = (228,142,228)
colours["Purple"] = (128,0,128)	
colours["Teal"] = (0,128,128)	
colours["Navy"] = (0,0,128)	
colours["Orange"] = (255,165,0)

c_hour  = colours["Red"]
c_min_1 = colours["LightGreen"]
c_min_2 = colours["Green"]
c_sec_1 = colours["LightPurple"]
c_sec_2 = colours["Purple"]

def get_pixel(value):
	above_30 = False
	if value > 30:
		above_30 = True
		value = value-30
	# Now convert to binary and pad to 5 digits to right (with 0 on the left, and then reverse)
	bval = bin(value)[2:].rjust(5,"0")[::-1]
	return bval, above_30


while True:
	# Get the time
	now    = datetime.now()
	hour   = now.hour
	minute = now.minute
	second = now.second
	# Convert to binary points (on/off)
	b_hour, hour_over_30     = get_pixel(hour)
	b_minute, minute_over_30 = get_pixel(minute)
	b_second, second_over_30 = get_pixel(second)
	# Activate lights
	# set pixel - x,y,r,g,b,brightness (used to switch off instead of clear)
	for x in range(5):
		# Hour
		if b_hour[x] == "1":
			rgbmatrix5x5.set_pixel(y_hour, x, c_hour[0], c_hour[1], c_hour[2], frame=0)
		else:
			rgbmatrix5x5.set_pixel(y_hour, x, 0, 0, 0, frame=0)
		# Minutes
		if b_minute[x] == "1":
			if minute_over_30:
				rgbmatrix5x5.set_pixel(y_minute, x, c_min_2[0], c_min_2[1], c_min_2[2], frame=0)
			else:
				rgbmatrix5x5.set_pixel(y_minute, x, c_min_1[0], c_min_1[1], c_min_1[2], frame=0)
		else:
			rgbmatrix5x5.set_pixel(y_minute, x, 0, 0, 0, frame=0)
		# Seconds
		if b_second[x] == "1":
			if second_over_30:
				rgbmatrix5x5.set_pixel(y_second, x, c_sec_2[0], c_sec_2[1], c_sec_2[2], frame=0)
			else:
				rgbmatrix5x5.set_pixel(y_second, x, c_sec_1[0], c_sec_1[1], c_sec_1[2], frame=0)
		else:
			rgbmatrix5x5.set_pixel(y_second, x, 0, 0, 0, frame=0)
	# If only showing minutes
	# time.sleep(20)
	# If showing seconds
	time.sleep(1)

