""" Lab 9 - Sprite Collection Game """

import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 9 - Custom Sprite Game")

        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        self.player_sprite = None
        self.physics_engine = None

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.score = 0
        self.collect_sound = None

    def setup(self):
        """ Set up the game and initialize variables. """
        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        # --- CITE GRAPHICS/SOUNDS ---
        # Graphics from Kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk0.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # --- Wall textures
        wall_textures = [":resources:images/tiles/boxCrate_single.png", ":resources:images/tiles/boxCrate_single.png", ":resources:images/tiles/boxCrate_single.png"]

        # --- Custom wall layout with boundary walls
        for x in range(0, SCREEN_WIDTH, 64):
            for y in range(0, SCREEN_HEIGHT, 64):
                if x == 0 or x == SCREEN_WIDTH - 64 or y == 0 or y == SCREEN_HEIGHT - 64:
                    wall = arcade.Sprite(random.choice(wall_textures), SPRITE_SCALING_BOX)
                    wall.center_x = x + 32
                    wall.center_y = y + 32
                    self.wall_list.append(wall)

        # Inner structure (cross pattern)
        for x in range(160, 640, 64):
            wall = arcade.Sprite(random.choice(wall_textures), SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = SCREEN_HEIGHT // 2
            self.wall_list.append(wall)
        for y in range(128, 480, 64):
            wall = arcade.Sprite(random.choice(wall_textures), SPRITE_SCALING_BOX)
            wall.center_x = SCREEN_WIDTH // 2
            wall.center_y = y
            self.wall_list.append(wall)

        # --- Coins
        coin_texture = ":resources:images/items/coinGold.png"
        for _ in range(30):
            coin = arcade.Sprite(coin_texture, SPRITE_SCALING_COIN)
            placed = False
            while not placed:
                coin.center_x = random.randrange(64, SCREEN_WIDTH - 64)
                coin.center_y = random.randrange(64, SCREEN_HEIGHT - 64)
                if not arcade.check_for_collision_with_list(coin, self.wall_list):
                    placed = True
            self.coin_list.append(coin)

        # --- Load sound
        self.collect_sound = arcade.load_sound(":resources:sounds/coin1.wav")

        # Physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.camera_for_sprites.use()
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        self.physics_engine.update()

        # Collect coins
        coins_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.collect_sound)

        # Camera scroll
        CAMERA_SPEED = 1
        lower_left = (self.player_sprite.center_x - self.width / 2,
                      self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player_sprite.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player_sprite.change_x = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()