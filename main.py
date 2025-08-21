import arcade
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from views.game_view import GameView

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game = GameView()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()