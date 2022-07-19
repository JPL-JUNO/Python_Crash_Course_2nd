import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    管理游戏资源和行为的类
    """

    def __init__(self):
        """
        初始化游戏并创建游戏资源
        """
        pygame.init()
        # 创建setting实例
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width,
        #                                        self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """
        开始游戏的主循环
        :return:
        """
        while True:
            # 监视键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """
        响应按键和鼠标事件
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """
        响应按键
        :param event:
        :return:
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """
        更新屏幕上的图像，并切换到新屏幕
        :return:
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
