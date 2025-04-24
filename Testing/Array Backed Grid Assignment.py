import arcade


WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10
SCREEN_HEIGHT = COLUMN_COUNT * HEIGHT + MARGIN * (COLUMN_COUNT + 1)
SCREEN_WIDTH = ROW_COUNT * HEIGHT + MARGIN * (ROW_COUNT + 1)



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        for column in range(COLUMN_COUNT):
            x = column * WIDTH + WIDTH / 2 + (column + 1) * MARGIN
            for row in range(ROW_COUNT):
                y = row * HEIGHT + HEIGHT / 2 + (row + 1) * MARGIN
                color = arcade.color.WHITE
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_RIGHT:
            column = x // (WIDTH + MARGIN)
            row = y // (HEIGHT + MARGIN)
            print(f"Click Coordinates: ({x}, {y}). Grid coordinates: ({row}, {column}).")
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()