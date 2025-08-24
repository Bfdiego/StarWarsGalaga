import arcade
import random
from settings import (BOSS_SCALING, SCREEN_WIDTH)
from bullets.boss_raybull import BossRayBull

class Boss(arcade.Sprite):
    def __init__(self, image="assets/boss.png", scale=BOSS_SCALING):
        super().__init__(image, scale)
        self.image = image
        self.center_x
        self.center_y
        self.hp = 50
        self.canShoot = True
        self.canMove = True

    def shoot_raybull(self, raybull_list: arcade.SpriteList):
        raybull = BossRayBull(self.center_x, self.bottom - 240)
        raybull_list.append(raybull)

    def take_damage(self, dmg: int):
        self.hp -= dmg

    def is_dead(self) -> bool:
        return self.hp <= 0
                
    def setCanShoot(self, canShoot: bool):
        self.canShoot = canShoot
    
    def getCanShoot(self) -> bool:
        return self.canShoot
    
    def moving(self, delta_time: float):
        relative_position = random.random()
        if relative_position < 0.2:
            self.center_x = SCREEN_WIDTH // 2 -120
        elif relative_position < 0.4:
            self.center_x = SCREEN_WIDTH // 2 + 120
        elif relative_position < 0.6:
            self.center_x = SCREEN_WIDTH // 2 - 240
        elif relative_position < 0.8:
            self.center_x = SCREEN_WIDTH // 2 + 240
        else:
            self.center_x = SCREEN_WIDTH // 2
        
    def update(self, delta_time: float):
        pass
        
