import arcade
from settings import ENEMY_SCALING

class Enemy(arcade.Sprite):
    def __init__(self, image="assets/player.png", scale=ENEMY_SCALING):
        super().__init__(image, scale)
        self.center_x
        self.center_y 
        self.change_y = 0.1

    def update(self, delta_time: float):
        self.center_y -= self.change_y
        pass