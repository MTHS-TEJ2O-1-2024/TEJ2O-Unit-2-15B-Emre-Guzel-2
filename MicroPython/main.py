"""
Created by: Emre Guzel
Created on: Nov 5 2024
This module is a Micro:bit MicroPython program This program moves pixels
"""

# Librarie
from microbit import *

# Setting the variables
loopMove = 0
loopTurn = 0
x = 0
y = 0
# setting the screen
display.clear()
display.show(Image.HAPPY)

# Setting the while loop for button a.
while True:
    if button_a.is_pressed():
        display.clear()
        # It allows the progam to move horizantely
        x = (x + 1) % 5
        # Reseting the loopTrun
        loopTurn = 0
        # Setting the pixels of microbit
        display.set_pixel(x, y, 0)
        sleep(500)

        # Setting the loop for turn
        while loopTurn < 4:
            # Reseting the loopMove
            loopMove = 0
            # Setting the MoveLopp that way the pixels start to move
            while loopMove < 5:
                display.move(1)
                loopMove +=1
                sleep(500)
