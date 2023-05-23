let player = game.createSprite(randint(4, 2), 0)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    player.move(-1)
})
