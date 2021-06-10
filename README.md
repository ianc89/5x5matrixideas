# 5x5matrixideas
## Matrix driver and properties
Adapted driver moving from pimoroni to adafruit
https://circuitpython.readthedocs.io/projects/is31fl3731/en/latest/index.html
    - matrix_driver.py provides a new class to use the 5x5 matrix with, where you set pixel LED but only show when the frame is active. At the moment, this is compatible with multiple scripts touching different frames.
    - matrix_properties.py pulls the pixel address information from pimoroni class to be used on the fly
    - display.py is a simple script to run simultaneously and control switching the frames
## Clock
A binary clock using row 0,1,2 to display hour,minute,second
    - clock.py uses pimoroni
    - clock_2.py uses matrix_driver
