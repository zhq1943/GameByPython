import pygame
class Ship():
    def __init__(self,screen):
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
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """move depend on ship pos"""
        if self.moving_right:
            self.rect.centerx += 1
            if self.rect.centerx > self.screen_rect.right:
                self.rect.centerx = self.screen_rect.left
        elif self.moving_left:
            self.rect.centerx -= 1  
            if self.rect.centerx < self.screen_rect.left:
                self.rect.centerx = self.screen_rect.right
        elif self.moving_up:
            self.rect.top -= 1
            if self.rect.top < 0:
                self.rect.top = 0
        elif self.moving_down:
            self.rect.bottom += 1
            if self.rect.bottom > self.screen_rect.height:
                self.rect.bottom = self.screen_rect.height       
