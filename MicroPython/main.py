"""
Created by: Emre Guzel
Created on: Nov 5 2024
This module is a Micro:bit MicroPython program This program moves pixels
"""

# Librairie
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
        # Reseting the loopTrun
        loopTurn = 0
        # Setting the pixels of microbit

        # Setting the loop for turn
        while loopTurn < 4:
            display.clear
            display.set_pixel(x, y, 9)
            sleep(500)
            # Reseting the loopMove
            loopMove = 0
            # Setting the MoveLopp that way the pixels start to move
            while loopMove < 4:
                # Set direction
                if loopTurn == 0:  # Move right
                    x = (x + 1) % 5
                elif loopTurn == 1:  # Move down
                    y = (y + 1) % 5
                elif loopTurn == 2:  # Move left
                    x = (x - 1) % 5
                elif loopTurn == 3:  # Move up
                    y = (y - 1) % 5
                display.clear()
                # Move
                display.set_pixel(x, y, 9)
                loopMove += 1
                sleep(500)
            loopTurn += 1
        display.clear
        display.show(Image.HAPPY)
