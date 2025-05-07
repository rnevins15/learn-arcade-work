import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 600             # Width of the game window
SCREEN_HEIGHT = 800            # Height of the game window
SCREEN_TITLE = "Falling Objects Catcher - Part 2"  # Title shown at the top of the window

PLAYER_SPEED = 5               # Speed the player moves left/right
ITEM_FALL_SPEED = 3            # Speed at which items fall down the screen
SPAWN_RATE = 0.02              # Probability each frame that an item will spawn

MAX_LIVES = 3                  # Starting number of lives for the player

# --- Sprite for falling items ---
class FallingItem(arcade.Sprite):
    def __init__(self, image, scale, item_type):
        # Initialize the parent class (arcade.Sprite)
        super().__init__(image, scale)
        self.item_type = item_type  # 'good' or 'bad' to define behavior on collision

    def update(self):
        # Move the item downward
        self.center_y -= self.change_y

        # Remove item if it falls below the screen
        if self.top < 0:
            self.remove_from_sprite_lists()

# --- Main Game Window ---
class CatchGame(arcade.Window):
    def __init__(self):
        # Set up the main game window with dimensions and title
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_BLUE)

        # Game state and sprite variables
        self.player = None              # The player's character
        self.items = None               # List of all falling items
        self.score = 0                  # Player's score
        self.lives = MAX_LIVES          # Player's remaining lives
        self.game_over = False          # Whether the game is over

        # Load sound effects
        self.catch_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/error1.wav")

    def setup(self):
        """Initial game setup: load sprites, reset score/lives."""
        # Create and place the player sprite
        self.player = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png", 0.5)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 60

        # Create an empty list for falling items
        self.items = arcade.SpriteList()

        # Reset score, lives, and game state
        self.score = 0
        self.lives = MAX_LIVES
        self.game_over = False

    def on_draw(self):
        """Render all visuals on the screen."""
        arcade.start_render()  # Start drawing

        # Draw the player and all falling items
        self.player.draw()
        self.items.draw()

        # Display score and lives
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)
        arcade.draw_text(f"Lives: {self.lives}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

        # If the game is over, display "GAME OVER"
        if self.game_over:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2,
                             arcade.color.RED, 40)

    def on_update(self, delta_time):
        """Game logic runs here every frame (60 times per second)."""
        if self.game_over:
            return  # Don't update anything if the game is over

        # --- Item spawning ---
        if random.random() < SPAWN_RATE:
            # 80% chance of spawning a good item
            if random.random() < 0.8:
                item = FallingItem(":resources:images/tiles/mushroomRed.png", 0.5, "good")
            else:
                # 20% chance of spawning a bad item
                item = FallingItem(":resources:images/tiles/bomb.png", 0.5, "bad")

            # Position the item at a random horizontal location, above the screen
            item.center_x = random.randint(20, SCREEN_WIDTH - 20)
            item.center_y = SCREEN_HEIGHT + 20
            item.change_y = ITEM_FALL_SPEED
            self.items.append(item)

        # Update positions of items and player
        self.items.update()
        self.player.update()

        # --- Check for collisions between player and items ---
        for item in self.items:
            if arcade.check_for_collision(self.player, item):
                if item.item_type == "good":
                    self.score += 1
                    arcade.play_sound(self.catch_sound)
                else:
                    self.lives -= 1
                    arcade.play_sound(self.hit_sound)
                    if self.lives <= 0:
                        self.game_over = True  # End the game
                item.remove_from_sprite_lists()  # Remove the item that was caught

    def on_key_press(self, key, modifiers):
        """Move the player left or right when arrow keys are pressed."""
        if self.game_over:
            return

        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        """Stop moving when arrow keys are released."""
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0

# --- Start the game ---
if __name__ == "__main__":
    game = CatchGame()
    game.setup()
    arcade.run()