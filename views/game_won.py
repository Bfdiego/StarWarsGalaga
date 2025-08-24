import arcade
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class GameWonView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_sprite = arcade.Sprite("assets/game_won_view_1.png")
        self.background_sprite.center_x = SCREEN_WIDTH // 2
        self.background_sprite.center_y = SCREEN_HEIGHT // 2
        self.background_list = arcade.SpriteList()
        self.background_list.append(self.background_sprite)
        self.restart_text = "Press 'R' to Restart"
        self.menu_text = "Press 'M' for Menu"
        self.restart_font_size = 24

    def on_draw(self):
        self.clear()
        self.background_sprite.scale = 0.6
        self.background_list.draw()
        arcade.draw_text(self.restart_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 222,
                         arcade.color.WHITE, font_size=self.restart_font_size, anchor_x="center")
        arcade.draw_text(self.menu_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 260,
                         arcade.color.WHITE, font_size=self.restart_font_size, anchor_x="center")

    def on_key_press(self, key, modifiers):
        from views.title_view import TitleView
        from views.game_view import GameView
        if key == arcade.key.R:
            game_view = GameView()
            self.window.show_view(game_view)
        elif key == arcade.key.M:
            menu_view = TitleView()
            self.window.show_view(menu_view)

