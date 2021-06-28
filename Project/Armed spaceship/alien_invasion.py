
# 模块pygame包含开发游戏所需的功能。玩家退出时，使用模块sys中的工具来退出。
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """ 管理游戏资源和行为的类 """

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()
        self.settings = Settings()

        # 设置背景色(浅灰色)
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # 由于无法预先知道屏幕的宽度和高度，要在创建屏幕后更新这些设置
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """ 开始游戏的主循环 """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self.__update_bullets()
            self._update_screen()

    def __update_bullets(self):
        """ 更新子弹的位置并删除消失的子弹。"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹
        # 使用for循环便利列表（或Pygame编组）时，Python要求该列表的长度在整个循环中保持不变。
        # 因为不能从for循环遍历的列表或编组中删除元素，所以必须遍历组的副本。
        # 使用copy()来设置for循环，从而能够在循环中修改bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _check_events(self):
        """ 响应按键和鼠标事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)                    
                
    def _check_keydown_events(self, event):
        """ 响应按键。 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        # 按空格键时调用_fire_bullet()。
        elif event.key ==pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """ 响应松开。 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """ 创建一颗子弹，并将其加入编组bullets中。"""

        # 在创建新子弹前检查未消失的子弹数是否小于该设置
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_screen(self):
        """ 更新屏幕上的图像，并切换到新屏幕。"""
        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见。
        pygame.display.flip()



if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()




