import arcade

class BossRayBull(arcade.Sprite):
    def __init__(self, x, y, image="assets/boss_shot.png", scale=0.8):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y

    def update(self):
        pass