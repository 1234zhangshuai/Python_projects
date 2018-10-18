
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所在的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen
        
        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        # ship.rect.top表示在飞船的上面（即将发射的状态)
        self.rect.top = ship.rect.top        
        
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值(因为随着子弹的运行，y坐标值减小)
        self.y -= self.speed_factor
        # 更新表示子弹的rect的设置
        self.rect.y = self.y
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
    
        
        
        
        
        
        
        
        
        
    #     # 绘制子弹及屏幕外接矩形
    #     self.image_bullet = pygame.image.load('image/bullet.bmp')
    #     self.rect_bullet = self.image_bullet.get_rect()
    #     self.screen_rect = self.screen.get_rect()
    #
    #     # 将子弹放到屏幕的中央
    #     self.rect_centerx = self.screen_rect.centerx
    #     self.rect_centery = self.screen_rect.centery
    #
    #     # 在子弹的属性center中储存小数值
    #     # self.center_bullet = float()
    #
    # def update_bullet(self):
    #     """根据移动标志调整子弹的位置"""
    #     if self.moving_right and self.rect_bullet.right < self.screen_rect.right:
    #         self.centerx += 1
    #     if self.moving_left and self.rect.left > 0:
    #         self.centerx -= 1
    #     if self.moving_down and self.rect.down < self.screen_rect.down:
    #         self.centery += 1
    #     if self.moving_up and self.rect.up > 0:
    #         self.centery -= 1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
#        if event.key == pygame.K_RIGHT:
#            self.centerx += 1
#        if event.key == pygame.K_LEFT:
#            self.centerx -= 1
#        if event.key == K_UP:
#            self.centery += 1
#        if event.key == K_DOWN:
#            self.centerx -= 1
