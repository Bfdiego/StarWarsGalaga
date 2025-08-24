import arcade
from settings import ENEMY_SCALING

class Enemy(arcade.Sprite):
    def __init__(self, image="assets/enemy.png", scale=ENEMY_SCALING):
        super().__init__(image, scale)
        self.center_x
        self.center_y 
        self.change_y = 0.1
        self.game_over = False

    def update(self, delta_time: float):
        self.center_y -= self.change_y
        self.scale = ENEMY_SCALING + (0.00015 * (600 - self.center_y))
        if self.bottom < 60:
            self.game_over = True