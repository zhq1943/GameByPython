import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        """初始化飞船的位置"""
        self.screen = screen
        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将飞船放在底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.moving_right = False
        self.moving_left  = False
        self.moving_up = False
        self.moving_down = False
        
        self.ai_settings = ai_settings
        self.center_x = float(self.rect.centerx)
        
        self.on_fire = False
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """move depend on ship pos"""
        if self.moving_right:
            if self.rect.right < self.screen_rect.right:  
                self.center_x += self.ai_settings.ship_speed_factor
        elif self.moving_left:
            if self.rect.left > self.screen_rect.left:
                self.center_x -=  self.ai_settings.ship_speed_factor 
        elif self.moving_up:
            if self.rect.top > self.screen_rect.top:
                self.rect.top -= self.ai_settings.ship_speed_factor
        elif self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom:  
                self.rect.bottom += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center_x     
    def center_ship(self):
        """move ship to start position"""
        self.center  = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
