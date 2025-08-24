import arcade
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from views.title_view import TitleView

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game = TitleView()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()