import arcade
from settings import BULLET_SPEED, SCREEN_HEIGHT

class PlayerBullet(arcade.Sprite):
    def __init__(self, x, y, image="assets/player.png", scale=0.10):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.change_y = BULLET_SPEED

    def update(self, delta_time: float):
        self.center_y += self.change_y
        if self.top > SCREEN_HEIGHT:
            self.remove_from_sprite_lists()