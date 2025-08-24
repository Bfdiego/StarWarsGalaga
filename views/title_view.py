import arcade
from views.game_view import GameView
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

class TitleView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_sprite = arcade.Sprite("assets/title_view.png")
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        self.background_list = arcade.SpriteList()
        self.background_list.append(self.background_sprite)
        self.start_text = "Press 'Enter' to Start"
        self.title_font_size = 36
        self.start_font_size = 24

    def on_draw(self):
        self.clear()
        self.background_sprite.scale = 0.6
        self.background_list.draw()
        arcade.draw_text(self.start_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 222,
                         arcade.color.WHITE, font_size=self.start_font_size, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game_view = GameView()
            self.window.show_view(game_view)