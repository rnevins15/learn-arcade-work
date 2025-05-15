import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Falling Objects Catcher - Part 2"

PLAYER_SPEED = 5
SPAWN_RATE = 0.01
MAX_LIVES = 3

class FallingItem(arcade.Sprite):
    def __init__(self, image, scale, item_type):
        super().__init__(image, scale)
        self.item_type = item_type

    def update(self):
        self.center_y -= self.change_y
        self.center_x += self.change_x

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.top < 0:
            self.remove_from_sprite_lists()

class CatchGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.player = None
        self.items = None
        self.score = 0
        self.lives = MAX_LIVES
        self.level = 1
        self.spawn_timer = 0
        self.game_over = False
        self.current_screen = "start"
        self.slow_motion_active = False
        self.slow_motion_timer = 0
        self.catch_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.powerup_sound = arcade.load_sound(":resources:sounds/upgrade1.wav")

    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png", 0.5)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 60
        self.items = arcade.SpriteList()
        self.score = 0
        self.lives = MAX_LIVES
        self.level = 1
        self.spawn_timer = 0
        self.game_over = False
        self.slow_motion_active = False
        self.slow_motion_timer = 0

    def on_draw(self):
        arcade.start_render()
        if self.current_screen == "start":
            arcade.draw_text("Falling Objects Catcher", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, arcade.color.WHITE, font_size=36, anchor_x="center")
            arcade.draw_text("Catch the mushrooms!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40, arcade.color.LIGHT_GREEN, 20, anchor_x="center")
            arcade.draw_text("Avoid the bombs!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10, arcade.color.RED, 20, anchor_x="center")
            arcade.draw_text("Blue Gems give you extra lives!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, arcade.color.PINK, 20, anchor_x="center")
            arcade.draw_text("Green Flags = Slow Motion!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, arcade.color.LIGHT_BLUE, 20, anchor_x="center")
            arcade.draw_text("Use ARROW KEYS to move", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 90, arcade.color.GRAY, 16, anchor_x="center")
            arcade.draw_text("Press SPACE to Start", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 140, arcade.color.YELLOW, 24, anchor_x="center")
        elif self.current_screen == "game":
            self.player.draw()
            self.items.draw()
            arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)
            arcade.draw_text(f"Lives: {self.lives}", SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)
            arcade.draw_text(f"Level: {self.level}", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20, anchor_x="center")
            if self.slow_motion_active:
                arcade.draw_text("SLOW MOTION!", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60, arcade.color.LIGHT_BLUE, 20, anchor_x="center")
        elif self.current_screen == "game_over":
            arcade.draw_text("GAME OVER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40, arcade.color.RED, 40, anchor_x="center")
            arcade.draw_text(f"Final Score: {self.score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, 24, anchor_x="center")
            arcade.draw_text("Press SPACE to Restart", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60, arcade.color.YELLOW, 20, anchor_x="center")

    def on_update(self, delta_time):
        if self.current_screen != "game" or self.game_over:
            return

        self.spawn_timer += delta_time
        if self.spawn_timer > 10:
            self.spawn_timer = 0
            self.level += 1

        spawn_chance = SPAWN_RATE + 0.005 * self.level
        if random.random() < spawn_chance:
            rand = random.random()
            if rand < 0.6:
                item = FallingItem(":resources:images/tiles/mushroomRed.png", 0.5, "good")
            elif rand < 0.75:
                item = FallingItem(":resources:images/tiles/bomb.png", 0.5, "bad")
            elif rand < 0.85:
                item = FallingItem(":resources:images/items/gemBlue.png", 0.5, "powerup")
            elif rand < 0.95:
                item = FallingItem(":resources:images/items/flagGreen2.png", 0.5, "slow")
            elif rand < 0.985:
                item = FallingItem(":resources:images/items/coinGold.png", 0.5, "bonus")
            else:
                item = FallingItem(":resources:images/enemies/fly.png", 0.5, "enemy")

            base_speed = random.uniform(3 + self.level, 8 + self.level)
            item.change_y = base_speed * 0.5 if self.slow_motion_active else base_speed
            item.change_x = random.uniform(-1.5, 1.5)
            item.center_x = random.randint(20, SCREEN_WIDTH - 20)
            item.center_y = SCREEN_HEIGHT + 20
            self.items.append(item)

        self.items.update()
        self.player.update()

        if self.player.left < 0:
            self.player.left = 0
        elif self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

        if self.player.bottom < 0:
            self.player.bottom = 0
        elif self.player.top > SCREEN_HEIGHT:
            self.player.top = SCREEN_HEIGHT

        for item in self.items:
            if arcade.check_for_collision(self.player, item):
                if item.item_type == "good":
                    self.score += 1
                    arcade.play_sound(self.catch_sound)
                elif item.item_type == "bad":
                    self.lives -= 1
                    arcade.play_sound(self.hit_sound)
                    if self.lives <= 0:
                        self.game_over = True
                        self.current_screen = "game_over"
                elif item.item_type == "powerup":
                    if self.lives < MAX_LIVES:
                        self.lives += 1
                    arcade.play_sound(self.powerup_sound)
                elif item.item_type == "slow":
                    self.slow_motion_active = True
                    self.slow_motion_timer = 5.0
                    arcade.play_sound(self.powerup_sound)
                elif item.item_type == "bonus":
                    self.score += 5
                    arcade.play_sound(self.catch_sound)
                elif item.item_type == "enemy":
                    self.lives -= 2
                    arcade.play_sound(self.hit_sound)
                    if self.lives <= 0:
                        self.game_over = True
                        self.current_screen = "game_over"
                item.remove_from_sprite_lists()

        if self.slow_motion_active:
            self.slow_motion_timer -= delta_time
            if self.slow_motion_timer <= 0:
                self.slow_motion_active = False

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.current_screen == "start":
                self.setup()
                self.current_screen = "game"
            elif self.current_screen == "game_over":
                self.setup()
                self.current_screen = "game"
        if self.current_screen != "game":
            return
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0

if __name__ == "__main__":
    game = CatchGame()
    arcade.run()