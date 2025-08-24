import arcade
import random
import numpy as np
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PLAYER_SPEED
)
from player.player import Player
from enemies.enemy import Enemy
from enemies.boss import Boss
from bullets.player_bullet import PlayerBullet

level = 1

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.boss_list = arcade.SpriteList()
        self.boss_bullets = arcade.SpriteList()
        self.player = Player()
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 50
        self.player_list.append(self.player)
        boss = Boss()
        boss.center_x = SCREEN_WIDTH // 2 - 120
        boss.center_y = SCREEN_HEIGHT - 90
        self.boss_list.append(boss)
        global level
        level = 1

    def on_show_view(self):
        self.setup()

    def setup(self):
        if level == 1:
            enemy_speed = 0.1
        elif level == 2:
            enemy_speed = 0.4
        elif level == 3:
            enemy_speed = 0.7
        elif level == 4:
            enemy_speed = 0.95
        else:
            enemy_speed = 1+(level * 0.05)
        cols = 6
        xs = np.linspace(100, SCREEN_WIDTH - 100, cols, dtype=int)
        for x in xs:
            enemy = Enemy()
            enemy.center_x = int(x)
            enemy.center_y = 520
            enemy.change_y = enemy_speed
            self.enemy_list.append(enemy)
            enemy2 = Enemy()
            enemy2.center_x = int(x)
            enemy2.center_y = 480
            enemy2.change_y = enemy_speed
            self.enemy_list.append(enemy2)
    
    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.boss_list.draw()
        self.boss_bullets.draw()
        arcade.draw_text(f"Level: {level}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)
        arcade.draw_text("Boss HP: " + str(self.boss_list[0].hp) if len(self.boss_list) > 0 else "Boss HP: 0",
                         SCREEN_WIDTH - 200, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = PLAYER_SPEED
        elif key == arcade.key.SPACE:
            bullet = PlayerBullet(self.player.center_x, self.player.center_y + 20)
            self.bullet_list.append(bullet)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.player.change_x = 0
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.player.change_x = 0

    def close_game(self, delta_time):
        from views.title_view import TitleView  
        self.window.show_view(TitleView())

    def clear_boss_bullet_list(self, delta_time):
        for raybull in list(self.boss_bullets):
            self.boss_bullets.remove(raybull)
        self.boss_list[0].setCanShoot(True)

    def shoot_raybull(self, delta_time):
        self.boss_list[0].shoot_raybull(self.boss_bullets)
        self.boss_list[0].setCanShoot(False)
        arcade.schedule_once(self.clear_boss_bullet_list, 1.0)
    
    def on_update(self, delta_time):
        global level
        self.player_list.update(delta_time)
        self.bullet_list.update(delta_time)
        self.enemy_list.update(delta_time)
        self.boss_list.update(delta_time)
        # self.bullet_list.update()
        # self.boss_bullets.update()
        if len(self.enemy_list) == 0:
            level += 1
            self.setup()

        for bullet in list(self.bullet_list):
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if hit_list:
                self.bullet_list.remove(bullet)
                for enemy in hit_list:
                    self.enemy_list.remove(enemy)

        if len(self.boss_list) > 0:
            boss = self.boss_list[0]
            for bullet in list(self.bullet_list):
                if arcade.check_for_collision(bullet, boss):
                    self.bullet_list.remove(bullet)
                    boss.take_damage(1)
                    if boss.is_dead():
                        boss.remove_from_sprite_lists()
                        arcade.schedule_once(self.close_game, 1.0)

            shoot_chance = random.random()
            if shoot_chance < 0.008 and boss.getCanShoot():
                boss.moving(delta_time)
                arcade.schedule_once(self.shoot_raybull, 1.0)
                

        for raybull in list(self.boss_bullets):
            hit_list = arcade.check_for_collision_with_list(raybull, self.player_list)
            if hit_list:
                # self.boss_bullets.remove(raybull)
                for player in hit_list:
                    self.player_list.remove(player)
                    arcade.schedule_once(self.close_game, 1.0)
        
        for enemy in list(self.enemy_list):
            if enemy.game_over:
                arcade.schedule_once(self.close_game, 0.5)
    

