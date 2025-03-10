import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)

def draw_section_1():
    #Grid of white squares
    for row in range(30):
        for col in range(30):
            x = 5 + col * 10
            y = 5 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    #Grid of black and white squares every other column
    for row in range(30):
        for col in range(30):
            x = 305 + col * 10
            y = 5 + row * 10
            color = arcade.color.WHITE if col % 2 == 0 else arcade.color.BLACK
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_3():
    #Grid of black and white squares every other row
    for row in range(30):
        for col in range(30):
            x = 605 + col * 10
            y = 5 + row * 10
            color = arcade.color.WHITE if row % 2 == 0 else arcade.color.BLACK
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_4():
    #Every other row and column all black
    for row in range(30):
        for col in range(30):
            # Make the entire row black every other row
            if row % 2 == 0:
                color = arcade.color.BLACK
            # Make the entire column black every other column
            elif col % 2 == 0:
                color = arcade.color.BLACK
            else:
                color = arcade.color.WHITE
            x = 905 + col * 10
            y = 5 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, color)

def draw_section_5():
    #Right triangle facing left
    for row in range(30):
        for col in range(30 - row):
            if col == 30 - row - 1:
                continue
            x = 295 - col * 10
            y = 305 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    #Right triangle facing right
    for row in range(30):
        for col in range(30 - row):
            x = 305 + col * 10
            y = 305 + row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_7():
    #Section 6 flipped
    for row in range(30):
        for col in range(30 - row):
            x = 605 + col * 10
            y = 595 - row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    #Section 5 flipped
    for row in range(30):
        for col in range(30 - row):
            x = 1195 - col * 10
            y = 595 - row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    #Create window
    arcade.open_window(1200, 600, "Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines and sections
    draw_section_outlines()
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()
    arcade.run()


main()