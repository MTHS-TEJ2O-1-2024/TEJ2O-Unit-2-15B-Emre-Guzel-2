/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Emre Guzel
 * Created on: Oct 31 2024
 * This program moves pixels
*/

// Setting the varibels
let sprite: game.LedSprite = null
let loopMove = 0
let loopTurn = 0

// Setting the screen
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// Setting the while loop for button a.
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    sprite = game.createSprite(0, 0)
    let loopTurn = 0;
    //blink on the first led
    sprite.set(LedSpriteProperty.X, 0)
    basic.pause(500)

    //loop for turn
    while (loopTurn < 4) {
        let loopMove = 0;
        //loop for move
        while (loopMove < 5) {
            sprite.move(1)
            loopMove++;
            basic.pause(500)
        }
        sprite.turn(Direction.Right, 90)
        loopTurn++
    }
    sprite.delete()
    basic.showIcon(IconNames.Happy)
})
