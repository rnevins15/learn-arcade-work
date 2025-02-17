"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade
from arcade.key import RIGHT

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Lab")

# Set the background color
arcade.set_background_color(arcade.csscolor.BLUE)

# Get ready to draw
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
arcade.draw_circle_filled(300,330, 40,arcade.csscolor.ORANGE)
# Draw shooting strings
arcade.draw_line(234,400,366, 400, arcade.csscolor.DARK_BLUE)

arcade.draw_line(228,385,371, 385, arcade.csscolor.DARK_GRAY)
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()