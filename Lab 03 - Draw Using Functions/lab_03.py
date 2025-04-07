import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_shooting_strings(x, y):
    arcade.draw_line(x - 66, y + 40, x + 66, y + 40, arcade.csscolor.DARK_BLUE)
    arcade.draw_line(x - 72, y + 25, x + 71, y + 25, arcade.csscolor.DARK_GRAY)

def draw_ball(x, y):
    arcade.draw_circle_filled(x, y - 30, 40, arcade.csscolor.ORANGE)

def draw_stick(x, y):
    arcade.draw_lrtb_rectangle_filled(x - 15, x + 15, y - 60, y - 360, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(x - 15, x + 15, y - 210, y - 360, arcade.csscolor.WHITE)

def draw_head(x, y):
    arcade.draw_ellipse_filled(x, y, 150, 175, arcade.csscolor.GRAY)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()

    draw_stick(300, 360)

    draw_head(300, 360)

    draw_ball(300, 360)

    draw_shooting_strings(300, 360)
# Finish drawing
    arcade.finish_render()

# Keep the window up until someone closes it.
    arcade.run()
    # Keep the window up until someone closes it.

#Call main function to start program
main()