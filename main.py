player = game.create_sprite(randint(4, 2), 0)

def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)