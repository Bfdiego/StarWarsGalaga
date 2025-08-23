import arcade
from settings import BOSS_SCALING
from bullets.boss_raybull import BossRayBull

class Boss(arcade.Sprite):
    def __init__(self, image="assets/boss.png", scale=BOSS_SCALING):
        super().__init__(image, scale)
        self.hp = 10
        self.canShoot = True

    def shoot_raybull(self, raybull_list: arcade.SpriteList):
        raybull = BossRayBull(self.center_x, self.bottom - 270)
        raybull_list.append(raybull)

    def take_damage(self, dmg: int):
        self.hp -= dmg

    def is_dead(self) -> bool:
        return self.hp <= 0
                
    def setCanShoot(self, canShoot: bool):
        self.canShoot = canShoot
    
    def getCanShoot(self) -> bool:
        return self.canShoot
    
    def update(self, delta_time: float, raybull_list: arcade.SpriteList):
        pass
