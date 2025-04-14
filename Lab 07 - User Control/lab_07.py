""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

# Load sounds
CLICK_SOUND = arcade.load_sound(":resources:sounds/coin1.wav")
EDGE_SOUND = arcade.load_sound(":resources:sounds/hurt3.wav")

# --- Drawing Functions ---

def draw_background():
    """Draw the background scene: sky, grass, and sun"""
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 100, 0, arcade.color.DARK_SPRING_GREEN)  # Grass
    arcade.draw_circle_filled(700, 500, 50, arcade.color.GOLD)  # Sun

# --- Game Object Classes ---

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.edge_sound_played = False

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        # Check for screen boundaries
        hit_edge = False

        if self.x < 0:
            self.x = 0
            hit_edge = True
        elif self.x > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH
            hit_edge = True

        if self.y < 0:
            self.y = 0
            hit_edge = True
        elif self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            hit_edge = True

        # Play edge sound if we just hit the edge
        if hit_edge and not self.edge_sound_played:
            arcade.play_sound(EDGE_SOUND)
            self.edge_sound_played = True
        elif not hit_edge:
            self.edge_sound_played = False

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, 60, 30, arcade.color.GRAY)
        arcade.draw_triangle_filled(self.x + 30, self.y, self.x + 50, self.y + 10, self.x + 50, self.y - 10, arcade.color.RED)

class UFO:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, 60, 30, arcade.color.LIGHT_GRAY)
        arcade.draw_circle_filled(self.x, self.y + 10, 10, arcade.color.GREEN)

# --- Main Game Window ---

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.spaceship = Spaceship(100, 150)
        self.ufo = UFO(400, 300)

    def on_draw(self):
        arcade.start_render()
        draw_background()
        self.spaceship.draw()
        self.ufo.draw()

    def on_update(self, delta_time):
        self.spaceship.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.spaceship.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.spaceship.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.spaceship.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.spaceship.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.spaceship.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.spaceship.change_x = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.ufo.set_position(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(CLICK_SOUND)

# --- Main Function ---
def main():
    window = MyGame()
    arcade.run()

main()
