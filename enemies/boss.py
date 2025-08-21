import arcade
from settings import BOSS_SCALING
from bullets.boss_raybull import BossBeam

class Boss(arcade.Sprite):
    def __init__(self, image="assets/boss.png", scale=BOSS_SCALING):
        super().__init__(image, scale)
        self.hp = 10

    def shoot_beam(self, beam_list: arcade.SpriteList):
        beam = BossBeam(self.center_x, self.bottom - 10)
        beam_list.append(beam)

    def take_damage(self, dmg: int):
        self.hp -= dmg

    def is_dead(self) -> bool:
        return self.hp <= 0