import arcade
from settings import BOSS_BEAM_SPEED

class BossRayBull(arcade.Sprite):
    def __init__(self, x, y, image="assets/boss_shot.png", scale=0.8):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.change_y = BOSS_BEAM_SPEED

    def update(self):
        self.center_y += self.change_y
        if self.top < 0:
            self.remove_from_sprite_lists()