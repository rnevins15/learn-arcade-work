import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_shooting_strings():
    arcade.draw_line(234, 400, 366, 400, arcade.csscolor.DARK_BLUE)
    arcade.draw_line(228, 385, 371, 385, arcade.csscolor.DARK_GRAY)

def draw_ball():
    arcade.draw_circle_filled(300, 330, 40, arcade.csscolor.ORANGE)

def draw_stick():
    arcade.draw_lrtb_rectangle_filled(285, 315, 300, 0, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(285, 315, 150, 0, arcade.csscolor.WHITE)
def draw_head():
    arcade.draw_ellipse_filled(300, 360, 150, 175, arcade.csscolor.GRAY)

def on_draw(delta_time):
    arcade.start_render()
    draw_stick()
    draw_head()
    draw_ball()
    draw_shooting_strings()

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()

    draw_stick()

    draw_head()

    draw_ball()

    draw_shooting_strings()
# Finish drawing
    arcade.finish_render()

# Keep the window up until someone closes it.
    arcade.run()

#Call main function to start program
main()