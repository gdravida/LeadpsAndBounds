import os
import random
import timeit
import arcade
from level1 import BIRD
from level2 import BIRD2
from level3 import BIRD3


SPRITE_SCALING = 0.6
SPRITE_SCALING_COIN = 0.7
SPRITE_SCALING_BIRD=0.2

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Big Ole' Frog"
NUMBER_OF_COINS=25
NUMBER_OF_BIRDS=8

INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)


        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None
        self.coin_list = None
        self.bird_list=[]

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.view_bottom = 0
        self.view_left = 0
        self.score=0
        self.level=1

        self.processing_time=0
        self.draw_time=0
        self.frame_count=0
        self.fps_start_timer=None
        self.fps=None

        self.game_over = arcade.load_sound("Audio/GameOver.wav")
        self.current_state = INSTRUCTIONS_PAGE_0

        self.instructions = []
        texture = arcade.load_texture("images/play.png")
        self.instructions.append(texture)


        self.gameover = arcade.load_texture("images/gameover.png")



    def level_1(self):
        for i in range(NUMBER_OF_BIRDS):
            bird = BIRD("images/bird.png", SPRITE_SCALING_BIRD)
            print(str(bird))
            bird_placed_successfully = False

                # Keep trying until success
            while not bird_placed_successfully:
                    # Position the coin
                bird.center_x = random.randrange(SCREEN_WIDTH)
                bird.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the coin is hitting another coin
                bird_hit_list = arcade.check_for_collision_with_list(bird, self.bird_list)

                if len(bird_hit_list) == 0:
                        # It is!
                    bird_placed_successfully = True

                # Add the coin to the lists
            self.bird_list.append(bird)

            # Create the coins
        for i in range(NUMBER_OF_COINS):

                # Create the coin instance
            coin = arcade.Sprite("images/crab_meat.png", SPRITE_SCALING_COIN)

                # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

                # Keep trying until success
            while not coin_placed_successfully:
                    # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(coin_hit_list) == 0:
                        # It is!
                    coin_placed_successfully = True

                # Add the coin to the lists
            self.coin_list.append(coin)

    def level_2(self):
        for i in range(NUMBER_OF_BIRDS):
            bird = BIRD2("images/bird.png", SPRITE_SCALING_BIRD)
            print(str(bird))
            bird_placed_successfully = False

                # Keep trying until success
            while not bird_placed_successfully:
                    # Position the coin
                bird.center_x = random.randrange(SCREEN_WIDTH)
                bird.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the coin is hitting another coin
                bird_hit_list = arcade.check_for_collision_with_list(bird, self.bird_list)

                if len(bird_hit_list) == 0:
                        # It is!
                    bird_placed_successfully = True

                # Add the coin to the lists
            self.bird_list.append(bird)

            # Create the coins
        for i in range(NUMBER_OF_COINS):

                # Create the coin instance
            coin = arcade.Sprite("images/crab_meat.png", SPRITE_SCALING_COIN)

                # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

                # Keep trying until success
            while not coin_placed_successfully:
                    # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(coin_hit_list) == 0:
                        # It is!
                    coin_placed_successfully = True

                # Add the coin to the lists
            self.coin_list.append(coin)

    def level_3(self):
        for i in range(NUMBER_OF_BIRDS):
            bird = BIRD3("images/bird.png", SPRITE_SCALING_BIRD)
            print(str(bird))
            bird_placed_successfully = False

                # Keep trying until success
            while not bird_placed_successfully:
                    # Position the coin
                bird.center_x = random.randrange(SCREEN_WIDTH)
                bird.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the coin is hitting another coin
                bird_hit_list = arcade.check_for_collision_with_list(bird, self.bird_list)

                if len(bird_hit_list) == 0:
                        # It is!
                    bird_placed_successfully = True

                # Add the coin to the lists
            self.bird_list.append(bird)

            # Create the coins
        for i in range(NUMBER_OF_COINS):

                # Create the coin instance
            coin = arcade.Sprite("images/crab_meat.png", SPRITE_SCALING_COIN)

                # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

                # Keep trying until success
            while not coin_placed_successfully:
                    # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(coin_hit_list) == 0:
                        # It is!
                    coin_placed_successfully = True

                # Add the coin to the lists
            self.coin_list.append(coin)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bird_list=arcade.SpriteList()

        self.score=0
        self.level=1

        # Set up the player
        self.player_sprite = arcade.Sprite("images/froggy.png" )
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, arcade.SpriteList())

        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0
        self.level_1()

    def draw_instructions_page(self, page_number):
        """
        Draw an instruction page. Load the page as an image.
        """
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """

        output = "Game Over"
        arcade.draw_text(output, 100, 400, arcade.color.BLACK, 54)

        output = "Click to restart"
        arcade.draw_text(output, 180, 300, arcade.color.BLACK, 24)



    def draw_game(self):
        """
        Render the screen.
        """
        draw_start_time=timeit.default_timer()

        if self.frame_count % 60 == 0:
            if self.fps_start_timer is not None:
                total_time=timeit.default_timer()-self.fps_start_timer
                self.fps=60/total_time
            self.fps_start_timer=timeit.default_timer()
        self.frame_count += 1

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()
        self.coin_list.draw()
        self.bird_list.draw()

        output = f"Score:{self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

        output = f"Level: {self.level}"
        arcade.draw_text(output, 10, 35, arcade.color.WHITE, 15)
        self.draw_time = timeit.default_timer() - draw_start_time

    def on_draw(self):
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == INSTRUCTIONS_PAGE_0:
                # Next page of instructions.
                # Start the game
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
                # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        self.coin_list.update()

        coins_hit_list=arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.game_over)
            self.score+=1
        if len(self.coin_list)==0 and self.level==1:
            self.level+=1
            self.level_2()
        elif len(self.coin_list)==0 and self.level==2:
            self.level+=1
            self.level_3()
        if self.current_state == GAME_RUNNING:
            self.bird_list.update()
        if len(self.coin_list) == 0:
            self.current_state = GAME_OVER

        bird_hit_list=arcade.check_for_collision_with_list(self.player_sprite, self.bird_list)
        if any(bird_hit_list):
            self.current_state = GAME_OVER

        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        elif self.player_sprite.right > SCREEN_WIDTH - 1:
            self.player_sprite.right = SCREEN_WIDTH - 1

        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        elif self.player_sprite.top > SCREEN_HEIGHT - 1:
            self.player_sprite.top = SCREEN_HEIGHT - 1


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()