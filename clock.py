#!/usr/bin/env python
import time
from rgbmatrix5x5 import RGBMatrix5x5
from datetime import datetime

print("""
Clock.py
Light up pixels in the first two rows as a binary clock
First row is hour
Second row is minutes, with colour variant for 0-30,31-60
Press Ctrl+C to exit!
""")

rgbmatrix5x5 = RGBMatrix5x5()
y_hour = 0
y_minute = 1

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
colours["Green"] = (0,128,0)	
colours["Purple"] = (128,0,128)	
colours["Teal"] = (0,128,128)	
colours["Navy"] = (0,0,128)	

c_hour  = colours["White"]
c_min_1 = colours["Blue"]
c_min_2 = colours["Green"]

def get_pixel(value):
	above_30 = False
	if value > 30:
		above_30 = True
		value = value-30
	# Now convert to binary and pad to 5 digits to right
	bval = bin(value)[2:].ljust(5,"0")
	return bval, above_30


while True:
	# Get the time
	now = datetime.now()
	hour = now.hour
	minute = now.minute
	# Convert to binary points (on/off)
	b_hour, hour_over_30   = get_pixel(hour)
	b_minute, minute_over_30 = get_pixel(minute)
	# Activate lights
	# Hour
	for x in range(5):
		#rgbmatrix5x5.clear()
		# set pixel - x,y,r,g,b,brightness (used to switch off instead of clear)
		rgbmatrix5x5.set_pixel(y_hour, x, c_hour[0], c_hour[1], c_hour[2], int(b_hour[x]))
		if minute_over_30:
			rgbmatrix5x5.set_pixel(y_minute, x, c_min_1[0], c_min_1[1], c_min_1[2], int(b_minute[x]))
		else:
			rgbmatrix5x5.set_pixel(y_minute, x, c_min_2[0], c_min_2[1], c_min_2[2], int(b_minute[x]))
		rgbmatrix5x5.show()
	time.sleep(20)

