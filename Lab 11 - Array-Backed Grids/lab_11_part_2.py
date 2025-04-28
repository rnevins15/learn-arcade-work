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

    def on_mouse_press(self, x, y, button, modifiers):
        # Change the clicked cell
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        if 0 <= row < ROW_COUNT and 0 <= column < COLUMN_COUNT:
            # Flip the cell
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        # Count all selected cells
        selected_count = 0
        for row in self.grid:
            for cell in row:
                if cell == 1:
                    selected_count += 1

        print(f"Total selected cells: {selected_count}")

        # Count selected cells in each row
        for row_index, row in enumerate(self.grid):
            row_selected_count = 0
            for cell in row:
                if cell == 1:
                    row_selected_count += 1
            print(f"Row {row_index} has {row_selected_count} selected cells.")

        # Count selected cells in each column
        for col_index in range(COLUMN_COUNT):
            column_selected_count = 0
            for row in self.grid:
                if row[col_index] == 1:
                    column_selected_count += 1
            print(f"Column {col_index} has {column_selected_count} selected cells.")

        # Track continuous selected cells in each row
        for row_index, row in enumerate(self.grid):
            continuous_count = 0  # Reset continuous count for each row
            for col_index, cell in enumerate(row):
                if cell == 1:
                    continuous_count += 1
                else:
                    # If we hit a 0, check if the continuous count is greater than 2
                    if continuous_count > 2:
                        print(f"Row {row_index} has {continuous_count} continuous selected cells from column {col_index - continuous_count} to column {col_index - 1}.")
                    # Reset continuous count
                    continuous_count = 0

            # After finishing the row, check if there's a continuous sequence at the end
            if continuous_count > 2:
                print(f"Row {row_index} has {continuous_count} continuous selected cells from column {COLUMN_COUNT - continuous_count} to column {COLUMN_COUNT - 1}.")

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()

