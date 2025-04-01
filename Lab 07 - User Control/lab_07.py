""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """


        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.set_background_color(arcade.csscolor.BLUE)
        arcade.start_render()
        # Draw a rectangle
        # Left of 285, right of 315
        # Top of 300, bottom of 0
        # Draw a Lacrosse shaft
        arcade.draw_lrtb_rectangle_filled(285, 315, 300, 0, arcade.csscolor.BLACK)
        # Draw Tape on shaft
        arcade.draw_lrtb_rectangle_filled(285, 315, 150, 0, arcade.csscolor.WHITE)
        # Draw Lacrosse head
        arcade.draw_ellipse_filled(300, 360, 150, 175, arcade.csscolor.GRAY)
        # Draw a Lacrosse ball
        arcade.draw_circle_filled(300, 330, 40, arcade.csscolor.ORANGE)
        # Draw shooting strings
        arcade.draw_line(234, 400, 366, 400, arcade.csscolor.DARK_BLUE)

        arcade.draw_line(228, 385, 371, 385, arcade.csscolor.DARK_GRAY)
        # Finish drawing
        arcade.finish_render()


def main():
    window = MyGame()
    arcade.run()


main()