import arcade
from settings import PLAYER_SPEED, PLAYER_SCALING, SCREEN_WIDTH

class Player(arcade.Sprite):
    def __init__(self, image="assets/player.png", scale=PLAYER_SCALING):
        super().__init__(image, scale)
        self.change_x = 0
        self.image = image
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 50

    def update(self, delta_time: float):
        self.center_x += self.change_x
        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

         