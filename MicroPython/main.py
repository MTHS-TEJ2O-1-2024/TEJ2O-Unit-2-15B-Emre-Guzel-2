"""
Created by: Emre Guzel
Created on: Nov 5 2024
This module is a Micro:bit MicroPython program This program moves pixels
"""

# Liyberies 
from microbit import *
import game
import sprite

# Setting the varibles
loopMove = 0
loopTurn = 0

# setting the screen
display.clear()
display.show(Image.HAPPY)

# Setting the while loop for button a.
while True:
    if button_a.is_pressed():
        display.clear()
        # Setting the spirte game
        sprit = game.create_sprite(0, 0)
        # Reseting the loopTrun
        loopTurn = 0
        sprite.set(LedSpriteProperty.X, 0)
