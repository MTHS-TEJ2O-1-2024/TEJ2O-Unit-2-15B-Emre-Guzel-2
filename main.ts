/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Emre Guzel
 * Created on: Oct 31 2024
 * This program moves pixels
*/

// Setting the varibels
let sprite: game.LedSprite = null
//let loopCounter = 0
let xcnt = 0
let ycnt = 0

// Setting the screen
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// Setting the while loop for button a.
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    sprite = game.createSprite(0, 0)
    let cntTurn = 0;
    //blink on the first led
    sprite.set(LedSpriteProperty.X, 0)
    basic.pause(500)
    //loop for turn
    while (cntTurn < 4) {
        let cntMove = 0;
        //loop for move
        while (cntMove < 5) {
            sprite.move(1)
            cntMove++;
            basic.pause(500)
        }
        sprite.turn(Direction.Right, 90)
        cntTurn++
    }
    sprite.delete()
    basic.showIcon(IconNames.Happy)
})